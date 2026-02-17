# Compare renamed UserGuide Markdown files with old HTML originals
param(
  [string]$NewRoot = "D:\\data\\project\\modelE2.1.2_Lazenca\\doc\\UserGuide",
  [string]$OldRoot = "D:\\data\\project\\modelE2.1.2_Lazenca\\doc\\archive-old-doc\\UserGuide",
  [string]$ReportPath = "D:\\data\\project\\modelE2.1.2_Lazenca\\.claude\\review-userguide-renamed.txt"
)

function Normalize-MarkdownEnglish([string]$text) {
  # Drop code fences markers but keep code content
  $t = $text -replace '```[a-zA-Z0-9_-]*', '' -replace '```', ''
  # Remove markdown emphasis and headings markers
  $t = $t -replace '^[#>]+\s*', '' -replace '\*\*', '' -replace '\*', ''
  # Remove inline code backticks
  $t = $t -replace '\`', ''
  # Remove Chinese characters and common CJK punctuation
  $t = [regex]::Replace($t, "[\u2E80-\u2FFF\u3000-\u303F\u3040-\u30FF\u31C0-\u31EF\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF]", "")
  # Collapse whitespace
  $t = ($t -replace "\s+", " ").Trim()
  return $t
}

function Html-ToText([string]$html) {
  # Decode basic entities
  $t = $html -replace "&quot;", '"' -replace "&amp;", "&" -replace "&lt;", "<" -replace "&gt;", ">"
  # Remove style/script
  $t = [regex]::Replace($t, "<script[\s\S]*?</script>", "", 'IgnoreCase')
  $t = [regex]::Replace($t, "<style[\s\S]*?</style>", "", 'IgnoreCase')
  # Replace <br> and <p> with newlines
  $t = $t -replace "<br\s*/?>", "`n" -replace "</p>", "`n" -replace "<p[^>]*>", ""
  # Remove all tags
  $t = [regex]::Replace($t, "<[^>]+>", "")
  # Collapse whitespace
  $t = ($t -replace "\s+", " ").Trim()
  return $t
}

function Map-NewMd-To-OldHtml([IO.FileInfo]$mdFile) {
  $name = $mdFile.Name
  if ($name -eq 'index.md') { return $null }
  # Strip numeric prefix and dash
  $base = $name -replace "^[0-9]+(\.[0-9]+)*-", ""
  $html = [System.IO.Path]::ChangeExtension($base, ".html")
  # Special case: diagnostics.md
  if ($html -eq 'diagnostics.md') { $html = 'diagnostics.html' }
  # Map to known typo filename 'Getting_the_code_form_GISS_repository.html'
  if ($html -eq 'Getting_the_code_from_GISS_repository.html') {
    $html = 'Getting_the_code_form_GISS_repository.html'
  }
  return Join-Path $OldRoot $html
}

New-Item -ItemType Directory -Force -Path ([System.IO.Path]::GetDirectoryName($ReportPath)) | Out-Null
"UserGuide Renamed Docs Review (auto-compare)" | Set-Content -Path $ReportPath -Encoding UTF8
Add-Content -Path $ReportPath -Value ("Generated: " + (Get-Date).ToString('yyyy-MM-dd HH:mm'))

$mdFiles = Get-ChildItem -File -Path $NewRoot -Filter *.md | Where-Object { $_.Name -ne 'index.md' }

$summary = @()
$details = @()

foreach ($md in $mdFiles) {
  $oldPath = Map-NewMd-To-OldHtml $md
  $status = ''
  $notes = ''
  if (-not $oldPath -or -not (Test-Path $oldPath)) {
    $status = 'UNMAPPED'
    $notes = 'No corresponding old HTML found'
    $summary += [PSCustomObject]@{ File=$md.Name; OldHtml=[System.IO.Path]::GetFileName($oldPath); Status=$status; Notes=$notes }
    continue
  }
  $mdText = Get-Content -Raw -Path $md.FullName
  $htmlText = Get-Content -Raw -Path $oldPath
  $mdNorm = Normalize-MarkdownEnglish $mdText
  $htmlNorm = Html-ToText $htmlText
  # Compare normalized strings
  if ($mdNorm -eq $htmlNorm) {
    $status = 'MATCH'
  } else {
    $status = 'DIFF'
    # Produce lightweight diff context by words
    $mdWords = ($mdNorm -split '\s+')
    $htmlWords = ($htmlNorm -split '\s+')
    $len = [Math]::Min($mdWords.Length, $htmlWords.Length)
    $firstDiff = -1
    for ($i=0; $i -lt $len; $i++) {
      if ($mdWords[$i] -ne $htmlWords[$i]) { $firstDiff = $i; break }
    }
    if ($firstDiff -ge 0) {
      $mdSnippet = ($mdWords[ [Math]::Max(0,$firstDiff-10) .. [Math]::Min($mdWords.Length-1, $firstDiff+10) ]) -join ' '
      $htmlSnippet = ($htmlWords[ [Math]::Max(0,$firstDiff-10) .. [Math]::Min($htmlWords.Length-1, $firstDiff+10) ]) -join ' '
      $notes = "First diff near: NEW=[$mdSnippet] | OLD=[$htmlSnippet]"
    } else {
      $notes = 'Different lengths or ordering after normalization'
    }
  }
  $summary += [PSCustomObject]@{ File=$md.Name; OldHtml=[System.IO.Path]::GetFileName($oldPath); Status=$status; Notes=$notes }
}

# Link integrity scan
$linkIssues = @()
foreach ($md in $mdFiles) {
  $content = Get-Content -Raw -Path $md.FullName
  $matches = Select-String -InputObject $content -Pattern "\[(?<text>[^\]]+)\]\((?<url>[^)]+)\)" -AllMatches
  foreach ($m in $matches.Matches) {
    $url = $m.Groups['url'].Value
    if ($url.StartsWith('#')) { continue }
    $target = $url.Split('#')[0]
    if ($target -like '*.md') {
      $p = Join-Path $NewRoot $target
      if (-not (Test-Path $p)) {
        $linkIssues += [PSCustomObject]@{ File=$md.Name; Link=$url; Issue='Target file not found' }
      }
      if (-not ($target -match '^[0-9]+\.' ) -and $md.Name -ne 'index.md') {
        $linkIssues += [PSCustomObject]@{ File=$md.Name; Link=$url; Issue='Target lacks numeric prefix' }
      }
    }
  }
}

Add-Content -Path $ReportPath -Value "`n== Summary =="
$summary | Sort-Object File | ForEach-Object { Add-Content -Path $ReportPath -Value ("{0} | {1} | {2} | {3}" -f $_.File, $_.OldHtml, $_.Status, $_.Notes) }

Add-Content -Path $ReportPath -Value "`n== Link Issues =="
if ($linkIssues.Count -eq 0) { Add-Content -Path $ReportPath -Value "None" } else { $linkIssues | Sort-Object File | ForEach-Object { Add-Content -Path $ReportPath -Value ("{0} | {1} | {2}" -f $_.File, $_.Link, $_.Issue) } }

Write-Output "Report written: $ReportPath"
