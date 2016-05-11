---
layout: post
title: ios打包--ipa包重签(四)
date: 2016-05-03
categories: IOS

---


## 证书和密匙

### 证书信息

代码签名的核心是一个证书，一个公钥和一个私钥
![](http://7xqijx.com1.z0.glb.clouddn.com/cer.png)

      

![](http://7xqijx.com1.z0.glb.clouddn.com/cer_detail.png)

可以用`$ security find-identity -v -p codesigning `来获取证书信息
  
    1) 697CC3476B6AEC059E4F12DCD5CD28C48441E4CD "iPhone Developer: zhida wu (8MR2HY4EQA)"
    2) 1C6D6C437FB47E188EE5D77105D0D993ADA93E16 "iPhone Distribution: Hangzhou Riguan Apparel Co.,ltd (V9LX9F46VG)"
    3) 8323CA449B35E26865DD08D619DE7EE221349C64 "iPhone Developer: david.wu@davebella.com (48KD969HKA)"
    4) 7494432634E5176DF5DAFF1360AAAD4B871747AB "iPhone Distribution: Hangzhou Ouer Technology Co., Ltd"
     4 valid identities found
     
注意:

* 一个证书是一个公钥加上许多附加信息组成
* 这些附加信息都是被某个认证机构（Certificate Authority 简称 CA）进行签名认证过的
* 认证的目的是认证这个证书中的信息是准确无误的
* 认证的签名有固定的有效期，这就意味着当前系统时间需要被正确设置
* 如果我们把系统时间设置的较早或者较后，那么证书会变成失效状态(亲测)

## 签名工具codesign

### codesign 的路径

`$ xcrun --find codesign`

    /usr/bin/codesign
    
    
