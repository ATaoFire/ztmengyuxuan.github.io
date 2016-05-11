---
layout: post
title: ios打包--build过程探析（一）
date: 2016-04-29
categories: IOS


---

## build 过程控制
一般来说，当你选择打开xcode工程并且选择工程文件的时候，会在 project editor 顶部显示出 6 个 tabs：General, Capabilities, Info, Build Settings, Build Phases 以及 Build Rules。对我们的build过程来说，后三项与build紧密相关。

## build Phases解析

### build phases 代表将代码转变为可执行文件的最高规则，
![](http://7xqijx.com1.z0.glb.clouddn.com/1.png)

### 下图对各项过程进行简单介绍
![build Phases解析](http://7xqijx.com1.z0.glb.clouddn.com/build%2BPhases.png)

至此，build过程并没有结束，还有code sigining以及packageing阶段。总的来说我们可以把build过程分为编译，链接，
code signing ，packageing四个阶段。


## build Rules

 Build rules 指定了不同的文件类型该如何编译。一般不许要开发者进行设置，如果想要详细了解，请参考[这篇文章](http://objccn.io/issue-6-1/)

## build setting


    Prefix Header ->${SRCROOT}/工程名/文件名.pch
    Framework Search Paths -> $(PROJECT_DIR)/DV/Frameworks/Lib/QQSDK）
    Header Search Paths -> "${PODS_ROOT}/Headers/Public/AFNetworking"
    Library Search Paths -> $(PROJECT_DIR)/DV/Frameworks/Lib/PingcooSDK
    Oher Linker Flags -> -ObjC 或者 -all_load
    Code Signing Identity -> 选择证书
    Provisioning Profile -> 选择对用的配置文件

先列举我常用的，以后会继续补充

## 参考文章

* [Build 过程](http://objccn.io/issue-6-1/)









     
  
  
 
  
  