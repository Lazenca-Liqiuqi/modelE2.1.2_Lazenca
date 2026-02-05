# Git HOW-TO document for the GISS GCM
# GISS GCM的Git使用指南文档

---

## Git

Git is a revision control system as CVS is.
Git是像CVS一样的版本控制系统。

The main difference between these two systems is that Git is a "distributed" revision control system.
这两个系统的主要区别在于Git是一个"分布式"版本控制系统。

This means that each checked out copy of the code ("cloned" in git terms) contains the entire history of the project and in theory can serve as a new repository.
这意味着每个检出的代码副本（在Git术语中称为"克隆"）都包含项目的完整历史，理论上可以作为一个新的仓库。

This allows to perform a lot of operations locally, without accessing the central repository.
这使得可以在本地执行许多操作，而无需访问中央仓库。

These operations include looking into the history, switching between the branches, comparing modified code in the local directory to the original code etc.
这些操作包括查看历史记录、在分支之间切换、将本地目录中修改的代码与原始代码进行比较等。

Local operations are much faster and one doesn't need network access when performing them.
本地操作要快得多，并且在执行时不需要网络访问。

Particularly useful are local commits.
本地提交特别有用。

"git commit -a" will commit changes to local repository, nobody will see them until they are sent to central repository (with "git push").
"git commit -a"将把更改提交到本地仓库，在它们被发送到中央仓库之前（使用"git push"），没有人会看到这些更改。

So while working on ones own code the developer can do a lot of commits to memorize the various stages of the local code.
因此，在处理自己的代码时，开发者可以进行大量提交，以记录本地代码的各个阶段。

These commits will not interfere with other peoples work and will not be visible to others until the developer sends them to the central repository with "git push".
这些提交不会干扰其他人的工作，并且在开发者使用"git push"将它们发送到中央仓库之前，对其他人不可见。

One should remember though that until the code is pushed to the central repository it is developers responsibility to back it up.
但请记住，在代码被推送到中央仓库之前，备份代码是开发者的责任。

Since by its nature Git doesn't force the developer to send changes to the central repository as often as CVS does, it is advisable that one keeps the local copy of the code on a filesystem which is regularly backed up.
由于Git本质上不像CVS那样强制开发者频繁地将更改发送到中央仓库，因此建议将代码的本地副本保存在定期备份的文件系统上。

---

## Setting Up

To work with Git you need to have it installed on your computer.
要使用Git，您需要在计算机上安装它。

We are planning to use some functionality which was added in 1.7.0 version of git.
我们计划使用在Git 1.7.0版本中添加的某些功能。

So preferably you should install version no older than 1.7.0.
因此，最好安装不低于1.7.0的版本。

Older version will work for most operations but you may see some problems in the future.
较旧的版本适用于大多数操作，但将来可能会遇到一些问题。

On Discover the latest version of Git is available as a module.
在Discover上，最新版本的Git可作为模块使用。

You can load it with:
您可以使用以下命令加载它：

```bash
module load other/git-1.7.3.4
```

If you want to install it on your own workstation or laptop, git is available through Mac ports on Mac and as a rpm package on Linux (use EPEL repository on Red Hat 5).
如果您想在自己的工作站或笔记本电脑上安装它，Git可通过MacPorts在Mac上获得，或在Linux上作为rpm包获得（在Red Hat 5上使用EPEL仓库）。

Of course, you can always compile it from the source (real easy) which you can get from
当然，您始终可以从源代码编译它（非常简单），源代码可从以下地址获取：

```
http://git-scm.com/download
```

You also have to set the following environment variables:
您还必须设置以下环境变量：

```bash
export GIT_AUTHOR_NAME="your_name"
export GIT_AUTHOR_EMAIL=your_email
export GIT_COMMITTER_NAME="your_name"
export GIT_COMMITTER_EMAIL=your_email
```

where `your_name` is the name Git will be using to identify you (in commit info etc.), so preferably use your full name like "John Smith" to avoid confusion.
其中`your_name`是Git将用来识别您的名称（在提交信息等中），因此最好使用您的全名，如"John Smith"，以避免混淆。

