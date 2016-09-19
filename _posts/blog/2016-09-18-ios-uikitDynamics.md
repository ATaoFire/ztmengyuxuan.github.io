---
layout: post
title: UIKit Dynamics学习
categories: ios
description: 为自己的项目加入一些动画效果。
keywords: UIKit Dynamics
---
本人进行初次学习该框架，在闲时无聊写一下简单的demo为自己丰富知识内容。

UIKit Dynamics是iOS7以后的新增的类，可以很好地改善用户体验。要实现该行为，可以创建一个UIDynamicsAnimator(动力学动画)。对于每个动力学动画生成器可以，使用各种属性和行为进行定制，例如`重力`，`碰撞检测`，`密度`，`摩擦力`等等。

常用的类有：UIAttachmentBehavior,UICollisionBehavior,UIDynamicItemBehavior,UIGravityBehavior,UIPushBehavior,UISnapBehavior这六类。


## 实现UIKit Dynamics

### 重力的实现


```
frogImageView = [[UIImageView alloc] initWithFrame:CGRectMake(20, 300, 20, 20)];
    frogImageView.backgroundColor = [UIColor redColor];
    frogImageView.userInteractionEnabled = YES;
    [self.view addSubview:frogImageView];
    animator = [[UIDynamicAnimator alloc] initWithReferenceView:self.view];
    //重力
    UIGravityBehavior * gravityBehavior = [[UIGravityBehavior alloc] initWithItems:@[frogImageView]];
    //设置重力方向
    [gravityBehavior setAngle:0 magnitude:0.1];
    [animator addBehavior:gravityBehavior];
```

注意：动态图必须是参考试图的子试图，否则力学动画生成器将不会有任何效果
 
 
### 碰撞

碰撞顾名思义是当一个物体，在运动过程中，受到障碍物的阻挡与接触，才可以发生。frogImageView和dragonImageView对象是一开始设置好的。

    ```animator = [[UIDynamicAnimator alloc] initWithReferenceView:self.view];
    //重力
    UIGravityBehavior * gravityBehavior = [[UIGravityBehavior alloc] initWithItems:@[frogImageView, dragonImageView]];
    //改变方向
    [gravityBehavior setAngle:0 magnitude:0.1];
    
    UICollisionBehavior * collisionBehavior = [[UICollisionBehavior alloc] initWithItems:@[frogImageView, dragonImageView]];
    //。还可以设置NSBezierPath或者两点之间的线段，其中前者可以使用addBoundaryWithIdentifier: forPath:
    /**
     *  要是想要物体发生碰撞，必须要定义边界translatesReferenceBoundsIntoBoundary属性
     *  还可以设置NSBezierPath或者两点之间的线段，其中前者可以使用addBoundaryWithIdentifier: forPath:后者可以使用
     addBoundaryWithIdentifier: fromPoint: toPoint:;
     */
    collisionBehavior.translatesReferenceBoundsIntoBoundary = YES;
    //设置代理
    collisionBehavior.collisionDelegate = self;
    [animator addBehavior:gravityBehavior];
    [animator addBehavior:collisionBehavior];
    ```



* [具体代码demo敬请参考](https://github.com/ztmengyuxuan/UIKitDybanics.git)


