# Markdown typography QA audit script
param(
  [string]$RootDir = 'doc/UserGuide',
  [string]$OutFile = 'doc/UserGuide/.lint/typography-qa-report.txt'
)

$ErrorActionPreference = 'Stop'
if (!(Test-Path -LiteralPath $RootDir)) {
  Write-Error "Root directory not found: $RootDir"
}

$outDir = Split-Path -Parent $OutFile
if (!(Test-Path -LiteralPath $outDir)) { New-Item -ItemType Directory -Path $outDir | Out-Null }

$files = rg --files $RootDir -g '*.md'
Write-Host ("Scanning {0} files under {1}" -f ($files | Measure-Object | Select-Object -ExpandProperty Count), $RootDir)
$results = @()

function Add-Result {
  param($file,$line,$type,$severity,$msg)
  $results += [pscustomobject]@{file=$file; line=[int]$line; type=$type; severity=$severity; msg=$msg}
}

foreach ($file in $files) {
  $lines = Get-Content -LiteralPath $file -Encoding UTF8
  $inCode = $false; $codeFenceLine = 0; $prevHeadingLevel = $null; $seenH1 = $false; $lineNum = 0
  $ordListActive = $false; $expectedNum = 0
  $blankRun = 0

  foreach ($line in $lines) {
    $lineNum++
    $trim = $line.TrimEnd()
    $isBlank = ($trim -eq '')
    if ($isBlank) { $blankRun++ } else { if ($blankRun -ge 3) { Add-Result $file ($lineNum-1) 'excessive-blank-lines' 'minor' ("出现连续 $blankRun 行空行") }; $blankRun = 0 }

    if ($trim -match '^[`]{3,}') {
      if (-not $inCode) {
        $inCode = $true; $codeFenceLine = $lineNum
        if ($trim -match '^```\s*$') { Add-Result $file $lineNum 'codeblock-missing-language' 'major' '代码块缺少语言标记' }
      } else { $inCode = $false; $codeFenceLine = 0 }
      continue
    }
    if ($inCode) { continue }

    if ($trim -match '^\*\*(.+)\*\*\s*$') {
      $content = $matches[1]; if ($content.Length -ge 60) { Add-Result $file $lineNum 'bold-paragraph' 'major' '整段或超长段落被加粗' }
    }
    $boldPattern = '\*\*([^*]|\*(?!\*))+\*\*'
    $m = [regex]::Matches($line, $boldPattern)
    foreach ($mm in $m) { $len = $mm.Value.Length - 4; if ($len -ge 40) { Add-Result $file $lineNum 'bold-too-long' 'moderate' ("单个加粗片段过长: $len 字符") } }

    if ($trim -match '^(#{1,6})\s+(.+)$') {
      $level = $matches[1].Length
      if ($level -eq 1) { if ($seenH1) { Add-Result $file $lineNum 'multiple-h1' 'major' '文档包含多个H1标题' } else { $seenH1 = $true } }
      if ($prevHeadingLevel -ne $null) { if ($level -gt ($prevHeadingLevel + 1)) { Add-Result $file $lineNum 'heading-jump' 'major' ("标题层级跳跃: 上一层级 $prevHeadingLevel -> 当前 $level") } }
      $prevHeadingLevel = $level
    }
    if ($trim -match '^={3,}$') { Add-Result $file $lineNum 'setext-heading' 'moderate' '使用了下划线式H1(===)，应统一为# 样式' }
    if ($trim -match '^-{3,}$') { Add-Result $file $lineNum 'setext-heading' 'moderate' '使用了下划线式H2(---)，应统一为# 样式' }

    if ($line -match '^(\s{0,3})(\d+)\.\s+') {
      if (-not $ordListActive) { $ordListActive = $true; $expectedNum = [int]$matches[2] }
      else { $expectedNum++; if ([int]$matches[2] -ne $expectedNum) { Add-Result $file $lineNum 'ordered-list-nonconsecutive' 'moderate' ("有序列表编号不连续: 期望 $expectedNum 实际 $($matches[2])") } }
    }
    else { if ($ordListActive) { if (-not $isBlank) { $ordListActive = $false; $expectedNum = 0 } } }

    if ($line -match '^(\s*)([\*\+])\s+') { $sym = $matches[2]; Add-Result $file $lineNum 'unordered-bullet-style' 'moderate' ("无序列表符号应统一为 '-'，发现 '$sym'") }
    if ($line -match '^(\t+)[-\*\+]\s+') { Add-Result $file $lineNum 'list-indent-tabs' 'minor' '列表缩进使用了TAB，应使用空格' }

    $inline = [regex]::Matches($line,'`([^`]+)`')
    foreach ($ic in $inline) { if (($ic.Groups[1].Value).Length -ge 60) { Add-Result $file $lineNum 'inline-code-too-long' 'minor' '内联代码过长，应改为代码块' } }
    if ($line -match '\$') { if ($inline.Count -eq 0) { Add-Result $file $lineNum 'dollar-outside-code' 'minor' '检测到 $ 符号不在代码环境，需确认是否应使用内联代码或转义' } }

    if ($line -match '(?<=\p{IsCJKUnifiedIdeographs})[()]|[()](?=\p{IsCJKUnifiedIdeographs})') { Add-Result $file $lineNum 'mixed-parentheses' 'minor' '中英对照括号风格不统一，建议使用全角（），或统一规范' }
  }
  if ($inCode) { Add-Result $file $codeFenceLine 'codeblock-unclosed' 'major' '代码块未闭合' }
  if (-not $seenH1) { Add-Result $file 1 'missing-h1' 'major' '文档缺少H1标题' }
}

$ts = (Get-Date).ToString('yyyy-MM-dd HH:mm')
$header = @(
  "# Typography QA Report",
  "Generated: $ts",
  "Root: $RootDir",
  "",
  "格式: file:line|type|severity|message",
  ""
)

$summary = ($results | Group-Object type, severity | Sort-Object Count -Descending | ForEach-Object { "SUMMARY|$($_.Name)|$($_.Count)" })

$body = ($results | Sort-Object file, line | ForEach-Object { "{0}:{1}|{2}|{3}|{4}" -f $_.file,$_.line,$_.type,$_.severity,$_.msg })

@($header + $summary + "" + $body) | Set-Content -LiteralPath $OutFile -Encoding UTF8

Write-Host ("Found {0} issues" -f $results.Count)
Write-Host "Report written to: $OutFile"