`your_email` is the email which will be stored together with your name and which people can use to contact you.
`your_email`是将与您的名称一起存储的电子邮件，人们可以使用它来联系您。

If you are going to use Git on more than one computer make sure that these variable are set to identical values on all computers.
如果您将在多台计算机上使用Git，请确保这些变量在所有计算机上设置为相同的值。

---

## Useful Git commands

Useful Git commands (apart from the initial "git clone ..." all commands are executed from inside of modelE directory tree):
常用Git命令（除了初始的"git clone ..."外，所有命令都从modelE目录树内执行）：

### 1. to check out the main branch of modelE
### 1. 检出modelE的主分支

(equivalent of "cvs checkout modelE")
（相当于"cvs checkout modelE"）

```bash
git clone username@simplex.giss.nasa.gov:/giss/gitrepo/modelE.git
```

where `username` is your username on simplex.
其中`username`是您在simplex上的用户名。

This will create a directory modelE with all model code in it.
这将创建一个包含所有模型代码的modelE目录。

It will also create a hidden directory modelE/.git with Git version control information in it (this among other things will include entire history of the code so that a lot of Git operations can be performed without access to the main server).
它还将创建一个隐藏目录modelE/.git，其中包含Git版本控制信息（其中包括代码的完整历史记录，因此可以在不访问主服务器的情况下执行许多Git操作）。

### 2. to switch to a branch
### 2. 切换到分支

(after you downloaded the code with "git clone...")
（在使用"git clone..."下载代码之后）

```bash
git checkout branch_name
```

this will switch the entire directory tree to the branch `branch_name`.
这将把整个目录树切换到分支`branch_name`。

To see the list of available branches type
要查看可用分支列表，请输入

```bash
git branch -a
```

If you want to switch to a remote branch (prefixed with "remotes") use a "short" `branch_name` for this branch (omitting "remotes/origin").
如果要切换到远程分支（以"remotes"为前缀），请为该分支使用"简短"的`branch_name`（省略"remotes/origin"）。

I.e. if you want to work with the branch `remotes/origin/AR5_branch` just do
即，如果要使用分支`remotes/origin/AR5_branch`，只需执行

```bash
git checkout AR5_branch
```

The first time you execute this command Git will say that it has created a local branch `AR5_branch` which is "tracking" a remote branch.
第一次执行此命令时，Git会表示它已创建一个本地分支`AR5_branch`，该分支正在"跟踪"远程分支。

Next time it will just switch the branch.
下次将直接切换分支。

### 3. to update the code in your working directory to the latest code in the repository on simplex
### 3. 将工作目录中的代码更新为simplex仓库中的最新代码

(equivalent of "cvs update"):
（相当于"cvs update"）：

```bash
git pull
```

This will "pull" the latest changes from the repository you cloned from (`simplex.giss.nasagov:/giss/gitrepo/modelE.git` in our case).
这将从您克隆的仓库（在我们这里是`simplex.giss.nasagov:/giss/gitrepo/modelE.git`）"拉取"最新更改。

Typically one should always use this simple command, unless one needs to do something fancy, like pulling from a private repository of other user.
通常应该始终使用这个简单命令，除非需要做一些特殊操作，比如从其他用户的私有仓库拉取。

In that case one can use more explicit command
在这种情况下，可以使用更明确的命令

```bash
git pull username@host_name:/path_to_modelE_dir branch_name
```

But be carefull when using this explicit command, for example, if you omit branch_name you will be pulling from the master branch, even if locally you are on a different branch.
但在使用这个明确命令时要小心，例如，如果省略branch_name，您将从主分支拉取，即使在本地您处于不同的分支。

### 4. to commit your code to the central repository on simplex
### 4. 将代码提交到simplex的中央仓库

you have to execute two commands:
您必须执行两个命令：

```bash
git commit -a
git push
```

The first one commits the code "locally", i.e. it stores this information in .git subdirectory.
第一个命令将代码"本地"提交，即将此信息存储在.git子目录中。

The second command "pushes" this information to the central repository on simplex.
第二个命令将此信息"推送"到simplex上的中央仓库。

Once the information is successfully pushed to simplex Git will send a message to the list with the commit info (similar to commit messages we are getting now from CVS).
一旦信息成功推送到simplex，Git将向列表发送包含提交信息的消息（类似于我们现在从CVS收到的提交消息）。

