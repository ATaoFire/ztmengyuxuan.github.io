---
layout: post
title: ios打包--xcodebuild以及xcrun(二)
date: 2016-04-29
categories: IOS


---


## xcodebuild 

### 简介

 xcodebuild 用于编译xcode中的projects和workspaces
 
### 文档
 
 1 在终端中输入
 
 `$ man xcodebuild`
 
 2 下面是xcodebuild的部分文档
  
    NAME
     xcodebuild -- build Xcode projects and workspaces

    SYNOPSIS
     xcodebuild [-project name.xcodeproj]
                [[-target targetname] ... | -alltargets]
                [-configuration configurationname]
                [-sdk [sdkfullpath | sdkname]] [action ...]
                [buildsetting=value ...] [-userdefault=value ...]

     xcodebuild [-project name.xcodeproj] -scheme schemename
                [[-destination destinationspecifier] ...]
                [-destination-timeout value]
                [-configuration configurationname]
                [-sdk [sdkfullpath | sdkname]] [action ...]
                [buildsetting=value ...] [-userdefault=value ...]

     xcodebuild -workspace name.xcworkspace -scheme schemename
                [[-destination destinationspecifier] ...]
                [-destination-timeout value]
                [-sdk [sdkfullpath | sdkname]] [action ...]
                [buildsetting=value ...] [-userdefault=value ...]

     xcodebuild -version [-sdk [sdkfullpath | sdkname]] [infoitem]

     xcodebuild -showsdks

     xcodebuild -showBuildSettings
                [-project name.xcodeproj | [-workspace name.xcworkspace -scheme schemename]]

     xcodebuild -list [-project name.xcodeproj | -workspace name.xcworkspace]

     xcodebuild -exportArchive -archivePath xcarchivepath -exportPath
                destinationpath -exportOptionsPlist path

     xcodebuild -exportLocalizations -project name.xcodeproj -localizationPath
                path [[-exportLanguage language] ...]
     xcodebuild -importLocalizations -project name.xcodeproj -localizationPath
                path
         OS X                            March 19, 2015                            OS X
         
         

## xcodebuild命令

### xcodebuild -version [-sdk [sdkfullpath | sdkname]] [infoitem]

1 显示版本信息

`$ xcodebuild -version`


    Xcode 7.3
    Build version 7D175

2 显示某个sdk的版本信息

`$ xcodebuild -version -sdk iphoneos9.3`


    iPhoneOS9.3.sdk - iOS 9.3 (iphoneos9.3)
    SDKVersion: 9.3
    Path: /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/    SDKs/iPhoneOS9.3.sdk
    PlatformVersion: 9.3
    PlatformPath: /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform
    ProductBuildVersion: 13E230
    ProductCopyright: 1983-2016 Apple Inc.
    ProductName: iPhone OS
    ProductVersion: 9.3

3 注意:
    
   1 -sdk 对应的值可以通过下面的`xcodebuild -showsdks`来得到
   
   2 infoitem显示信息项，没有什么有意义的作用可以不管
    

### xcodebuild -showsdks

1 显示sdk

`$ xcodebuild -showsdks`



    OS X SDKs:
	   OS X 10.11                    	-sdk macosx10.11

    iOS SDKs:
	  iOS 9.3                       	-sdk iphoneos9.3

    iOS Simulator SDKs:
	  Simulator - iOS 9.3           	-sdk iphonesimulator9.3

    tvOS SDKs:
	  tvOS 9.2                      	-sdk appletvos9.2

    tvOS Simulator SDKs:
	  Simulator - tvOS 9.2          	-sdk appletvsimulator9.2

    watchOS SDKs:
	  watchOS 2.2                   	-sdk watchos2.2

    watchOS Simulator SDKs:
	  Simulator - watchOS 2.2       	-sdk watchsimulator2.2



