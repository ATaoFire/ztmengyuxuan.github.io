---
layout: post
title: Cocoapods系列:制作自己的pods(二)
date: 2016-05-10
categories: IOS

---

## 建立git仓库

### 1 在github上建立MakeCocoapods的仓库,如下图
 
 ![](http://7xqijx.com1.z0.glb.clouddn.com/MakeCocoapods.png)

### 2 把工程克隆到桌面上

    $ git ~/desktop
    $ git clone https://github.com/lhjzzu/MakeCocoapods

### 3 创建我们的工程demo放到MakeCocoapods文件夹中

 ![](http://7xqijx.com1.z0.glb.clouddn.com/cocoapodsDemo.png)
 
 我在demo工程中建立了一个`MakeCocoapods`类，创建了一个下载图片的方法，并且依赖了`SDWebImage`
 可以直接[fork](https://github.com/lhjzzu/MakeCocoapods)我的工程查看源代码 

### 4创建Classes文件夹

Classes文件夹与MakeCocoapods文件夹同级，并且把`MakeCocoapods.h`，`MakeCocoapods.m`文件放进去
 ![](http://7xqijx.com1.z0.glb.clouddn.com/cocoapodsclass.png)

### 5 打标签
    $ cd 进入工程文件
    $ git add .
    $ git commit -m '0.0.1'
    $ git push origin master
    $ git tag 0.0.1
    $ git push --tag

## trunk
  
### 注册trunk

    1 $ pod trunk register 1822657131@qq.com lhjzzu  --verbose'
        
     [!] Please verify the session by clicking the link in the verification email that has been sent to 1822657131@qq.com
     
     打开这个邮件直接打开邮件中的链接即可，如果链接打不开的话，直接复制到浏览器中打开
     
    2 $ pod trunk me 查看信息
     
       - Name:       lhjzzu
       - Email:    1822657131@qq.com
       - Since:    September 14th, 2015 01:09
       - Pods:
         - LHJTestes
         - LHJView
         - LHJButton
         - LHJLast
         - HJExtension
       - Sessions:
         - September 14th, 2015 01:09 -      March 8th, 20:46. IP:
         115.236.11.98
         - November 1st, 2015 23:43   -     March 23rd, 00:21. IP: 115.236.11.98
         Description: macbook air
         - May 9th, 00:44             - September 14th, 00:45. IP: 60.191.70.18
         - May 9th, 01:09             - September 14th, 01:15. IP: 60.191.70.18 
         Description: register trunk

    Pods就是你拥有的库，我的这些库都没有实际的内容
    
## .podspec文件   

### 创建.podspec文件
 
    cd进入MakeCocoapods文件夹
    $ pod spec create MakeCocoapods
  
    Specification created at MakeCocoapods.podspec
    
    
### 打开并分析.podspec文件


    #
    #  Be sure to run `pod spec lint MakeCocoapods.podspec' to ensure this is a
    #  valid spec and to remove all comments including this before submitting the spec.
    #
    #  To learn more about Podspec attributes see http://docs.cocoapods.org/specification.html
    #  To see working Podspecs in the CocoaPods repo see https://github.com/CocoaPods/Specs/
    #
    #  一定要运行 'pod spec lint xx.podspec'来确保.podspec文件是有效的。
    # 并且最后在提交.podspec之前要移除所有注释.
    #  可以了解更过关于Podspec，通过http://docs.cocoapods.org/specification.html
    #  see https://github.com/CocoaPods/Specs/

    Pod::Spec.new do |s|

      # ―――  Spec Metadata  ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――― #
      #
      #  These will help people to find your library, and whilst it
      #  can feel like a chore to fill in it's definitely to your advantage. The
      #  summary should be tweet-length, and the description more in depth.
      #
      
      # ―――  Spec 元数据  ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――― #
      #
      # 这些将帮助人们找到你的库，同时在成为你的优势之前可能感觉是麻烦的。(原谅我渣一样的翻译)
      # 概要的长度限制与推特的一样（140），并且这个描述更加深入
      # s.summary最好不要与s.description一样，会报警告(多写两字不会死)

      s.name         = "MakeCocoapods"
      s.version      = "0.0.1"
      s.summary      = "A short description of MakeCocoapods."

      # This description is used to generate tags and improve search results.
      #   * Think: What does it do? Why did you write it? What is the focus?
      #   * Try to keep it short, snappy and to the point.
      #   * Write the description between the DESC delimiters below.
      #   * Finally, don't worry about the indent, CocoaPods strips it!
      
      # 这个描述用来生成标签和改善搜索结果
      #   思考:它做了什么？你为什么要写它？重点是什么？
      #   尽力保持它简短，精炼
      #   在DESC之间写这个描述
      #   最后不要担心缩进。cocoapods将做它。
      
      s.description  = <<-DESC
                   DESC
                   
      # 主页地址，直接填写我们的仓库地址即可
      s.homepage     = "http://EXAMPLE/MakeCocoapods"
      #屏幕截图(不需要关心，直接删除即可)
      # s.screenshots  = "www.example.com/screenshots_1.gif", "www.example.com/screenshots_2.gif"

      # ―――  Spec License  ――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― #
      #
      #  Licensing your code is important. See http://choosealicense.com for more info.
      #  CocoaPods will detect a license file if there is a named LICENSE*
      #  Popular ones are 'MIT', 'BSD' and 'Apache License, Version 2.0'.
      #
      # ―――  Spec 授权  ――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― #
      #
      #  授权你的代码是很重要的。查看http://choosealicense.com得到更多的信息
      #  CocoaPods 如果这里有一个命名为LICENSE*的文件，那么Cocoapods将检测这个授权文件
      #  主要的授权为:'MIT', 'BSD' and 'Apache License, Version 2.0'
      #

      s.license      = "MIT (example)"
      # s.license      = { :type => "MIT", :file => "FILE_LICENSE" }

      # ――― Author Metadata  ――――――――――――――――――――――――――――――――――――――――――――――――――――――――― #
      #
      #  Specify the authors of the library, with email addresses. Email addresses
      #  of the authors are extracted from the SCM log. E.g. $ git log. CocoaPods also
      #  accepts just a name if you'd rather not provide an email address.
      #
      #  Specify a social_media_url where others can refer to, for example a twitter
      #  profile URL.
      #
      
      # ――― 作者 元数据  ――――――――――――――――――――――――――――――――――――――――――――――――――――――――― #
      #
      #  指定这个库的作者和email地址。
      #  作者的email地址也可以通过 $ git log来提取。
      #  如果你不愿意提供邮箱，CocoaPods也接受仅仅一个名字
      #  指定一个别人可以访问的社交账号，例如推特
      # s.social_media_url这一项最好不要指定了，因为推特国内无法访问，验证.podsec时，不通过。

      #填写用户名以及自己的github邮箱
      s.author             = { "lhjzzu" => "1822657131@qq.com" }
      # Or just: s.author    = "lhjzzu"
      # s.authors            = { "lhjzzu" => "1822657131@qq.com" }
      # s.social_media_url   = "http://twitter.com/lhjzzu"

      # ――― Platform Specifics ――――――――――――――――――――――――――――――――――――――――――――――――――――――― #
      #
      #  If this Pod runs only on iOS or OS X, then specify the platform and
      #  the deployment target. You can optionally include the target after the platform.
      #
      
      # ――― 平台的指定 ――――――――――――――――――――――――――――――――――――――――――――――――――――――― #
      #
      #  如果你的Pod仅仅运行在iOS或者OS X上，那么要指定platform以及deployment target。
      # 一般而言，我们直选择
      # s.platform = :ios和s.ios.deployment_target = "5.0"
      # s.platform     = :ios, "5.0"与上面两句话相等
      
      
      # s.platform     = :ios
       s.platform     = :ios, "5.0"
     

      #  When using multiple platforms
      # s.ios.deployment_target = "5.0"
      # s.osx.deployment_target = "10.7"
      # s.watchos.deployment_target = "2.0"
      # s.tvos.deployment_target = "9.0"


      # ――― Source Location ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――― #
      #
      #  Specify the location from where the source should be retrieved.
      #  Supports git, hg, bzr, svn and HTTP.
      #
      
      # ――― 资源的位置 ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――― #
      #
      #  指定将被拉取的资源的位置
      #  支持 git, hg, bzr, svn and HTTP.
      # http://EXAMPLE/MakeCocoapods.git 就是我们仓库的地址(一定不要忘了.git)
      # tag => "0.0.1" 就是我们打的标签
      

      s.source       = { :git => "http://EXAMPLE/MakeCocoapods.git", :tag => "0.0.1" }

      # ――― Source Code ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― #
      #
      #  CocoaPods is smart about how it includes source code. For source files
      #  giving a folder will include any swift, h, m, mm, c & cpp files.
      #  For header files it will include any header in the folder.
      #  Not including the public_header_files will make all headers public.
      #
      
      # ――― 源码 ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― #
      #
      #  对于怎样去包含源码，cocoapods是很聪明的。
      #  s.source_files将包含所有的源文件（swift, h, m, mm, c & cpp）
      #  s.exclude_files要排除的文件（一般直接删除即可）
      #  s.public_header_files 指定我们想公开的头文件
      #  如果不含有s.public_header_files，那么我们的.h文件是默认全部公开的。
      
      s.source_files  = "Classes", "Classes/**/*.{h,m}"
      s.exclude_files = "Classes/Exclude"

      # s.public_header_files = "Classes/**/*.h"


      # ――― Resources ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― #
      #
      #  A list of resources included with the Pod. These are copied into the
      #  target bundle with a build phase script. Anything else will be cleaned.
      #  You can preserve files from being cleaned, please don't preserve
      #  non-essential files like tests, examples and documentation.
      #
   
      # ――― 资源 ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― #
      #
      #  这个Pod包含的一系列的资源。在编译脚本的阶段，它们被复制到这个目标bundle中。
      #  其它的任何资源将被清理。你可以保护文件免于被清理，但是请不要保存不必要的文件
      #  例如tests，examples，documentation

      # s.resource  = "icon.png"
      # s.resources = "Resources/*.png"
      # s.preserve_paths = "FilesToSave", "MoreFilesToSave"

      # ――― Project Linking ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――― #
      #
      #  Link your library with frameworks, or libraries. Libraries do not include
      #  the lib prefix of their name.
      #
      
      # ――― 项目 链接 ―――――――――――――――――――――――――――――――――――――――――――――――――――――――――― #
      #
      #  链接你的Framework和library（系统的Framework，library）. 
      # librarys的指定不包含lib的前缀，例如libxml2.tbd
      

      # s.framework  = "SomeFramework"
      # s.frameworks = "SomeFramework", "AnotherFramework"

      # s.library   = "iconv"
      # s.libraries = "iconv", "xml2"

 
      # ――― Project Settings ――――――――――――――――――――――――――――――――――――――――――――――――――――――――― #
      #
      #  If your library depends on compiler flags you can set them in the xcconfig hash
      #  where they will only apply to your library. If you depend on other Podspecs
      #  you can include multiple dependencies to ensure it works.

      # ――― 项目 设置 ――――――――――――――――――――――――――――――――――――――――――――――――――――――――― #
      # 如果你的library依赖一个compiler flags。你能设置他们在xcconfig，它们将应用于你的lib中。
      #  如果你的pods依赖其他的Podspecs，你能够包含多个依赖来确保它工作。
      # s.requires_arc指定是否为ARC
      # s.xcconfig做一些配置
      # s.dependency指定依赖
      
      # s.requires_arc = true
      # s.xcconfig = { "HEADER_SEARCH_PATHS" => "$(SDKROOT)/usr/include/libxml2" }
      # s.dependency "JSONKit", "~> 1.4"

    end


### 最终的.podspec文件 


    Pod::Spec.new do |s|

      s.name         = "MakeCocoapods"
      s.version      = "0.0.1"
      s.summary      = "this is demo of  Cocoapods."
      s.description  = <<-DESC
                   this is a demo of  Cocoapods.
                   DESC
      s.homepage     = "https://github.com/lhjzzu/MakeCocoapods"
      s.license      = "MIT"
      s.author             = { "lhjzzu" => "1822657131@qq.com" }
      s.platform     = :ios
      s.ios.deployment_target = "5.0"
      s.source       = { :git => "https://github.com/lhjzzu/MakeCocoapods.git", :tag => "0.0.1" }
      s.source_files  = "Classes", "Classes/*.{h,m}"
      #s.exclude_files = "Classes/Exclude"
      #s.public_header_files = "Classes/*.h"
      s.requires_arc = true
      s.dependency "SDWebImage"
    end


### 验证.podspec文件
  
    $ pod spec lint MakeCocoapods.podspec --verbose
     如果出现下面的信息，表示验证通过
     MakeCocoapods.podspec passed validation.
     
     --vebose:打印细节，可以把执行过程中具体的信息打印出来
     
验证时可能遇到的问题

* 如果`s.summary`与`s.description`完全一样的话，验证时会出现警告

        -> MakeCocoapods (0.0.1)
             - WARN  | description: The description is equal to the summary.

          Analyzed 1 podspec.

          [!] The spec did not pass validation, due to 1 warning (but you can use `--allow-warnings`     to ignore it).
    
          它提示我们可能通过加--allow-warnings去忽略警告，虽然我们可以通过忽略警告来使podspec文件通过验证，但是我们不应该这么做，因为这会导致我们在发布pod给trunk服务器时，验证失败。

* 指定我们的platform和deployment_target

        s.platform = :ios, "5.0"相当于s.platform= :ios
        和s.ios. s.ios.deployment_target = "5.0"
  
* `s.version`要与`tag`保持一致否则验证时会报警告

        - WARN  | source: The version should be included in the Git tag.
* `tag`一定要是已经提交过的`tag`，例如我们现在打了`tag`为`0.01`的标签，那么如果把tag改为0.02,那么验证时会告诉我们找不到`tag`为`0.0.2`的分支
   
         - ERROR | [iOS] unknown: Encountered an unknown error ([!] /usr/local/bin/git clone https://github.com/lhjzzu/MakeCocoapods.git /var/folders/fk/l6j6lbss3jn84g7xvsb2l4mw0000gn/T/d20160510-20861-1tcybky --single-branch --depth 1 --branch 0.0.2

         Cloning into '/var/folders/fk/l6j6lbss3jn84g7xvsb2l4mw0000gn/T/d20160510-20861-1tcybky'...
         warning: Could not find remote branch 0.0.2 to clone.
         fatal: Remote branch 0.0.2 not found in upstream origin
         
* `s.license`要把`(example)`删除掉，否则验证时，会报下面的错误(在以前时并没有影响,现在要删掉)
  
        -> MakeCocoapods (0.0.1)
            - ERROR | license: Sample license type.

        Analyzed 1 podspec.

        [!] The spec did not pass validation, due to 1 error 
 

## 发布到trunk上
 
### 把我们的.podspec文件发布到trunk服务器
 
    $ pod trunk push MakeCocoapods.podspec --verbose 
  
     如果有下面的信息显示，表明push成功
      - Data URL: https://raw.githubusercontent.com/CocoaPods/Specs/335c1455963cf88460632a956bd2f5ffdc5bc155/Specs/LHJButton/0.0.1/MakeCocoapods.podspec.json
      - Log messages:
    - May 9th, 23:29: Push for `MakeCocoapods 0.0.1' initiated.
    - May 9th, 23:29: Push for `MakeCocoapods 0.0.1' has been pushed (3.41790716 s).
  
  
  注意:我们不能重复发布我们的pods，会报下面的错误
  
        Unable to accept duplicate entry for: MakeCocoapods (0.0.1)
        
  这个时候直接搜索我们的pod
  
   `$ pod search MakeCocoapods`
  
    -> MakeCocoapods (0.0.1)
    this is demo of  Cocoapods.
    pod 'MakeCocoapods', '~> 0.0.1'
    - Homepage: https://github.com/lhjzzu/MakeCocoapods
    - Source:   https://github.com/lhjzzu/MakeCocoapods.git
    - Versions: 0.0.1 [master repo]
    
    表明我们的pod已经建立成功


 使用初始化`$Pod setup`或者更新`$ Pod repo  update`我们的仓库
  
  

### 使用我们的pod 

  再建立一个测试工程在Podfile中，输入`pod 'MakeCocoapods', '~ 0.0.1'`，然后安装我们的pod，就可以正常使用我们的pod了。

## FAQ  

### 执行`$ pod spec lint MakeCocoapods.podspec --verbose`，这条命令到底干了什么，它仅仅是验证我们的.podspec本身吗？它是如何保证我们工程的有效性了？
    
        我们可以大致分析一下终端中执行的大致过程
            
        MakeCocoapods (0.0.1) - Analyzing on iOS 5.0 platform.
          Preparing
        Analyzing dependencies
        Fetching external sources
        -> Fetching podspec for `MakeCocoapods` from `/Users/chiyou/Desktop/MakeCocoapods/        MakeCocoapods.podspec`
        Resolving dependencies of 

        Comparing resolved specification to the sandbox manifest
          A MakeCocoapods
          A SDWebImage

        Downloading dependencies
        -> Installing MakeCocoapods (0.0.1)
        -> Installing SDWebImage (3.7.6)
        
        Generating Pods project
        Building with xcodebuild. 
        ** BUILD SUCCEEDED **
        
        Analyzed 1 podspec.
        MakeCocoapods.podspec passed validation.
        
       
* 在iOS 5.0上解析`MakeCocoapods`，进行准备工作去获取外部资源--`MakeCocoapods.podspec`
* 解决依赖，添加`MakeCocoapods`，和`SDWebImage`(`MakeCocoapods`库实际上并没有，
    相当于根据我们`.podspec`中在配置的文件的配置暂时生成一个库) ，并安装。
* 然后生成`Pods`工程文件
* 利用`xcodebuild`来编译我们的Pods工程,出现`**BUILD SUCCEEDED**`代表编译成功，编译的过程可以具体参考[这篇文章](http://www.lhjzzu.com/2016/04/29/ios-xcodebuild/)
* 然后验证 `MakeCocoapods.podspec`的其他选项，看`.podspec`是否通过验证
 
 
### 对`$ pod trunk push MakeCocoapods.podspec --verbose`进行分析？

        Updating spec repo `master`
        CocoaPods 1.0.0.rc.2 is available.
        To update use: `gem install cocoapods --pre`
        [!] This is a test version we'd love you to try.


         MakeCocoapods (0.0.1) - Analyzing on iOS 5.0 platform.
          Preparing
        Analyzing dependencies
        Fetching external sources
        -> Fetching podspec for `MakeCocoapods` from `/Users/chiyou/Desktop/MakeCocoapods/        MakeCocoapods.podspec`
        Resolving dependencies of 

        Comparing resolved specification to the sandbox manifest
          A MakeCocoapods
          A SDWebImage

        Downloading dependencies
        -> Installing MakeCocoapods (0.0.1)
        -> Installing SDWebImage (3.7.6)
        
        Generating Pods project
        Building with xcodebuild. 
        ** BUILD SUCCEEDED **
        
        Analyzed 1 podspec.
        MakeCocoapods.podspec passed validation.
        
        
        Updating spec repo `master`

        CocoaPods 1.0.0.rc.2 is available.
        To update use: `gem install cocoapods --pre`
        [!] This is a test version we'd love you to try.
        
        - Data URL: https://raw.githubusercontent.com/CocoaPods/Specs/335c1455963cf88460632a956bd2f5ffdc5bc155/Specs/LHJButton/0.0.1/MakeCocoapods.podspec.json
         - Log messages:
         - May 9th, 23:29: Push for `MakeCocoapods 0.0.1' initiated.
         - May 9th, 23:29: Push for `MakeCocoapods 0.0.1' has been pushed (3.41790716 s).
  
  
* 首先是更新我们的库，然后告诉我们有了一个`1.0.0.rc.2`版本的`Cocoapods`(测试版)
* 然后就是验证我们`.podspec`文件，之所以在上面说不要在验证`.podspec`文件时使用`--allow-warnings`就是因为，这里会再次进行验证。
* 再次更新我们的pod，这时我们的`.podspec`已经push成功了，接下来打印出了相应的信息。
        

### 什么情况下表明已经通过创建成功了呢？ 

* 当你能用`$ pod search xxx` 搜索到自己的库的时候，那么已经创建成功了，别人搜索不到是因为他们的库没有更新，执行`$ pod setup`操作即可

### 为什么在其他人电脑上有的人搜得到，有的人搜不到呢？
   
* 因为有的人在`$ pod install`或者`$ pod update`时常常会这么写：`$ pod update --no-repo-update`，加了后面那一串就表示“只更新我指定的库到我的电脑，而不是cocoaPods成千上万个库一起更新”。
* 如果你单单使用`$ pod install`或者`$ pod update`，那应该就可以搜得到你的库。
 
### 为什么随便写的代码也能通过审核，审核的机制是什么？

* 我们从问题1以及问题2可以看出，`Cocoapods`仅仅上保证我们工程编译能够成功，仅仅是验证`.podspec`文件的有效性
* 总结来说它校验的是格式，而不是检验我们代码的质量。


## 参考
* [CocoaPods详解之----制作篇](http://blog.csdn.net/wzzvictory/article/details/20067595)
* [手把手教你发布代码到CocoaPods(Trunk方式)](http://www.cnblogs.com/wengzilin/p/4742530.html)
* [Podspec Syntax Reference](https://guides.cocoapods.org/syntax/podspec.html)


     
  
  
 
  
  