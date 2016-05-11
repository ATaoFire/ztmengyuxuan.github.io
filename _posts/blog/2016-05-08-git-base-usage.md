---
layout: post
title: git基本用法
date: 2016-05-08
categories: Git

---


## git简介

### git作用

git是进行版本控制的工具。

### 利用github建立一个git仓库

#### 方法1:直接克隆远程仓库（建议）

1 首先注册一个github账号

2 新建一个仓库，如下图，并且点击`creating repository`

![](http://7xqijx.com1.z0.glb.clouddn.com/git%E4%BB%93%E5%BA%93.png)

3 克隆这个仓库到桌面

* cd到桌面
   
        $ cd ~/desktop
   
* 克隆仓库
          
        $ git clone https://github.com/lhjzzu/learngit
        
        Cloning into 'learngit'...        
        remote: Counting objects: 11, done.
        remote: Compressing objects: 100% (7/7), done.
        remote: Total 11 (delta 2), reused 7 (delta 1), pack-reused 0
        Unpacking objects: 100% (11/11), done.
        Checking connectivity... done
        
    
* 添加文件
        
        $ cd ./learngit
        $ touch test.txt (创建test.txt文件)
        $ open test.txt (输入这是一个测试)
        $ git add . (添加所有文件到版本库的暂存区)
        $ git commit -m 'first commit' （把暂存区的所有内容提交到当前分支）
        
* 把本地的分支的修改推送到远端
     
        $ git push
     
        Counting objects: 3, done.
        Delta compression using up to 8 threads.
        Compressing objects: 100% (2/2), done.
        Writing objects: 100% (3/3), 283 bytes | 0 bytes/s, done.
        Total 3 (delta 1), reused 0 (delta 0)
        To https://github.com/lhjzzu/learngit
           ffc4dff..c422d8d  master -> master
     
#### 方法2:建立本地仓库，并与远程仓库关联

1 首先注册一个github账号

2 新建一个仓库，如下图，并且点击`creating repository`

![](http://7xqijx.com1.z0.glb.clouddn.com/git%E4%BB%93%E5%BA%93.png)

3 在本地建立git仓库，并与远端仓库关联到一起

* 建立learngit文件夹并进入文件夹
   
        $ cd ~/desktop
        $ mkdir learngit
        $ cd ./learngit
    
* 初始化仓库
    
        $ git init 
        
        Initialized empty Git repository in /Users/chiyou/Desktop/learngit/.git/
   
* 添加文件
   
        $ touch test.txt (创建test.txt文件)
        $ open test.txt (输入这是一个测试)
        $ git add . (添加所有文件到版本库的暂存区)
        $ git commit -m 'first commit' （把暂存区的所有内容提交到当前分支）
        
        
* 与远程仓库建立连接
    
        $ git remote add origin https://github.com/lhjzzu/learngit
     
     
* 由于远程仓库中的信息与本地并不一直，先进行拉取  
   
        $ git pull
     
        See git-pull(1) for details.
          git pull <remote> <branch>
        If you wish to set tracking information for this branch you can do so with:
          git branch --set-upstream-to=origin/<branch> master
          
* 由上面的信息可知，我们需要设置本地仓库与远程仓库的拉取的关联(pull)
     
        $ git branch --set-upstream-to=origin/master master 
   
           Branch master set up to track remote branch master from origin.
        
        $ git pull
     
        Merge made by the 'recursive' strategy.
        .gitignore | 53 +++++++++++++++++++++++++++++++++++++++++++++++++++++
        LICENSE    | 21 +++++++++++++++++++++
        README.md  |  2 ++
        3 files changed, 76 insertions(+)
        create mode 100644 .gitignore
        create mode 100644 LICENSE
        create mode 100644 README.md
      
* 把本地的分支的修改推送到远端
   
        $ git push
     
        Counting objects: 5, done.
        Delta compression using up to 8 threads.
        Compressing objects: 100% (3/3), done.
        Writing objects: 100% (5/5), 512 bytes | 0 bytes/s, done.
        Total 5 (delta 1), reused 0 (delta 0)
        To https://github.com/lhjzzu/learngit
           fe6b1e2..10c8b9c  master -> master
        
   
   
## learngit结构分析

工作区:learngit文件夹就是工作区

版本库:工作区中的隐藏目录,.git就是版本库

* 查看.git目录的相关信息
  
        $ cd ~/desktop/learngit
        $ cd .git
        $ ls -F1
        
        COMMIT_EDITMSG
        HEAD
        branches/
        config
        description
        hooks/
        index
        info/
        logs/
        objects/
        packed-refs
        refs/
  
* 关于.git目录下的各项的作用请参考[这篇文章](http://www.zhihu.com/question/38983686?sort=created)

暂存区：版本库中的stage（或者index）就是暂存区，还有Git为我们自动创建的第一个分支master，以及指向master的一个指针叫HEAD。


## git常用命令

### 添加内容并推送
  
这个内容在建立git仓库的时候已经演示过了,这里主要列举一下相关命令

      小结:
      git init 初始化一个git仓库
      git add . 把文件添加进去，实际上就是把文件修改添加到暂存区
      git commit -m 'xx' 提交更改，实际上就是把暂存区的所有内容提交到当前分支。
      git status 随时查看工作区的状态
      git diff 查看修改的内容    

### 撤销修改
     
#### 直接撤销工作区的修改  

     1 在test.txt中添加`git基本使用`
     2 $ git checkout -- test.txt 
     3 此时查看test.txt文件，我们刚才添加的内容已经撤销
   
当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令`git checkout -- file`。
     
#### 当添加到暂存区中后，撤销修改

      1 在test.txt中添加`git基本使用`
      2 $ git add .
      3 $ git reset HEAD test.txt
         
         Unstaged changes after reset:
         M	test.txt  
      4  git checkout -- test.txt
      5 此时查看test.txt文件，我们刚才添加的内容已经撤销

当你不但改乱了工作区某个文件的内容，还执行 `git add . `添加到了暂存区时，想丢弃修改，分两步，第一步用命令`git reset HEAD file`，再执行`git checkout -- file`。
 

#### 当已经commit到本地分支后，撤销修改

 最好直接版本回退


### 分支

#### 1 查看分支

`$ git branch`
 
    * master
    
 *指向当前分支
 
 `$ git branch -a` 会将所有分支以及远程仓库都显示出来
 
     * master
      remotes/origin/HEAD -> origin/master
      remotes/origin/master
 
#### 2 创建分支

 `$ git branch dev`
 
#### 3 再次查看分支

`$ git branch`

    dev
    * master
    
此时指向master分支

#### 4 切换分支

`$ git checkout dev`

    Switched to branch 'dev'
    
#### 5 再次查看分支

`$ git branch`

    * dev
     master
     
此时指向dev分支

#### 6 修改dev分支并合并到master上

给test.txt添加`合并分支`的内容

    $ git add .
    # git commit -m 'dev'
    $ git checkout master
    $ git merge dev
    
     Updating c422d8d..0697ece
     Fast-forward
     test.txt | 3 ++-
     1 file changed, 2 insertions(+), 1 deletion(-)

* 要合并分支，首先切换分支到最终合并到的分支(master),此时master中的test.txt并没有`合并分支`
* 执行完`git merge dev`,此时可以看到test.txt中已经有`合并分支`的内容了。
* 注意到上面的Fast-forward信息，Git告诉我们，这次合并是“快进模式”，也就是直接把master指向dev的当前提交，所以合并速度非常快。

####  7 删除分支

* 删除一个已经合并过的分支（无论修改过与否）

   `$ git branch -d dev`
        
    Deleted branch dev (was 0697ece).


* 删除一个未合并过的分支,创建一个test分支(修改,并且commit过的)

 `$ git branch -d dev`
  
    error: The branch 'test' is not fully merged.
    If you are sure you want to delete it, run 'git branch -D test'.

 `$ git branch -D dev`
 
     Deleted branch test (was 51b2ab3).

* 要删除某个分支，当前分支必须是其他分支。
* 最好不要删除主分支。
* 如果确定要删除某分支，直接使用`git branch -D xxx`即可。
* 最好还是使用`git branch -d xxx`,以防删除未合并的分支。
     


#### 8 冲突的解决

若master分支和feature1分支各自都分别有新的提交，变成了这样
![](http://www.liaoxuefeng.com/files/attachments/001384909115478645b93e2b5ae4dc78da049a0d1704a41000/0)

这种情况下，Git无法执行“快速合并”，只能试图把各自的修改合并起来，但这种合并就可能会有冲突
Git用`<<<<<<<`，`=======`，`>>>>>>>`标记出不同分支的内容，我们修改如下后保存，再add，commit
现在，master分支和feature1分支变成了下图所示：

![](http://www.liaoxuefeng.com/files/attachments/00138490913052149c4b2cd9702422aa387ac024943921b000/0)


`git log --graph --pretty=oneline --abbrev-commit` 用于查看分支合并情况


     *   36c2f7a Merge branch 'dev'
     |\  
     | * 7179ae4 添加空3个空格
     * | d754fe1 test
     * | bace4d4 adf
     |/  
     * 0697ece 123
     * c422d8d first commit
     * ffc4dff adf
     *   10c8b9c Merge branch 'master' of https://github.com/lhjzzu/learngit
     |\  
     | * fe6b1e2 Initial commit
     * e0ae3d2 first commit

`git log --graph `可以看到分支合并图

#### 9 分支的内容的存储

`git stash`可以把当前分支未完成的工作储藏起来
当其他分支的工作完成之后，切换回这个分支
然后`git stash list `查看，git把stash的内容存在某个地方了
恢复有两个办法

法1. 用`git stash pop`（既恢复了工作区内容，也删除了stash的存储）

法2.`git stash apply`恢复，但是恢复后，stash内容并不删除，你需要用`git stash drop`来删除；
恢复指定的stash，用命令`git stash apply stash@{0}`


#### 分支小结:

    对分支以及合并分支的理解:(Fast-forward)
    1 HEAD指针原本指向master指针，创建dev分支后仅仅是增加了一个dev指针
    2 切换到dev分支，仅仅是HEAD指针（永远指向当前分支）指向了dev指针
    3 对dev分支的每一个commit，dev指针都向前移动一步，master指针不变
    4 所谓将master与dev分支合并，也仅仅是将master指针直接指向dev指针所在的位置。
    合并完成后，如果不需要dev分支，那么可以删除
    
    查看分支:git branch
    创建分支:git branch <name>
    切换分支:git checkout <name>
    创建+切换分支:git checkout -b <name>
    合并某分支到当前分支: git merge <name>
    删除分支:git branch -d <name>

 
### 远程仓库


#### 1 查看远程仓库信息

`$ git remote -v `

    origin	https://github.com/lhjzzu/learngit (fetch)
    origin	https://github.com/lhjzzu/learngit (push)
   
#### 2 推送到某个远程仓库
`$ git push origin <name>`或者 `$ git push`会自动推送到与本地分支名字一致的远程仓库
   
   
#### 3 某个新建的分支推送到远端(例如dev分支)
切换到dev分支
`$ git push `

    fatal: The current branch dev has no upstream branch.
    To push the current branch and set the remote as upstream, use

    git push --set-upstream origin dev

设置关联
  
`$ git push --set-upstream origin dev` 

    Delta compression using up to 8 threads.
    Compressing objects: 100% (4/4), done.
    Writing objects: 100% (6/6), 551 bytes | 0 bytes/s, done.
    Total 6 (delta 2), reused 0 (delta 0)
    To https://github.com/lhjzzu/learngit
     * [new branch]      dev -> dev
    Branch dev set up to track remote branch dev from origin.
 
 下次直接`$ git push`即可  
 
 
#### 4 直接从某个远程仓库抓取

首先查看一下有多少远程仓库

`$ git branch -a`

    * dev
      master
      remotes/origin/HEAD -> origin/master
      remotes/origin/dev
      remotes/origin/master

先切换到master分支并将dev分支删除

`$ git checkout master`
`$ git branch -D dev`

创建dev分支，并从远程仓库dev拉取

`$ git checkout -b dev origin/dev `

此时你已经可以正常的提交和远程推送了，但是如果你的修改与小伙伴的修改冲突的话，那么推送失败。那么此时你需要先pull，把小伙伴的修改拉取下来

使用`$ git pull`进行拉取,但是拉取失败,因为没有指定本地dev分支与远程origin/dev分支的连接

`$ git branch --set-upstream  origin/dev dev`

此时在进行git pull成功，如果有冲突，手动解决冲突后再进行push即可


#### 5 删除远程仓库

首先先删除远程分支
`$ git branch -r -d origin/dev`

    Deleted remote-tracking branch origin/dev (was e484aab).


在将dev置为空
`$ git push origin :dev`

    To https://github.com/lhjzzu/learngit
    - [deleted]         dev
    
#### 小结:

- 查看远程库信息，使用`git remote -v`；

- 本地新建的分支如果不推送到远程，对其他人就是不可见的；

- 从本地推送分支，使用`git push origi name`，如果推送失败，先用`git pull`抓取远程的新提交；

- 在本地创建和远程分支对应的分支，使用`git checkout -b name origin/name`，本地和远程分支的名称最好一致；

- 建立本地分支和远程分支的关联，使用`git branch --set-upstream  origin/name name`；

- 从远程抓取分支，使用git pull，如果有冲突，要先处理冲突。

### 创建和操作标签

#### 创建标签

    git tag <tagname> 在当前分支下最新的commit打上标签
    git tag <tagname> <commit id> 指定的commit打上标签
    git tag 查看所有的标签
    git show <tagname> 显示指定标签的信息
    git tag -a <tagname> -m "msg"  -a指定标签名 -m指定说明文字
    git tag -s <tagname> -m "msg"  -s用私钥签名一个标签<PGP签名>不要求掌握
    注意:标签不是按时间排序，而是按字母排序的，创建的标签是放在本地的

#### 操作标签

    git tag -d <tagname> 删除标签，只是从本地删除标签
    git push origin —tags 推送所有标签到远程
    推送到远程之后，如果要删除标签，那么先删除本地的标签
    git tag -d <tagname>
    再删除远程的标签
    git push origin :refs/tags/<tagname>

#### 小结

- 命令git push origin <tagname>可以推送一个本地标签；
- 命令git push origin --tags可以推送全部未推送过的本地标签；
- 命令git tag -d <tagname>可以删除一个本地标签；
- 命令git push origin :refs/tags/<tagname>可以删除一个远程标签。

## 配置别名

    git config --global alias.st status
    git config --global alias.co checkout
    git config --global alias.ci commit
    git config --global alias.br branch
    git config --global alias.unstage 'reset HEAD'
    git config --global alias.last 'log -1'
    git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

## FAQ

### 1 如何查看所有的历史commit？

    1 git log --pretty=oneline 会将从当前版本及之前的一部分版本列举出来
    2 git reset --hard  xxx(最后一个版本号) ， 然后继续执行1， 直到找到所需的版本.
    
### 2 当我们想直接覆盖掉我们git远程分支中的版本的时候？

    git push origin 远程分支名 --force  
    
### 3 如何忽略 .xcuserstate ，/xxx.xcuserdatad/等中间文件


    1 git status 会将中间文件列出来
    2 vi .gitignore 打开忽略文件
    3 将列出来的中间文件名放到.gitignore中
    4 git rm -r —cached . （移除缓存以使.gitignore文件生效）
    5 git add .
    6 git commit -m "fiexed untracked files"
    7 git push 即可.
    
### 4 合并分支时.xcodeproj文件爆红打不开，以及info.plist文件打不开？

    1 回退到合并前的版本
    git reset --hard HEAD^ 或者 git reset —hard 版本号
     2 git 忽略.xcodeproj文件
    在.gitignore中加入
    *.xcodeproj/
    DerivedData/
    (解决了问题之后最好把这两个删了，再按下面的步骤提交一下,否则再切换分支的时候.xcodeproj会丢失)
    但是这样做后，.gitignore并没有起作用，是因为缓存的缘故
    .gitignore文件只是ignore没有被staged(cached)文件，对于已经被staged文件，加入ignore文件时一定要先从staged移除。
    git rm -r --cached .
    git add .
    git commit -m "fixed untracked files"
    如果没有加入
    文件，那么工程中很多文件会缺少文件的索引
    可以直接把所有的文件索引删除，然后再添加进来即可

## 参考
* [廖雪峰Git](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)
* [本地Git仓库和远程仓库的创建及关联](http://www.jianshu.com/p/dcbb8baa6e36)
* [.git文件夹下的每个文件都是做什么的？](http://www.zhihu.com/question/38983686?sort=created)


     
  
  
 
  
  