So if you don't receive such message you may want to check if your "commit" and "push" went through correctly.
因此，如果您没有收到这样的消息，您可能需要检查您的"commit"和"push"是否正确执行。

---

If you are working on more than one branch, then instead of "git push" it is more safe to execute
如果您在多个分支上工作，那么代替"git push"，执行以下命令更安全：

```bash
git push origin HEAD
```

This will push only your current local branch to the remote branch with the same name, while "git push" will push changes on all your branches which were committed but not pushed yet (and that may be not what you want).
这只会将您当前的本地分支推送到同名的远程分支，而"git push"将推送所有已提交但尚未推送的分支的更改（这可能不是您想要的）。

---

It is possible that when you try to "push" Git will complain about possible conflicts and refuse to push.
当您尝试"push"时，Git可能会抱怨可能的冲突并拒绝推送。

This situation is similar to trying to do "cvs commit" when your code in not up-to-date.
这种情况类似于在代码不是最新时尝试执行"cvs commit"。

In this case you have to do "git pull", resolve conflicts in your local directory and then repeat "git commit", "git push".
在这种情况下，您必须执行"git pull"，解决本地目录中的冲突，然后重复"git commit"、"git push"。

---

Sometimes "git pull" will request that you do local "git commit" first.
有时"git pull"会要求您先执行本地"git commit"。

This is to prevent your local code from being corrupted by conflicts with imported code.
这是为了防止您的本地代码因与导入代码的冲突而损坏。

In this case do "git commit -a" as advised by Git and repeat "pull".
在这种情况下，按照Git的建议执行"git commit -a"并重复"pull"。

Typically Git produces useful messages when executing the commands.
通常，Git在执行命令时会产生有用的消息。

If something doesn't work as expected read them and most likely you will know what to do.
如果某些操作没有按预期工作，请阅读这些消息，很可能您会知道该怎么做。

---

This small set of commands should get you started.
这小部分命令应该足以让您开始使用。

Eventually we will post a more complete list here.
最终我们将在此发布更完整的列表。

You can also read comprehensive Git manuals and tutorials at
您还可以在以下地址阅读全面的Git手册和教程：

```
http://git-scm.com/documentation
```

Also, typing
此外，输入

```bash
git command --help
```

will produce manual pages for the particular Git `command`.
将生成特定Git `command`的手册页。

If you have questions related to Git send me an email, or, better, post them to Modeling Guru forum:
如果您有与Git相关的问题，请给我发送电子邮件，或者更好的是，将它们发布到Modeling Guru论坛：

```
https://modelingguru.nasa.gov/thread/4743?tstart=0
```

so that others could profit from the answers.
这样其他人也可以从答案中受益。

You also may get your answers quicker since other people familiar with Git may read it.
您也可能更快地获得答案，因为其他熟悉Git的人可能会阅读它。

---

As with CVS we will have a Git repository viewer installed at
与CVS一样，我们将安装一个Git仓库查看器，位于：

```
http://simplex.giss.nasa.gov/cgi-bin/gitweb.cgi
```

---

## Working with branches

Git treats branches as local objects, which means that by default information about a new branch is not pushed to parent repository.
Git将分支视为本地对象，这意味着默认情况下不会将新分支的信息推送到父仓库。

Also, `git clone ...` doesn't add the branches from the remote repository to the local repository.
此外，`git clone ...`不会将远程仓库的分支添加到本地仓库。

To see all local branches one can execute
要查看所有本地分支，可以执行

```bash
git branch
```

Typically for a fresh clone this will show just a `master` branch.
通常，对于全新的克隆，这只会显示一个`master`分支。

One can though see the branches in a remote repository with
但可以使用以下命令查看远程仓库中的分支：

```bash
git branch -r
```

But if one wants to work with a remote branch one has to set up a local branch which is "tracking" a remote branch.
但是，如果要使用远程分支，必须设置一个"跟踪"远程分支的本地分支。

For example, to work with `origin/AR5_branch` branch one can create a local branch with
例如，要使用`origin/AR5_branch`分支，可以使用以下命令创建本地分支：