### xcodebuild -showBuildSettings
   
  1 cd进Test工程文件夹,显示buildSettings
  
   `$ xcodebuild -showBuildSettings`
   

    Build settings for action build and target Test:
        ACTION = build
        AD_HOC_CODE_SIGNING_ALLOWED = NO
        ALTERNATE_GROUP = staff
        ALTERNATE_MODE = u+w,go-w,a+rX
        ALTERNATE_OWNER = chiyou
        ALWAYS_SEARCH_USER_PATHS = NO
        ALWAYS_USE_SEPARATE_HEADERMAPS = NO
        APPLE_INTERNAL_DEVELOPER_DIR = /AppleInternal/Developer
        APPLE_INTERNAL_DIR = /AppleInternal
        APPLE_INTERNAL_DOCUMENTATION_DIR = /AppleInternal/Documentation
        APPLE_INTERNAL_LIBRARY_DIR = /AppleInternal/Library
        APPLE_INTERNAL_TOOLS = /AppleInternal/Developer/Tools
        APPLICATION_EXTENSION_API_ONLY = NO
        APPLY_RULES_IN_COPY_FILES = NO
        ARCHS = armv7 arm64
        ARCHS_STANDARD = armv7 arm64
        ARCHS_STANDARD_32_64_BIT = armv7 arm64
        ARCHS_STANDARD_32_BIT = armv7
        ....
        
        
### xcodebuild -list [-project name.xcodeproj | -workspace name.xcworkspace]

 显示关于Test.xcodeproj的信息

`$ xcodebuild -list`



    Information about project "Test":
      Targets:
        Test
        TestTests
        TestUITests

    Build Configurations:
        Debug
        Release

    If no build configuration is specified and -scheme is not passed then "Release" is used.

    Schemes:
        Test



注意：

 1 在这里我们可以得到project的`targets`以及`schemes`以及`Build Configurations`

 2 `xcodebuild -list`与`xcodebuild -list -project Test.xcodeproj`相同，因为它默认取`Test.xcodeproj`
     
 3 如果有pods，`xcodebuild -list -workspace Test.xcworkspace`
 
 
###  xcodebuild [-project name.xcodeproj][[-target targetname] ... | -alltargets] [-configuration configurationname][-sdk [sdkfullpath | sdkname]] [action ...][buildsetting=value ...] [-userdefault=value ...]

 cd进Test工程文件夹

`$ xcodebuild -sdk iphoneos9.3`

下面是编译的大致流程:

     Check dependencies 
     —CompileC 编译各个.m文件
     —Ld build/Test.build/Release-iphoneos/Test.build/Objects-normal/armv7/Test normal armv7 
     —Ld build/Test.build/Release-iphoneos/Test.build/Objects-normal/arm64/Test normal arm64 
     —CreateUniversalBinary build/Release-iphoneos/Test.app/Test normal armv7\ arm64 
     —CompileStoryboard Test/Base.lproj/LaunchScreen.storyboard 
     —CompileStoryboard Test/Base.lproj/Main.storyboard
     —CompileAssetCatalog build/Release-iphoneos/Test.app Test/Assets.xcassets
     —ProcessInfoPlistFile build/Release-iphoneos/Test.app/Info.plist Test/Info.plist 
     —GenerateDSYMFile build/Release-iphoneos/Test.app.dSYM build/Release-iphoneos/Test.app/Test
     —LinkStoryboards 
     —ProcessProductPackaging /Users/chiyou/Library/MobileDevice/Provisioning\ Profiles/2504ed49-d99e-4f7a-bafb-bd1eb4bcea9e.mobileprovision build/Release-iphoneos/Test.app/embedded.mobileprovision 
     —Touch build/Release-iphoneos/Test.app 
     —ProcessProductPackaging /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS9.3.sdk/Entitlements.plist build/Test.build/Release-iphoneos/Test.build/Test.app.xcent 
     —CodeSign build/Release-iphoneos/Test.app 
       Signing Identity:     "iPhone Developer: zhida wu (8MR2HY4EQA)"
       Provisioning Profile: "iOS Team Provisioning Profile: *"
                      (2504ed49-d99e-4f7a-bafb-bd1eb4bcea9e) —Validate build/Release-iphoneos/Test.app  
     -Validate /Users/chiyou/Library/Developer/Xcode/DerivedData/Test-dyjdzvtgqgxtqechyirrgsrcuxma/Build/Products/Debug-iphoneos/Test.app              
     ** BUILD SUCCEEDED **