### codesign 简单介绍

 * 签名工具，用来创建和修改代码签名
 * 由[ios打包--xcodebuild以及xcrun(二)](http://www.lhjzzu.com/2016/04/29/ios-xcodebuild/#section)中的`$ xcodebuild -sdk iphoneos9.3`，可知在ProcessProductPackaging之后，会用CodeSign来对Test.app进行代码签名
 
### codesign 命令

为一个没有被签过名的.app文件签名

 `$ codesign -s 'iPhone Developer: zhida wu (8MR2HY4EQA)' Test.app`
 
    Test.app: is already signed

如果app文件已经被签名过了,通过`-f`强制覆盖原来的签名

 `$ codesign -f -s 'iPhone Developer: zhida wu (8MR2HY4EQA)' Test.app`
   
    Test.app: replacing existing signature
    
查看.app的相关信息

`$ codesign -vv -d Test.app`

    Executable=/Users/chiyou/Library/Developer/Xcode/DerivedData/Test-   fmbqgffmjssiqmbnzkproqvtcqpm/Build/Products/Debug-iphoneos/Test.app/Test
    Identifier=com.ouer.www.Test
    Format=app bundle with Mach-O universal (armv7 arm64)
    CodeDirectory v=20200 size=657 flags=0x0(none) hashes=14+4 location=embedded
    Signature size=4717
    Authority=iPhone Developer: zhida wu (8MR2HY4EQA)
    Authority=Apple Worldwide Developer Relations Certification Authority
    Authority=Apple Root CA
    Signed Time=2016年5月3日 下午11:03:58
    Info.plist entries=27
    TeamIdentifier=V9LX9F46VG
    Sealed Resources version=2 rules=12 files=7
    Internal requirements count=1 size=176
    
 * `iPhone Developer: zhida wu (8MR2HY4EQA)`由`Apple Worldwide Developer Relations Certification Authority`授权，`Apple Worldwide Developer Relations Certification Authority`由`Apple Root CA`授权，所以`Apple Root CA`是根证书
 
 * `Format=app bundle with Mach-O universal (armv7 arm64)`表明Test.app是一个包含armv7，arm64的二进制文件
 * `Identifier`即是bundle identifier
 * `TeamIdentifier`标示工作组，一个开发者(账号)有唯一的一个工作组.（即无论是打包证书还是push证书，工作组都一样）
 
 
 验证签名后的.app文件
 
 `$ codesign --verify Test.app`
  
 * 没有任何输出信息，代表没有问题

如果修改.app文件，就会破坏我们的签名的完整性

    $ echo 'lol' >> Test.app/Test
    $ codesign --verify Test.app
    Test.app: main executable failed strict validation  
    
## 程序包和其他资源文件

* 程序包中的所有文件都会被签名，所有的签名都放在`_CodeSignatue/CodeResources`中.
* 在 CodeResources 文件中会有4个不同区域，其中的 rules 和 files 是为老版本准备的，而 files2 和 rules2是为新的第二版的代码签名准备的
* 更详细的信息请参考[代码签名探析](http://objccn.io/issue-17-2/)


## 授权机制 (Entitlements) 和配置文件 (Provisioning)

### 授权机制

Xcode 会自动生成一个entitlements文件(plist格式),文件格式如下

    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
    	<key>application-identifier</key>
	    <string>7T2277EURS.com.ouer.test</string>
	    <key>com.apple.developer.team-identifier</key>
	    <string>7T2277EURS</string>
	    <key>get-task-allow</key>
	    <false/>
	    <key>keychain-access-groups</key>
	    <array>
		    <string>7T2277EURS.com.ouer.test</string>
	    </array>
    </dict>
    </plist>

授权机制决定了哪些系统资源在什么情况下允许被一个应用使用


查看签名信息中具体包含了什么授权信息（从ipa包中解压得到Test.app）

`$ codesign -d --entitlements - Test.app`

    Executable=/Users/chiyou/Desktop/xxxx/Test 2016-05-04 00-11-33/Payload/Test.app/Test
    ??qq?<?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/    PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
    	<key>application-identifier</key>
    	<string>V9LX9F46VG.com.ouer.www.Test</string>
    	<key>com.apple.developer.team-identifier</key>
    	<string>V9LX9F46VG</string>
	    <key>get-task-allow</key>
	    <false/>
	    <key>keychain-access-groups</key>
	    <array>
	    	<string>V9LX9F46VG.com.ouer.www.Test</string>
	    </array>
    </dict>
    </plist>
 

### 配置文件

* XCode中配置文件都可以在`~/Library/MobileDevice/Provisioning Profiles`找到。
* 它并不是一个 plist 文件，它是一个根据密码讯息语法 (Cryptographic Message Syntax) 加密文件
* 通过`security cms -D -i example.mobileprovision`，查看.mobileprovision文件内部信息
 
   
 

## 重签名ipa

### 准备:

* 一个已经签名的ipa包（例如 DV.ipa）
* 企业发布证书，以及distribution的.mobileprovision文件，命名为embedded
* embedded.mobileprovision的bundle identify可以自定(例如com.ouer.test)
* 创建一个entitlements.plist文件,内容如下


        <dict>
           	<key>application-identifier</key>
       	    <string>7T2277EURS.com.ouer.test</string>
	        <key>com.apple.developer.team-identifier</key>
       	    <string>7T2277EURS</string>
	        <key>get-task-allow</key>
	        <false/>
	        <key>keychain-access-groups</key>
	        <array>
		    <string>7T2277EURS.com.ouer.test</string>
	        </array>
        </dict>


其中`7T2277EURS`为`team-identifier`，`com.ouer.test`为`bundle identify`


### 整个签名过程如下

#### 方法一:用codesign命令行
1 解压DV.ipa

`$ unzip DV.ipa`

2 替换证书配置文件（文件名必须为embedded，不得自定义,embedded.mobileprovision与Payload文件夹同级）

`$ cp embedded.mobileprovision Payload/DV.app`

3 重签名（entitlements.plist与Payload同级）

    $ codesign -f -s "iPhone Distribution: Hangzhou Ouer Technology Co., Ltd" --entitlements entitlements.plist Payload/DV.app

4 打包

`$ zip -r DV_Resign.ipa Payload`

注意:

* 步骤3执行之前，可以执行`$ open Payload/DV.app/info.plist`,然后修改`Bundle identifier`,然后执行继续执行步骤3，这种情况下由于`Bundle identifier`不同，所以我们的设备可以安多个app。
* 修改`Bundle identifier`有些弊端是不能进行微博登录，并且不能收到推送等等。


#### 方法二:使用工具iReSign

![](http://7xqijx.com1.z0.glb.clouddn.com/iResign.png)

1 下载[iReSign](https://github.com/maciekish/iReSign)工具

2 选择`.ipa`,`embedded.mobileprovision`,`entitlements.plist`文件

3 需要修改`Bundle identifier`为`embedded.mobileprovision`的`Bundle identifier`，否则不能通过。

4 点击重新签名


注意: 

* 修改`Bundle identifier`有些弊端是不能进行微博登录，并且不能收到推送等等。

#### 方法三:自动化脚本(autoResign)

1 这是我写的脚本[autoResign](https://github.com/lhjzzu/autoResign),你可以下载直接使用

2 用法 `$ python autoResign.py -f DV`,如果成功会生成一个`DV_Resign.ipa`文件

3 如果第二次执行该命令，会出现 `Archive:  DV.ipa
replace Payload/DV.app/_CodeSignature/CodeResources? [y]es, [n]o, [A]ll, [N]one, [r]ename: `,直接输入A，然后enter即可。


## 补充:

### 设置别名--彻底解放

我们可以把我们的某些命令，设置一个简单的别名，那么在我们执行的时候，只需输入别名即可

    1 cd ~
    2 vi .bash_profile
    3 点击i,进入输入模式，
      输入:alias resign='python autoResign.py -f'
      点击esc，shift+:,wq 退出
    4 source .bash_profile
    5 进入对应的文件夹，在终端中resign DV即可。


## 参考
* [代码签名探析](http://objccn.io/issue-17-2/)
* [iOS证书及ipa包重签名探究](http://www.olinone.com/?p=198)
* [ReCodeSign](https://gist.github.com/0xc010d/1365444)
 



     
  
  
 
  
  