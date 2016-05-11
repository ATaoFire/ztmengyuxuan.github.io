---
layout: post
title: Cocoapods系列:安装与使用(一)
date: 2016-05-09
categories: IOS

---


## 什么是Cocoapods？

* `Cocoapods`是用来管理`xcode`项目依赖库的。
* 你的工程的依赖在一个名字是`Podfile`的文本文件中被指定.`CocoaPods`将解决不同库之间依赖的问题。获取源码并把这些库一起链接到一个`.xcworkspace`文件中去创建你的项目。
* `Cocoapods`最终的目标是创建一个更集中化的生态系统去提高第三方开源库的可发现性，可使用性。


## Cocopods安装

`Cocoapods`是用`ruby`来创建的，我们使用`OS X `默认的可用的`ruby`来安装`Cocoapods`.你也可以使用`ruby`的版本管理，来更改`ruby`版本进行安装，但是官方还是建议使用`OS X `默认的`ruby`来安装。

唯一的问题是:当我们使用默认的ruby来进行安装`gems`的时候，需要使用`sudo`。

1 `$ sudo gem install -n /usr/local/bin cocoapods`

2 由于某些原因，执行时会出现下面的错误提示：

    ERROR:  Could not find a valid gem 'cocoapods' (>= 0), here is why:
    Unable to download data from https://rubygems.org/ - Errno::EPIPE: Broken pipe - SSL_connect (https://rubygems.org/latest_specs.4.8.gz)

3 这是因为默认所需的下载路径 `https://rubygems.org` 在国内的访问会有问题，解决上面的问题，可以用淘宝的`RubyGems`镜像来代替官方版本，执行以下命令

    $ gem sources -l
    $ gem sources --remove https://rubygems.org/
    $ gem sources -a https://ruby.taobao.org/
    $ gem sources -l

4 接着再执行 `sudo gem install -n /usr/local/bin cocoapods`

5 安装`cocoapods`库

`$ pod setup` 

第一个执行会非常慢，可以到`/.cocoapods`文件夹下看安装进度



## 更新Cocoapods

只需再次执行`$sudo gem install -n /usr/local/bin cocoapods`即可

## Cocoapods使用

1. 建立一个工程`CocoapodsTest`
2. cd 进入这个工程文件夹
3. 输入`$ vi Pofile`建立并打开`Podfile`文件。点击i，进入输入模式，输入下列内容后，按`esc`,`shift+:`,`wq`保存并退出
      
        target 'CocoapodsTest' do
        pod 'AFNetworking', '~> 3.1.0'
        end

4. 执行`$ pod install --verbose --no-repo-update`即可
 
        Analyzing dependencies
        Inspecting targets to integrate
          Using `ARCHS` setting to build architectures of target `Pods`: (``)
          Using `ARCHS` setting to build architectures of target `Pods-CocoapodsTest`:
          (``)
        Resolving dependencies of `Podfile`
        Comparing resolved specification to the sandbox manifest
          A AFNetworking
        Downloading dependencies
        -> Installing AFNetworking (3.1.0)
        .......
5. 执行成功生成`.xworkspace`文件，`Podfile.lock`文件，`Pods`文件夹。以后，项目操作就在`.xworkspace`文件中。


可以使用`$ pod search AFNetworking`来查看`AFNetworking`的版本信息

    -> AFNetworking (3.1.0)
       A delightful iOS and OS X networking framework.
       pod 'AFNetworking', '~> 3.1.0'
       - Homepage: https://github.com/AFNetworking/AFNetworking
       - Source:   https://github.com/AFNetworking/AFNetworking.git
       - Versions: 3.1.0, 3.0.4, 3.0.3, 3.0.2, 3.0.1, 3.0.0, 3.0.0-beta.3,
       3.0.0-beta.2, 3.0.0-beta.1, 2.6.3, 2.6.2, 2.6.1, 2.6.0, 2.5.4, 2.5.3, 2.5.2,
       2.5.1, 2.5.0, 2.4.1, 2.4.0, 2.3.1, 2.3.0, 2.2.4, 2.2.3, 2.2.2, 2.2.1, 2.2.0,
       2.1.0, 2.0.3, 2.0.2, 2.0.1, 2.0.0, 2.0.0-RC3, 2.0.0-RC2, 2.0.0-RC1, 1.3.4,
       1.3.3, 1.3.2, 1.3.1, 1.3.0, 1.2.1, 1.2.0, 1.1.0, 1.0.1, 1.0, 1.0RC3, 1.0RC2,
       1.0RC1, 0.10.1, 0.10.0, 0.9.2, 0.9.1, 0.9.0, 0.7.0, 0.5.1 [master repo]
       - Subspecs:
         - AFNetworking/Serialization (3.1.0)
         - AFNetworking/Security (3.1.0)
         - AFNetworking/Reachability (3.1.0)
         - AFNetworking/NSURLSession (3.1.0)
         - AFNetworking/UIKit (3.1.0)




## Podfile和Podfile.lock

### 什么是Podfile？

`Podfile`是描述一个或多个`xcode`程的的目标依赖的一个说明书。这个文件必须被命名为`Podfile`。

### Podfile文件所在的位置