当出现`** BUILD SUCCEEDED **`时，代表编译成功，

1 这种情况下，默认的`-project`的值为`Test. xcodeproj`，默认的`-target`的值为`Test`，默认的`-configuration`对应的值为`Release`，默认的`action`为`build`

2 在Test文件夹下，生成`build`文件夹，在`build`中存在`Release-iphoneos`，`Test.build`两个文件夹，`Test.app`存在于`Release-iphoneos`中。

3 签名信息，Signing Identity:     "iPhone Developer: zhida wu (8MR2HY4EQA)"
       Provisioning Profile: "iOS Team Provisioning Profile: *"
                      (2504ed49-d99e-4f7a-bafb-bd1eb4bcea9e) —Validate build/Release-iphoneos/Test.app ，自动选择的。
                      
4 可以通过`CODE_SIGN_IDENTITY`以及`PROVISIONING_PROFILE`改变签名信息

`$ xcodebuild -project Test.xcodeproj -configuration Release -sdk iphoneos9.3 build `  

1 这种情况与`xcodebuild -sdk iphoneos9.3`等价

2 可以将`iphoneos9.3`换成`iphonesimulator9.3`，`build`下会生成`Release-iphonesimulator`文件夹，可以将`Release`换成`Debug`，`build`下会生成对应的`debug_xxx`文件夹

3 作用是编译生成`xx.app`文件


    $ xcodebuild -project Test.xcodeproj -target Test -configuration Release -sdk iphoneos9.3 CODE_SIGN_IDENTITY="iPhone Distribution: Hangzhou Riguan Apparel Co.,ltd (V9LX9F46VG)" PROVISIONING_PROFILE="a97416b6-a868-44c7-8bd5-5847954305bb"

1 当我们使用xcode来进行打包的时候，`CODE_SIGN_IDENTITY`以及`PROVISIONING_PROFILE`的值就是`buildsetting`中选择的证书和`profile`文件对应的值。

2 注意，要将工程的bundle id与描述性文件中的bundle id保持一致

3 `CODE_SIGN_IDENTITY`可以通过钥匙串来查看，证书完整的名字就是对应的值

4 `PROVISIONING_PROFILE`通过xcode,同时按住`command`和`,`,然后选择Accounts->证书对应的账号->View Details ->选择对应的profile->show in finder ->文件名就是PROVISIONING_PROFILE对应的值。

5 此时的签名信息为

Signing Identity:     "iPhone Distribution: Hangzhou Riguan Apparel Co.,ltd (V9LX9F46VG)"

Provisioning Profile: "davebella_adhoc_all"(a97416b6-a868-44c7-8bd5-5847954305bb)

### xcodebuild -workspace name.xcworkspace -scheme schemename [[-destination destinationspecifier] ...] [-destination-timeout value] [-sdk [sdkfullpath | sdkname]] [action ...][buildsetting=value ...] [-userdefault=value ...]


`$ xcodebuild -workspace Test.xcworkspace -scheme Test -sdk iphoneos9.3 build`

1  -scheme的值可以通过xcodebuild -list -workspace Test.xcworkspace得到。

`$ xcodebuild -workspace Test.xcworkspace -scheme Test -sdk iphoneos9.3 archive`

1 生成一个`.xcarchive`文件,可以通过选择`window->organizer->Test` 可以看到我们的`.xcarchive`文件，右键`show in finder` 即可找到我们的文件.


### xcodebuild -exportArchive -archivePath MyMobileApp.xcarchive -exportPath ExportDestination -exportOptionsPlist 'export.plist'

     $ xcodebuild -exportArchive -archivePath /Users/chiyou/Library/Developer/Xcode/Archives/2016-05-02/Test.xcarchive -exportPath ~/desktop/ipa -exportOptionsPlist 'export.plist'

