---
layout: post
title: Masonry原理
date: 2016-03-23
categories: blog


---

## Masonry的简介

   1. 地址 : https://github.com/SnapKit/Masonry
   2. Masonry是链式编程的典型应用,用于ios开发中进行自动布局。

## 先简单介绍一下链式编程

   1. ios利用block来实现链式编程,其核心思想是:方法的返回值是一个Block,Block内部装着真正要执行的方法,Block内   部再返回self;
   2. 如下列的形式
   
      <pre><code> 
     -( 返回值是Block ) 方法名
         {   
            return *{   
                    Block内部装着真正要执行的代码
                    return self;
                    };
            }
     </code></pre>
            
            
   3. 简单模仿masonry的原理实现一个计算器
   
      <pre><code>
        建立一个计算的类CaculatorMaker
        在.h文件中
        @interface CaculatorMaker : NSObject
        @property (nonatomic, assign) NSInteger result;
        @property (nonatomic, strong) CaculatorMaker *(^add)(int);
        @property (nonatomic, strong) CaculatorMaker *(^sub)(int);
        @end        
        在.m文件中
       -(CaculatorMaker *(^)(int))add
         {
        return ^(int resut) {
          _result += resut;
          return self;
           };
         }
       -(CaculatorMaker *(^)(int))sub
         {
            return ^(int result) {
          _result -= result;
          return self;
           };
         }       
       </code></pre>
          
       创建NSObject+Caculator        
        在.h文件中
        <pre><code>
        +(NSInteger)makeCalulators:(void(^)(CaculatorMaker *make))caculatorMaker;
        在.m文件中
        +(NSInteger)makeCalulators:(void (^)(CaculatorMaker *))caculatorMaker
        {
            CaculatorMaker *maker = [[CaculatorMaker alloc] init];
            caculatorMaker(maker);
            return maker.result;
        }
        </code></pre>
        
    
       在控制器中实现
        <pre><code>
         [NSObject makeCalulators:^(CaculatorMaker *maker) {
           maker.add(1).add(2).sub(1);
           NSLog(@"%ld",maker.result);
               }];    
        </code></pre>
        

   4. 我利用链式编程给UIView做了一个简单的扩展来设置frame,创建**UIView+Chain**类
       在.h文件中
       <pre><code>
       -(UIView *(^)(int))x;
       -(UIView *(^)(int))y;
       -(UIView *(^)(int))with;
       -(UIView *(^)(int))height;
       </code></pre>
      在.m文件中
       <pre><code>
      \- (UIView *(^)(int))x
      {
        __weak typeof(self) wSelf = self;
          return ^(int a) {
        CGRect frame = wSelf.frame;
        frame.origin.x = a;
        wSelf.frame = frame;
        return wSelf;
          };
      }
      \- (UIView *(^)(int))y
      {
          __weak typeof(self) wSelf = self;
          return ^(int a) {
              CGRect frame = wSelf.frame;
              frame.origin.y = a;
              wSelf.frame = frame;
              return wSelf;
          };
      }

       \- (UIView *(^)(int))with
      {
          __weak typeof(self) wSelf = self;
          return ^(int a) {
              CGRect frame = wSelf.frame;
              frame.size.width = a;
              wSelf.frame = frame;
              return wSelf;
          };
       }

       \- (UIView *(^)(int))height
       {
          __weak typeof(self) wSelf = self;
          return ^(int a) {
              CGRect frame = wSelf.frame;
              frame.size.height = a;
              wSelf.frame = frame;
              return wSelf;
          };
       }
       
      </code></pre>
      
      在控制器其中使用
      
       <pre><code>
       
       UIView *view = [[UIView alloc] init];
       view.x(100).y(200).with(100).height(50);
       NSLog(@"%@",NSStringFromCGRect(view.frame));
       view.backgroundColor = [UIColor redColor];
       [self.view addSubview:view];
       
       </code></pre>
             

