---
layout: post
title: ios打包--脚本自动化打包并上传到蒲公英(三)
date: 2016-05-03
categories: IOS


---

## 命令行打包

### 打包可以简单分为两个阶段

* build生成.app文件
* 由.app文件生成.ipa文件

### 相关命令
通过[ios打包--xcodebuild以及xcrun](http://www.lhjzzu.com/2016/04/29/ios-xcodebuild/)这篇文章的学习，我们可以知道这样两条关键性的命令

第一条命令
如果没有.xcworkspace文件

* `xdebuild -project Test.xcodeproj -target DV -configuration Release -sdk iphoneos9.3 CODE_SIGN_IDENTITY="iPhone Distribution: Hangzhou Riguan Apparel Co.,ltd (V9LX9F46VG)" PROVISIONING_PROFILE="a97416b6-a868-44c7-8bd5-5847954305bb"`

如果有.xcworkspace文件

* `xdebuild -workspace DV.xcworkspace -scheme DV -configuration Release -sdk iphoneos9.3 CODE_SIGN_IDENTITY="iPhone Distribution: Hangzhou Riguan Apparel Co.,ltd (V9LX9F46VG)" PROVISIONING_PROFILE="a97416b6-a868-44c7-8bd5-5847954305bb"`

第二条命令

* `xcrun -sdk iphoneos -v PackageApplication ./build/Release-iphoneos/Test.app -o ~/Desktop/ipa/Test.ipa`

意:

1 第一条命令是生成.app文件，第二条命令是由.app文件生成.ipa文件

2 要将其中的签名信息，以及路径信息等换成自己的信息


## 脚本打包 

### 自动化脚本
* 你可以通过[github](https://github.com/carya/Util)来下载该脚本
* 该脚本来源于[@CaryaLiu](http://liumh.com)，非常感谢他的分享。

### 脚本的使用
* 首先脚本的使用[@CaryaLiu](http://liumh.com)已经在[github](https://github.com/carya/Util)的`README.md`中说的很清楚了，各位可以自行参考。
* 为防止有些同学不会用，我说一下它的用法（我自己就是例子，因为不懂python，所以摸索了好一会儿）。
* 脚本下载下来后要把下面这些信息修改为自己的
      
        CODE_SIGN_IDENTITY = "iPhone Distribution: Hangzhou Riguan Apparel Co.,ltd (V9LX9F46VG)"
        PROVISIONING_PROFILE = "a97416b6-a868-44c7-8bd5-5847954305bb"
        CONFIGURATION = "release"

        PGYER_UPLOAD_URL = "http://www.pgyer.com/apiv1/app/upload"
        DOWNLOAD_BASE_URL = "http://www.pgyer.com"
        USER_KEY = "b836bbd8c0cb96463a6ef0895061c3c9"
        API_KEY = "0607f8bf8233b5665255acf59f16cdf6"
        
        说明: CODE_SIGN_IDENTITY以及PROVISIONING_PROFILE是证书和描述性文件的信息，CONFIGURATION代表打包为线上，PGYER_UPLOAD_URL蒲公英上传的接口，DOWNLOAD_BASE_URL为蒲公英下载的接口，USER_KEY以及API_KEY为蒲公英生成的对用的key，可以通过登录蒲公英->应用管理->选择对应的应用->API 即可看到USER_KEY和API_KEY信息
        
* 把修改后的脚本放到工程文件夹中（以Test工程为例）


        1 cd到Test文件夹
        2 $ python autobuild.py -w Test.xcworkspace -s Test -o ~/desktop/ipa/Test.ipa 即可
        3 如果工程中没有使用cocoapods，$ python autobuild.py -p Test.xcodeproj -t Test -o ~/desktop/ipa/Test.ipa 即可


 

## 参考
* [iOS自动打包并发布脚本](http://liumh.com/2015/11/25/ios-auto-archive-ipa/)
* [敲一下enter键，完成iOS的打包工作](http://ios.jobbole.com/84677/)
 



     
  
  
 
  
  