1 作用是将生成的.xcarchive文件，打包成ipa文件.

2 `-archivePath`的值即是`.xcarchive`文件的路径，可以打开xcode，选择`window->organizer->Test` 可以看到我们的`.xcarchive`文件，右键`show in finder` 即可找到我们的文件，可以看到文件的名字是`工程名+archive`的时间，我们要把名字改成容易识别的名字，例如把`Test 16-5-2 下午12.46.xcarchive`改为`Test.xcarchive`，否则识别不出来.

3 `-exportPath`对应的值为输出的ipa包的存放路径，本例中是在桌面上建立一个ipa文件夹。

4 `-exportOptionsPlist`对应的是`export.plist`文件，我们要建立一个`export.plist`文件，文件内输入`ExportDestination`，对应的值为输出ipa包的路径`~/desktop/ipa`。
 
 
 
 
## xcrun

### 简介
 ` xcrun - Run or locate development tools and properties.` 
  运行或定位开发工具以及属性
  
### 部分文档
 1 在终端中输入 `$ man xcrun`
 
 2 下面是xcrun的整个文档
  
     NAME
       xcrun - Run or locate development tools and properties.

    SYNOPSIS
       xcrun [--sdk <SDK name>] --find <tool name>

       xcrun [--sdk <SDK name>] <tool name> ... tool arguments ...

       <tool name> ... tool arguments ...

     DESCRIPTION
       xcrun  provides  a  means  to locate or invoke developer tools from the
       command-line, without requiring users to modify Makefiles or  otherwise
       take inconvenient measures to support multiple Xcode tool chains.

       The tool xcode-select(1) is used to set a system default for the active
       developer directory, and may be overridden by the  DEVELOPER_DIR  envi-
       ronment variable (see ENVIRONMENT).
       
       The  SDK  which  will be searched defaults to the most recent available
       SDK, and can be specified by the SDKROOT environment  variable  or  the
       --sdk  option  (which  takes  precedences  over  SDKROOT). When used to
       invoke another tool (as opposed to simply finding it), xcrun will  pro-
       vide  the  absolute path to the selected SDK in the SDKROOT environment
       variable. See ENVIRONMENT for more information.
       
       
       Usage
       xcrun supports several different usages, to both look up the  paths  to
       tools as well as execute them.

       When  used  with  the  --find  argument, as in xcrun [--sdk <SDK name>]
       --find <tool name>, the absolute path to the tool (in the provided SDK,
       if given) will be printed.

       When  used  without --find, the name of a tool is required and the tool
       will be executed with the provided arguments.

       When used as the target of a symbolic link, it derives the tool name to
       use from the name it was invoked under, and then executes that tool.
       
       
       OPTIONS
       -v, --verbose
              Add verbose information on how the tool lookup is performed.

       -n, --no-cache
              Don't  consult  the  cache  when  looking  up values. In effect,
              causes the cache entry to be refreshed.

       -k, --kill-cache
              Removes the cache. Causes all values to be re-cached.

       --sdk  Specifies which SDK to search for tools. If no --sdk argument is
              provided, then the SDK used will be taken from the SDKROOT envi-
              ronment variable, if present.

              Use xcodebuild -showsdks to list the available SDK names.
      --toolchain
              Specifies which toolchain to use to perform the  lookup.  If  no
              --toolchain argument is provided, then the toolchain to use will
              be taken from the TOOLCHAINS environment variable, if present.

       -l, --log
              Print the full command line that is invoked.

       -f, --find
              Enable "find" mode, in which the resolved tool path  is  printed
              instead of the tool being executed.

       -r, --run
              Enable  "run"  mode, in which the resolved tool path is executed
              with any provided additional  arguments.  This  is  the  default
              mode.

       --show-sdk-path
              Print the path to the selected SDK.
              
       --show-sdk-version
              Print the version number of the selected SDK.

       --show-sdk-build-version
              Print the build version number of the selected SDK.

       --show-sdk-platform-path
              Print the path to the platform for the selected SDK.

       --show-sdk-platform-version
              Print the version number of the platform for the selected SDK.
              
              
       ENVIRONMENT
       DEVELOPER_DIR
          Overrides the active developer directory. When DEVELOPER_DIR is set,
          its value will be used instead of the system-wide  active  developer
          directory.

       SDKROOT
          Specifies  the  default  SDK  to be used when looking up tools (some
          tools may have SDK specific versions).

          This environment variable is also set by xcrun to  be  the  absolute
          path  to  the  user  provided  SDK  (either via SDKROOT or the --sdk
          option), when it is used to invoke a normal  developer  tool  (build
          tools like xcodebuild or make are exempt from this behavior).

          For example, if xcrun is used to invoke clang via:
              xcrun --sdk macosx clang test.c
              
          then xcrun will provide the full path to the macosx SDK in the envi-
          ronment variable SDKROOT. That in turn will be used by  clang(1)  to
          automatically select that SDK when compiling the test.c file.

       TOOLCHAINS
          Specifies  the  default  toolchain  to be used when looking up tools
          (for tools which are toolchain specific).

       xcrun_log
          Same as specifying --log.

       xcrun_nocache
          Same as specifying --no-cache.

       xcrun_verbose
          Same as specifying --verbose.
          
          
       EXAMPLES
       xcrun --find clang
          Finds the path to the clang binary in the default SDK.

       xcrun --sdk iphoneos --find texturetool
          Finds the path to the texturetool binary in the iOS SDK.

       xcrun --sdk macosx --show-sdk-path
          Prints the path to the current Mac OS X SDK.

       xcrun git status
          Locates the git command and then executes it with a single  argument
          ("status").
                    
       DIAGNOSTICS
       When  xcrun  is  invoked  with  the  name  xcrun, the options --log and
       --verbose are useful debugging aids. The option --no-cache can be  used
       to bypass cache lookup, but often at a significant cost in performance.

       When xcrun has taken the place of another tool, the arguments are those
       of  the  tool replaced, and the various xcrun options can't be used. In
       this case, use the specific environment variables instead.

    SEE ALSO
       xcodebuild(1), xcode-select(1)
       
       