## Masonry原理

  1 主要的类及作用
  
    * MASViewAttribute:视图的属性，包含一个视图（view）以及该视图的布局属性(layoutAttribute)
    * MASAttribute:对NSLayoutAttribute的重定义
    * MASLayoutConstraint:NSLayoutConstraint的子类，仅仅只是增加了一个mas_key属性
    * MASConstraint:一个抽象的基类，不能直接创，包含视图的约束。
    * MASViewConstraint:是MASConstraint的子类，由MASViewAttribute进行初始化。
    * MASCompositeConstraint::是MASConstraint的子类,包含一组MASViewConstraint。
    * MASConstraintMaker:约束创建器,通过它来创建一个个约束（MASConstraint）.
    * View+MASAdditions: 对UIView的扩展
    * MASUtilities: masonry一些公共的方法和工具,MASLayoutPriority是对UILayoutPriority的重定义，     _MASBoxValue（）将传入的值转化成对应的对象.
    * 当定义了MAS_SHORTHAND这个宏后，可以省略mas_的前缀
    
 2  通过对**mas_makeConstraints:**整个流程的解析来简单分析masonry的原理，
         
        UIView *testView = [[UIView alloc] init];
        testView.backgroundColor = [UIColor redColor];
        [self.view addSubview:testView];
        [testView mas_makeConstraints:^(MASConstraintMaker *make) {
        //每一行生成一个MASViewConstraint 加到make的私有数组中constraints
        //make.top 生成一个MASViewConstraint（设置firstViewAttribute)(testView = view)
        //mas_equalTo(self.view), 设置secondViewAttribute(view = self.view)
        make.top.mas_equalTo(self.view).mas_offset(10);
        make.left.mas_equalTo(self.view).mas_offset(10);
        make.bottom.mas_equalTo(self.view).mas_offset(-10);
        make.right.mas_equalTo(self.view).mas_offset(-10);
       }];  //执行完block,遍历constraints每一个元素执行install，安装完成移除constraints中的所有元素
       
       流程分析
       1 view执行mas_makeConstraints:方法
          //如果要自动布局,这个属性必须为NO
          self.translatesAutoresizingMaskIntoConstraints = NO;
          //创建constraintMaker
           MASConstraintMaker *constraintMaker = [[MASConstraintMaker alloc] initWithView:self];
         //执行block
         block(constraintMaker);
         //constraintMaker再执行install
         return [constraintMaker install];
       2 mas_makeConstraints:的block执行的过程。
          * make.top会先生成一个viewAttribute（MASViewAttribute，view=testView,
          layoutAttribute=NSLayoutAttributeTop）,然后用viewAttribute(也即firstViewAttribute )
          初始化生成newConstraint（MASViewConstraint，
          newConstraint.layoutPriority = MASLayoutPriorityRequired;
          newConstraint.layoutMultiplier = 1;），同时把newConstraint加入到self.constraints中
          * mas_equalTo,调用- (MASConstraint * (^)(id))equalTo，调用
          - (MASConstraint * (^)(id, NSLayoutRelation))equalToWithRelation，利用self.view和
          这个约束的firstViewAttribute.layoutAttribute生成secondViewAttribute(MASViewAttribute)，   
          并且把secondViewAttribute赋值给这个约束,并且把layoutRalation赋值给这个约束。
          * mas_offset设置偏离值，调用- (MASConstraint * (^)(NSValue *value))valueOffset,根据
          value中包含的值得类型给约束的offset或者centerOffset或者sizeOffset或者
          insets赋值，赋值方法调用MASViewConstraint中的setter方法，此时约束中的
          layoutConstant被赋值。
          * 每一行生成一个约束，并添加到make的私有数组中constraints中
          * 此时的每一个约束中的值，包含_firstViewAttribute和_secondViewAttribute,
          layoutRelation，layoutMultiplier，layoutConstant
      3 make执行install，相当于make的私有数组中constraints每一个约束执行install。
      4 MASViewConstraint执行install,得到layoutConstraint（MASLayoutConstraint），通过
      _firstViewAttribute.view和_secondViewAttribute.view得到两者最近的共同父视图
      closestCommonSuperview（如果第二个是第一个的父视图，那么这个第二个view即为所求），将  
      closestCommonSuperview赋值给约束的installedView属性，installedView调用addConstraint:方法将
      layoutConstraint添加到installedView上即完成。
      5 这个流程仅仅是展示了最简单的一个流程。




         

     
  
  
 
  
  