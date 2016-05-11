---
layout: post
title: Cocoapods系列:使用Cocoapods制作静态库(三)
date: 2016-05-10
categories: IOS

---

## 为什么要用Cocoapods制作静态库呢？

我们本来就可以通过`xcode`来进行静态库，`Cocoapods`制作静态库主要是解决第三方冲突的问题。

当我们开发`sdk`的时候，假如我们的静态库中需要使用一个第三方库，我们把这个第三方库打包进我们的`lib`中，当别人在使用我们的`lib`，如果他的工程中也已经使用可这个第三方库，那么就会造成冲突。

假设现在有一个需求，我要开发一个`sdk`，其中的下载图片我想用`SDWebImage`。但是众所周知`SDWebImage`是一个非常常用的库，基本上大部分的App都会使用到。那么当我的`sdk`的`lib`中使用了`SDWebImage`后，如何保证它不和别人工程中的`SDWebImage`冲突?`重命名`这个第三方库的所有文件--这是唯一的解决方法。但是假如让我们一个一个文件的重命名这基本是一个不可能完成的任务，更何况还有库之间的依赖。`Cocoapods`给我们提供了解决方案，通过`Cocoapods`我们可能很方便的制作我们的静态库并且对第三方库进行重新命名。






## 参考
* [使用CocoaPods开发并打包静态库](http://www.cnblogs.com/brycezhang/p/4117180.html)


     
  
  
 
  
  