## xcrun 命令探析
   
###  找到二进制文件clang在默认的SDK中的路径
   
   `$ xcrun --find clang`
   
   `/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang`
  
  1 通过`/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr
  /bin/`，我们可以发现在`bin`文件夹内，有好多与clang类似的二进制文件.
  
  2 通过`xcrun --find xxxxx`，可以方便的定位出其他二进制文件的路径

### 找到二进制文件texturetool在 IOS SDK中的路径

`$ xcrun --sdk iphoneos --find texturetool`

`/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/usr/bin/texturetool`

 1 通过 `/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer
 /usr/bin/`，我们可以发现在`bin`文件夹内，有好多与texturetool类似的二进制文件.
  
 2 通过`xcrun --find xxxxx`，可以方便的定位出其他二进制文件的路径
 
 3 其中二进制文件`PackageApplication`是用来将.app文件打包成ipa文件的.
 
### 打印出当前Mac OS X SDK的路径
`$ xcrun --sdk macosx --show-sdk-path`

### 将xxx.app文件打包成xxx.ipa并输出到指定位置(重点)
`$ xcrun -sdk iphoneos -v PackageApplication ./build/Release-iphoneos/Test.app -o ~/Desktop/ipa/Test.ipa`

1 `PackageApplication`指定打包的工具

2 `./build/Release-iphoneos/Test.app`指定打包的目标文件(.app)

3 `~/Desktop/ipa/Test.ipa`指定输出的路径

### 定位git命令并执行
`$ xcrun git status`



## 参考
* [iOS自动打包并发布脚本](http://liumh.com/2015/11/25/ios-auto-archive-ipa/)
* [敲一下enter键，完成iOS的打包工作](http://ios.jobbole.com/84677/)
* [iphone-命令行编译之--xcodebuild](http://www.cnblogs.com/xiaodao/archive/2012/03/01/2375609.html)
 



     
  
  
 
  
  