* 推荐把`Podfile`文件存在工程根目录下
* 如果把`Podfile`文件存在工程其他目录下，需要在`Podfile`中指定`xx.xcodeproj`文件的路径

        xcodeproj "/Users/chiyou/Desktop/CocoaPodsTest/CocoaPodsTest.xcodeproj" 
    
### 版本指定

* `pod 'AFNetworking'`              不显式指定依赖库版本，表示每次都获取最新版本  
* `pod 'AFNetworking', '2.0'`       只使用2.0版本  
* `pod 'AFNetworking', '> 2.0'`     使用高于2.0的版本  
* `pod 'AFNetworking', '>= 2.0'`    使用大于或等于2.0的版本  
* `pod 'AFNetworking', '< 2.0'`     使用小于2.0的版本  
* `pod 'AFNetworking', '<= 2.0'`    使用小于或等于2.0的版本  
* `pod 'AFNetworking', '~> 0.1.2'`  使用大于等于0.1.2但小于0.2的版本  
* `pod 'AFNetworking', '~>0.1'`     使用大于等于0.1但小于1.0的版本  
* `pod 'AFNetworking', '~>0'`       高于0的版本，写这个限制和什么都不写是一个效果，都表示使用最新版本


### Podfile与target

`Podfile`与一个`target`

    target 'target1' do
     pod 'AFNetworking'
     end
 
`Podfile`与多个`target`

     target 'target1' do
     pod 'AFNetworking'
     end
 
     target 'target2' do
     pod 'AFNetworking'
     end
     
`Podfile`默认的`target`为第一个`target`，我们可以这样写
     
     pod 'AFNetworking'


### Podfile.lock

- 在开始使用`CocoaPods`，执行完`pod install`之后，会生成一个`Podfile.lock`文件
- 该文件用于保存已经安装的Pods依赖库的版本
- 在`Podfile`文件中不指定库的版本(`pod 'AFNetworking', '= 2.6.3'`指定版本)，那么团队协作开发时，别人`check`下来的工程，如果有这个`Podfile.lock`文件，那么在执行`pod install `获取的库的版本与最开始用户获取的版本相同
- 如果缺少`Podfile.lock`文件,那么在执行`pod install` 就会获取最新的版本，会造成团队使用的库版本不一致，这是很严重的问题
- 这种情况下，如果团队想要使用最新版的`AFNetworking`，那么可以使用`pod update` 或者 `Podfile`中直接指定最新的版本号
- 综上所述，`Podfile.lock`一定要纳入版本管理中去


## pod install 和 pod update

### pod install 

`Podfile`版本写死的情况:

1 直接等于某个版本

    Pod 'AFNetworking', '2.6.3' 
 
2 相当于直接等于某个版本

因为2.6.x的版本中2.6.3就是最高版本了,我们写2.6.x获取的版本肯定是2.6.3

    Pod 'AFNetworking', '> 2.6.x' 
    Pod 'AFNetworking', '>= 2.6.x' 


- 如果版本写死，有没有`Podfile.lock`文件都没有影响，执行`Pod install`，不会更改库的版本
- 如果版本未写死，有`Podfile.lock`文件，执行`Pod install`，不会更改库的版本
- 如果版本未写死，没有`Podfile.lock`文件，且库版本未更新，执行`Pod install`，不会更改库的版本
- 如果版本未写死，没有`Podfile.lock`文件，且库版本更新，执行`Pod install`，**会更改库的版本**
- 如果用`pod install --verbose --no-repo-update` 意思是只安装，不更新`pods`库中的资源。如果经常执行`pod install --verbose --no-repo-update`会导致我们的库版本会低很多。一些新的库或者某些库的新的版本通过`pod search xxx` 会搜索不到
- 如果更改`Podfile`文件，且更改后应该安装的版本与原来的不一样，无论是否有`Podfile.lock`文件，执行`Pod install`，**会更改库的版本**。

### pod update

- 如果`Podfile`中指定的依赖库版本不是写死的（`pod 'AFNetworking'`），当对应的依赖库有了更新，无论有没有`Podfile.lock`文件都会去获取`Podfile`文件描述的允许获取到的最新依赖库版本。
- 如果`Podfile`中指定的依赖库版本是写死的（`pod 'AFNetworking', '2.3.1'`），那么执行`pod update`根本没有作用。

## FAQ

### 工程中Pods无效?

可能我们拉取别人的代码，或者下载网上的代码是会出现Pods失效报错的情况

由于工程中依旧存在`Podfile`和`Podfile.lock`文件,所以我们只需要进入工程文件然后执行`pod install --verbose --no-repo-update` 即可

但是有时它并不起作用，依旧没有把对应的库导入进来，这个时候我们最终极的解决方案是删除`Pods`文件夹，删除`.xcworkspec`文件，然后再次执行`pod install --verbose --no-repo-update`即可


## 参考
* [Cocoapods Guides](https://guides.cocoapods.org)
* [CocoaPods详解之----进阶篇](http://blog.csdn.net/wzzvictory/article/details/19178709)
* [Podspec Syntax Reference](http://blog.csdn.net/wzzvictory/article/details/19178709)
     
  
  
 
  
  