```bash
git checkout --track -b AR5_branch origin/AR5_branch
```

Starting with the Git version 1.7 this command can be shortened to
从Git版本1.7开始，此命令可以简化为：

```bash
git checkout AR5_branch
```

Once a local branch has been created one can always switch to it with
一旦创建了本地分支，就可以始终使用以下命令切换到它：

```bash
git checkout branch_name
```

The fact that `AR5_branch` we have just created is tracking a remote branch means that `git pull` will update your local branch from a remote repository and `git push` will send your local changes to a remote branch.
我们刚刚创建的`AR5_branch`正在跟踪远程分支这一事实意味着`git pull`将从远程仓库更新您的本地分支，而`git push`将把您的本地更改发送到远程分支。

One should mention that if for a local branch we have chosen a name which is different from the name of a remote branch then `git pull` will still update the local branch from the remote one, but `git push` will have no effect.
应该提到的是，如果为本地分支选择的名称与远程分支的名称不同，那么`git pull`仍将从远程分支更新本地分支，但`git push`将不会产生任何效果。

One can use this functionality to create ones own branch which one wants to periodically update from a public remote branch.
可以使用此功能创建自己的分支，并希望定期从公共远程分支更新。

---

To create a simple local branch (which will start from the current checked out state) typically one does
要创建一个简单的本地分支（将从当前检出的状态开始），通常执行

```bash
git checkout -b branch_name
```

If one wants then to commit it to central repository (to make it available to other users) one can do it with
如果然后想将其提交到中央仓库（使其对其他用户可用），可以使用

```bash
git push origin branch_name
```

---

## Using Git as a CVS server

Git is capable of simulating the behavior of CVS server, which means that one can access central Git repository using "cvs" (instead of "git") on local machine.
Git能够模拟CVS服务器的行为，这意味着可以在本地计算机上使用"cvs"（而不是"git"）访问中央Git仓库。

The use of such method is not encouraged and should be avoided if at all possible, but there may be circumstances when one can't use "git" (you have no control over local machine and can't install Git, connection is too slow to download the entire repository, you use a regression script which was written for CVS and was not yet converted to Git etc.).
不鼓励使用这种方法，如果可能的话应避免使用，但在某些情况下可能无法使用"git"（您无法控制本地计算机且无法安装Git、连接太慢无法下载整个仓库、您使用的是为CVS编写的回归脚本且尚未转换为Git等）。

---

If you decide to use this method keep in mind that only limited set of CVS operation is supported (pretty much just simple "checkout", "update" and "commit").
如果您决定使用此方法，请记住只支持有限的CVS操作集（基本上只有简单的"checkout"、"update"和"commit"）。

The execution may be very slow (may have to wait for several minutes) since Git has to build a special database for it.
执行可能非常慢（可能需要等待几分钟），因为Git必须为其构建特殊的数据库。

Set the following environment variable:
设置以下环境变量：

```bash
export CVS_SERVER="git cvsserver"
```

then you can check out the main branch of the model with:
然后可以使用以下命令检出模型的主分支：

```bash
cvs -d username@simplex.giss.nasa.gov:/giss/gitrepo/modelE.git \
    checkout -d modelE master
```

To check out a particular branch "branch_name" do:
要检出特定分支"branch_name"，请执行：

```bash
cvs -d username@simplex.giss.nasa.gov:/giss/gitrepo/modelE.git \
    checkout -d branch_name branch_name
```

Keep in mind that "cvs status" will always show that you are on the main trunk even if you have checked out a branch.
请记住，"cvs status"将始终显示您在主干上，即使您检出了分支。

It is up to you to remember this info.
记住这个信息是您的责任。

Also, this "simulated" CVS repository has nothing to do with the original CVS repository we were using before the switch to Git.
此外，这个"模拟的"CVS仓库与我们在切换到Git之前使用的原始CVS仓库没有任何关系。

Don't try to use these commands on the modelE directory checked out from the old CVS repository - it will destroy your code.
不要尝试在从旧CVS仓库检出的modelE目录上使用这些命令——它会破坏您的代码。

This method should be treated just as a temporary hack.
此方法应仅被视为临时权宜之计。
