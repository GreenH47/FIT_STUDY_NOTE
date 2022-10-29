# How to use this note
1. download the whole repository and view it via [Obsidian vault](https://help.obsidian.md/How+to/Working+with+multiple+vaults) that can show the linked section in the note document ![](pic/Pasted%20image%2020221029104434.png)
	and all linked file in text without checking the attachment folder ![](pic/Pasted%20image%2020221029122902.png)

2. you can view the MD file online but will lose the extra information

# Week 2 Requirements engineering
![](pic/Pasted%20image%2020221027144847.png)
+ Business: what is it that the business requires  the system to do  业务需要系统做什么
+ User: what is it that the user (or customer)  requires the system to do. A user can be a  stakeholder.  用户（或客户）需要系统做什么。用户可以是利益相关者
+ Functional: what the system should  functionally do  系统在功能上应该做什么
+ Non-functional: quality of service system  required to provide  系统需要提供的服务质量
+ Constraint: things that system should prohibit  the user to do  系统应该禁止用户做的事情
+ Implementation: platform, etc requirements of  the system平台等系统要求

## Functional requirements
+ ==定义系统的行为==
+ Describe functionality or system services 描述功能或系统服务  
+ Describe how the system should react to particular inputs  and how the system should behave in particular  situations  描述系统应如何对特定输入做出反应以及系统在特定情况下应如何表现
+ Expressed as inputs and outputs 表示为输入和输出

### Example
+ A user shall be able to search properties for all suburbs
+ At the end of each month, the system shall generate a  list of properties sold or rented
+ Each property agent shall be uniquely identified by his or her 8-digit employee number.
+ ==login  不是功能性要求==

## Non-functional requirements
+ ==定义系统的特性, 一般是隐性的==
+ A specific criteria that can be used to judge the operation of a system, rather than specific behaviours可用于判断系统运行而非特定行为的特定标准
+ The nitty-gritty of the services or functions offered by the system. The requirements that makes the quality of the system better系统提供的服务或功能的本质。使系统质量更好的要求
+ Often apply to the system as a whole rather than individual features or functions.通常适用于整个系统而不是单个特性或功能
+ Non-functional requirements may be more critical than functional requirements. If they are not met, the system may be useless非功能性需求可能比功能性需求更重要。  如果不满足，系统可能无用

### Example
+ number of customers allowed, password requirements, response time, storage requirements, I/O device capability, among others.允许的客户数量、密码要求、响应时间、存储要求、I/O 设备能力等。
+ the property management system shall be available to all property agents ***during normal working hours (Mon–Fri, 0830–1730***
+ Customers must authenticate themselves ***using their drivers license***
+ After receiving an inspection request, the system must acknowledge with a response e-mail ***within 10 seconds***
+  ==login  不是非功能性要求==

## USE CASE DIAGRAMS
TO DESCRIBE AND DOCUMENT ALL INTERACTIONS WITH THE SYSTEM 描述和记录与系统的所有交互
![](pic/Pasted%20image%2020221027160234.png)

A use case models an interaction between the software product itself and the users  (actors) of that software product  
Tool for formalizing your understanding of requirements.  
Captures some user-visible function or behaviour.  
Relationship(s) between actors and use cases
用例对软件产品本身与该软件产品的用户（参与者）之间的交互进行建模 • 用于形式化您对需求的理解的工具。 • 捕捉一些用户可见的功能或行为。 • 参与者和用例之间的关系

### syntax
![](pic/Pasted%20image%2020221027160356.png)
![](pic/Pasted%20image%2020221027160249.png)

### Actor
An actor is a member of the world outside the software product

How to identify
+ An actor is a frequent user of the software product  
+ Most of the software have more than one type of actor
+ ==As an initiator:发起人
• is generally an actor who initiates/start the use case  通常是发起/启动用例的参与者
• is placed on the left-side of the use case diagram 位于用例图的左侧==
+  ==As a participant;  参与者
• is generally an actor who participates in the use case  参与用例
• placed on the right-side of the use case diagram  放置在用例图的右侧
• one actor can participant in multiple use case 一个参与者可以参与多个用例==
> Customer must go to the real estate agent’s office with proof of ownership (of the house/apartment) to let the real estate agent add the property to the system for sale. 
> Real estate agent is the initiator and customer is the participant
![](pic/Pasted%20image%2020221027161521.png)

Overlapping actors (Actor Generalization)
If two actors communicate with the same set of use cases in the same way,  we can express this as a generalization to another (possibly abstract)  actor 如果两个参与者以相同的方式与同一组用例进行通信，我们可以将其表示为对另一个（可能是抽象的）参与者的概括
![](pic/Pasted%20image%2020221027165454.png)

### Inclusion and extension
Inclusion:  `<<Include>>  `
+ The inclusion are compulsory part of the use case.  包含是用例的强制性部分
+ An including use case never stands alone. It always includes the included use case 包含用例永远不会孤立。它始终包括包含的用例
![](pic/Pasted%20image%2020221027165928.png)

Extension:  `<<Extend>>`
+   is used to separate optional behaviour from mandatory  behaviour.  用于将可选行为与强制行为分开
+ The extended use case may stand alone, but, under certain conditions,  it may be extended by another use case扩展用例可能是独立的，但在某些情况下，它可能会被另一个用例扩展
![](pic/Pasted%20image%2020221027170202.png)

Example
![](pic/Pasted%20image%2020221027170336.png)
> When a student is enrolled, a confirmation is required to be sent to the student
> When a student is enrolled, a student can choose to enroll to the units
>  How to find what to include or extend?
>  Check your client’s requirements
![](pic/Pasted%20image%2020221027170246.png)

## ==必考User stories==
+ A user story is an informal, general explanation of a software feature written from the perspective of the end user or customer. ==从客户的角度出发，非正式的，普遍的软件功能的解释 功能性要求==
+ The purpose of a user story is to articulate how a piece of work will deliver a particular value back to the customer. ==目的是阐明一项工作将如何向客户交付特定的价值==
+ 用户故事应该非常简短，并从客户的角度编写——它们通常需要放在索引卡上。  
+ 由于它们是根据需要来表述的，因此通常很容易为它们编写测试。  
+ 这些用户故事应以客户的语言编写，并使用适合其业务的术语。

`As a <user>, I want to <goal> so that <benefit>`
+ As a (who wants to accomplish something)==谁需要这个功能 [user]==
+ I want to (what they want to achieve) ==他们想要做什么？[goal]==  
+ So that (why they want to achieve the goal) 这样==做会带来什么好处呢？[benefit]==  Benefit is optional, but is it?

Example
+ As a wiki user, I want to upload a file to the wiki so that I can share it with my colleagues
+ As a survey  participant, I want an  indication of  progress so that I  know how much I  have left to complete
+ As a customer, I  would like the  system to not  corrupt the  database


the INVEST mnemonic to guide user stories
+ Independent（独立的）用户故事之间应该尽量避免相互依赖
+ Negotiable（可协商的）所有之前达成的一致在新的变化发生情况下，协商后达成新的一致，从而推动系统的研发进展。
+ Valuable to users or customers（对用户或者客户是有价值的）如果不知道用户故事给用户带来什么好处，就无法知道用户故事的价值
+ Estimable（可估算的）user stories 应该与可以估计实现工作量的功能相对应。
+ Small（小的）user stories 必须足够小 追求快速交付
+ Testable（可测试的），所有合格的需求必须是可测试的


## ==必考Acceptance criteria==
==the criteria to test that the user story is implemented as expected. 测试用户故事是否按预期实施的标准== user story的边界，用于确认软件何时按预期工作，即故事何时完成
+ Good Acceptance Criteria 会带有非功能性需求。
+ 它是一个顺序结构，写它的语法使用==一般现在时== 
+ 禁止使用 can, will, be able to 等词  
+ 动词的使用必须准确和小组选择的程序类型有关。  Text-based ： 不可以用choose, click, select。 可以用 enter.  Desktop-based: 不可以用enter
+ ==顺序 不会报错 理想 positive test==
+ ==在哪个页面让我干什么 导航到下一个页面==
+ ==最后非功能性需求==

### example 
user story 1
> For a smart home app, one of the user stories could be: “As a homeowner, I want to be able to dim or brighten individual light globes so that I can create my ideal lighting.

The acceptance criteria for this user story might be
+ The user will select a globe and then see this view;  
+ This view should use a slider control so that the user has the full range of brightness levels  available to them;  
+ When opening this view, the initial slider position should reflect the current brightness of the  selected globe;  
+ The time for a light globe to respond to a change made by the user should be no greater  than 1 second

User story 2
> As a Customer I want to to check the  balance of my bank account so that I  can perform transactions

The acceptance criteria 2
+ Customer logged in before  checking balance.  
+ Balance for all accounts is  displayed

User story 3
> As a Customer I want to transfer money from my  account to another bank account so that I don’t  have to go to the bank for making such  transactions

The acceptance criteria 3
+ Customer logged in before transferring  amount.
+ System check the receivers account number  and validate it prior to performing the  transactions.  
+ If Ok the local account balance is updated  and displayed.  
+ System update both accounts concurrently

## USABILITY DESIGN  PRINCIPLES
USABILITY DESIGN PRINCIPLES HELPS US  UNDERSTAND THE BETTER WAY TO DESIGN THE  USER-INTERFACE OF A SOFTWARE 可用性设计原则帮助我们了解设计软件用户界面的更好方法
### Donald Norman’s design principles
+ (1) Visibility: relevant objects should be in view and obvious to recognise (1) 可见性：相关物体应清晰可见且易于识别
+ (2) Affordance: the appearance of an object should indicate how it should be used （2）可供性：一个物体的外观应该表明它应该如何使用
+ (3) Constraints: limiting the possible actions of an object, to prevent user making errors (3) 约束：限制一个对象可能的动作，防止用户出错
+ (4) Cognitive aids/ Feedback: External representations intended to gain our attention (4) 认知辅助/反馈：旨在引起我们注意的外部表征
+ (5) Consistency/ Transfer effects: transferring learning and expectations of similar  objects/interfaces to the current task (5) 一致性/迁移效果：将相似对象/接口的学习和期望迁移到当前任务
+ (6) Natural mapping: laying out screens to better represent their function (6) 自然映射：布局屏幕以更好地表现其功能

### Ben Shneiderman’s 8 golden rules
+ Strive for consistency: consistent user-interfaces 力求一致性：一致的用户界面
+ Cater to universal usability: for all range of users (age, disability, etc) 迎合通用可用性：适用于所有范围的用户（年龄、残疾等）
+ Offer informative feedback: give user feedback on their actions (green, tick, sound,  highlighting, etc) 提供信息反馈：向用户提供有关其操作的反馈（绿色、勾选、声音、突出显示等）
+ Design dialogue to yield closure: feedback or warnings at the end of the action 设计对话以产生关闭：行动结束时的反馈或警告
+ Prevent errors: detect error, let the user undo their mistake 预防错误：检测错误，让用户撤消错误
+ Permit easy reversal of actions: offer an easy way out where possible (change of mind,  unsubscribe) 允许轻松逆转行动：在可能的情况下提供简单的出路（改变主意，取消订阅）
+ Support internal locus of control: give the user a sense of control. Let the user initiate, and  control actions 支持内部控制点：给用户一种控制感。让用户发起和控制动作
+ Reduce short-term memory load: Don’t make navigation and tasks excessively complex—use  meaningful mnemonics, icons, and abbreviations or “hint” 减少短期记忆负荷：不要让导航和任务过于复杂——使用有意义的助记符、图标和缩写或“提示”

# Week 3 Analysis and OOP Concepts
## UML
for specifying, visualizing,  constructing and documenting the artefacts of software  systems, as well as for business modeling and other non-  software systems用于指定、可视化、构建和记录软件系统的人工制品，以及用于业务建模和其他非软件系统

Static diagrams 静态图
+ display the organization of a system in terms  of the components that make up that system and their  relationships 根据构成该系统的组件及其关系显示系统的组织

Dynamic diagrams 动态图
+ show the dynamic behaviour of the objects in  a system   E.g., how different components communicate with each other to  perform a task 显示系统中对象的动态行为 • 例如，不同组件如何相互通信以执行任务

![](pic/Pasted%20image%2020221027204817.png)
1. Use case diagrams, which show the interactions between a system and its environment, together with use case scenarios which provide more interaction details 用例图，显示系统与其环境之间的交互，以及提供更多交互细节的用例场景
2. Class diagrams, which show the object classes in the system  and the associations between these classes 类图，显示系统中的对象类以及这些类之间的关联
3. interaction Diagrams, which show interactions between actors  and the system and between system components.  • Sequence diagram shows object interactions arranged in  time sequence 交互图，显示参与者与系统之间以及系统组件之间的交互。 • 序列图显示按时间顺序排列的对象交互
4. Statecharts , which show how the system reacts to internal and  external events. 状态图，显示系统如何对内部和外部事件作出反应

## Requirements Analysis: The 3 steps - Overview
+ Functional modelling Present scenarios of all the use cases Use case scenario 功能建模 o 所有用例的当前场景 o 要创建的人工制品：用例场景
+ Class modelling   Determine the entity classes and their attributes  Determine the interrelationships and interactions between the entity classes   Class diagram 类建模 o 确定实体类及其属性 o 确定实体类之间的相互关系和交互 o 要创建的人工制品：类图
+ Dynamic modelling  Determine the operations performed by or to each entity class   State chart 动态建模 o 确定每个实体类执行的操作或对每个实体类执行的操作 状态图

### Use case scenario
A scenario = a description of a use case  
A scenario can be “normal” and “exception”
场景 = 用例的描述 场景可以是“正常”和“异常”
![](pic/Pasted%20image%2020221027214214.png)
+ Use Case Name - short, descriptive verb phrase;  简短的描述性动词短语 
+ Scenario - a sentence that captures the essence of the use case (functionality);  捕捉用例本质（功能）的句子
+ Trigger – the actor who perform certain actions to triggers the use case;  实际触发用例的参与者
+ Brief description - a paragraph that captures the goal of the use case;  简要描述：描述用例目标的段落
+ Actors - actors involved in the use case (initiator and participant actors);  用例中涉及的参与者（发起者和参与者参与者）
+ Related use cases - does the use case have any relation with other use cases – inclusion/exclusion/generalization?   相关用例：该用例是否与其他用例有任何关系 - 包含/排除/泛化
+ Preconditions – the conditions that must met before the use case can execute, they can be considered as constraints;  先决条件：在用例可以执行之前必须为真的事情——它们是对系统状态的约束；
+ Postconditions – the conditions that must be met at the end of the use case, they can be considered as outcomes  后置条件： 在用例结束时必须为真的事情；
+ Flow of events - the steps in the use case (if everything goes well – no error, interruption);  事件流：用例中的步骤（如果一切顺利——没有错误、中断）；
+ Exception conditions - a list of alternatives to the main flow (capture errors, interruption to the main flow)异常条件： 主要流程的替代列表（捕获错误，中断主要流程）

### Class diagram
Class diagrams are used when developing an object-oriented  system model to show the classes in a system and the associations  between these classes.在开发面向对象的系统模型时使用类图来显示系统中的类以及这些类之间的关联。

objects represent something in the  real world Easy way to remember: they are usually nouns, such as a patient, a prescription, a recipe, a doctor, a  lecturer, student, etc.   对象代表现实世界中的某些事物，例如患者、处方、食谱、医生、讲师、学生等。 • 易于记忆：它们通常是名词
#### Essential Elements of a UML Class Diagram
+ Class  类
+ Attributes  属性
+ Operations  操作
+ Relationships  关系
+ Associations  Generalization  Composition/Aggregation  Dependency  关联 • 泛化 • 组合/聚合 • 依赖关系
+ Constraint Rules and Notes 约束规则和注释



# WEEK 4
## WEEKLY QUIZ
![](pic/5136w4.jpg)
## ==必考Workflows==
![](pic/Pasted%20image%2020221028162049.png)
+ 这四个Phase加起来叫一个Event，另外Event之间需要解释
+ Person-hour = amount of work 1 person can do in 1 hr 工时 = 1 人在 1 小时内可以完成的工作量
+ Shaded area = person-hrs x time = total effort 阴影面积 = 工时 x时长 = 总努力

![](pic/Pasted%20image%2020221028162732.png)

# ==重点WEEK 5 Initial Class Diagram,Sequence Diagram, State Chart==
## WEEKLY QUIZ
answer content in 5136w5.pdf
![](pic/5136w5.pdf)

## Associations
https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-class-diagram/

![](pic/Pasted%20image%2020221028165814.png)
+ If the association has a navigability (i.e.an arrow on one end) it indicates that one class knows about the other but not vice versa 如果关联具有可导航性（即一端有箭头），则表明一个类知道另一个类，反之则不然

![](pic/Pasted%20image%2020221028170035.png)
+ Sometimes, the association is complex – needs a class  (sometimes called Association Class) to represent it有时，关联很复杂——需要一个类（有时称为关联类）来表示它。
![](pic/Pasted%20image%2020221028170132.png)

+ Each end of an association can have its multiplicity shown. This indicates how many objects of each class are involved in the association. One to one;  One to Many;  Many to one; Many to many; We read multiplicities from left to right 关联的每一端都可以显示其多重性。 ▪ 这表示关联中涉及每个类的对象数。 – 一对一 – 一对多 – 多对一 – 多对多 ▪ 我们从左到右阅读多重性
![](pic/Pasted%20image%2020221028170826.png)

## ==重点The Generalization Relationship 对应关系==
Lots of different terms for this  
+ Inheritance  
+  “is-a”  
+ Generalization 
+  Superclass/subclass

### Generalization 归化 空心箭头指向父类
![](pic/Pasted%20image%2020221028172329.png)
![](pic/Pasted%20image%2020221028172504.png)
+ 能够推断这些类的不同成员具有一些共同特征
+ 概括地说，与较高级别的类相关联的属性和操作也与较低级别的类相关联

### The “is-a” relationship 
![](pic/Pasted%20image%2020221028172806.png)
![](pic/Pasted%20image%2020221028172817.png)
Subclasses inherit the attributes and operations of their  superclass 子类继承其超类的属性和操作
+ Every lecturer and every tutor have name, id and password,  inherited from the User class.  每个讲师和每个导师都有从 User 类继承的姓名、ID 和密码
+ Lecturers and Tutors can mark assignments, because Users  can讲师和导师可以标记作业，因为用户可以

Subclasses provide extra operations and attributes 子类提供额外的操作和属性
+ Lecturers can create assignments 讲师可以创建作业

### Aggregation (has-a relationship) 聚合 a 是b 的一部分 空心菱形
![](pic/Pasted%20image%2020221028173451.png)
![](pic/Pasted%20image%2020221028173503.png)
+ An aggregation model shows how classes that are collections are composed of other classes. 聚合模型显示作为集合的类如何由其他类组成
+ An aggregation is the kind of association that exists between a group and its members 聚合是存在于组及其成员之间的一种关联
+ the aggregate object may potentially exist without  its constituent objects (although not necessarily in  a useful state),  聚合对象可能在没有其组成对象的情况下存在（尽管不一定处于有用状态）
+ at any time, each object may be a constituent of  more than one aggregate (e.g. a person may  belong to several clubs)在任何时候，每个对象都可能是多个聚合的组成部分（例如，一个人可能属于多个俱乐部）
+ constituent objects are typically of the same class  (but, again, that’s not always the case)组成部分对象通常属于同一类（但同样，情况并非总是如此）
## ==重点how do we get from requirements to classes==
+ ==Determine entity classes and their attributes  (particularly entity)  确定实体类及其属性（尤其是实体==
+ ==Determine the interrelationships and  interactions between the classes  确定类之间的相互关系和交互==
+  ==Represented as a class diagram 表示为类图==

Goal  
+ to create a dictionary of abstractions.

How?
+ Study use case scenarios
+ other requirements docs.

Steps:
+ Start by looking for tangible things.寻找有形的东西开始
+ Figure out what is inside and outside the problem boundary弄清楚问题边界的内部和外部是什么
+ Some things may be classes 有些东西可能是类
+ Some may be simple attributes 有些可能是简单的属性

### Scenario
> ![](pic/Pasted%20image%2020221028183818.png)
> ![](pic/Pasted%20image%2020221028183834.png)
### Classification of identified nouns 已识别名词的分类
Candidate entity classes 候选实体类:
+ RealEstateSystem, Agent, Property, House, Apartment, Category, ForRent, ForSale, RealEstateCompany

Abstract nouns* (attributes) 抽象名词*（属性）
+ list of properties, list of agents, name of the agent, mobile number,  business name, address of the company, number of storeys, age of  the property, unit number, floor number, id, street address, suburb,  no of bedrooms, no of bathrooms, number of car spaces, floor plan,  type, inspection time, price per week, bond, available date, land  size, selling price

Outside problem domain:
+ system (redundant), city, Parallex, council, council administrators  (redundant), property’s information (synonym), amount (redundant),  market, companies, month, administrator

### identify multiplicities and relationships 识别多重性和关系
+ Not all the classes will have a relationship with each other It could be: Association ▪ Generalisation ▪ Aggregation 并非所有的类都会相互关联——可能是： ▪ 关联 ▪ 泛化 ▪ 聚合
+ If two classes do not have a relationship with each other, they do  not have multiplicity either 如果两个类之间没有关系，它们也不具有多重性
+ Multiplicities are only added for association and aggregation  Could be:  ▪ One to one  ▪ One to many  ▪ Many to many (– If it is many to many, leave it as it is for initial class diagram)  多重性仅用于关联和聚合 – 可能是： ▪ 一对一 ▪ 一对多 ▪ 多对多 – 如果是多对多，则保留其为初始类图
+ For each class, find out what other classes it needs to  interact.   to manage the data of the other class  ▪ is dependent on the data of the other class  ▪ the two classes in question needs to work together对于每个类，找出它需要交互的其他类。 – 交互是 ▪ 管理其他类的数据 ▪ 依赖于其他类的数据 ▪ 有问题的两个类需要一起工作

### commonalities in responsibilities
Look for commonalities in responsibilities between classes. ▪ See whether these can be simplified using inheritance – does an “is-a” relationship exist? 寻找类之间职责的共同点。 ▪ 看看这些是否可以使用继承来简化——是否存在“is-a”关系？

Example of inheritance:  
+ Type of Properties  ▪ House  ▪ Apartment  
+ Type of Category  ▪ ForRent  ▪ ForSale

## ==重点Initial Class Diagram==
![](pic/Pasted%20image%2020221028193236.png)
![](pic/Pasted%20image%2020221028213041.png)
![](pic/Pasted%20image%2020221029152323.png)
### ==重点how to draw diagram==
1. 仔细阅读收集到的客户需求
2. 定义所有收集到资料的名词部分，并对他们具体分类： [Classification of identified nouns 已识别名词的分类](#Classification%20of%20identified%20nouns%20已识别名词的分类)
+ Abstract Noun; 
+ Outside problem Noun; 
+ Candidate entity class
3. 画出所有的Candidate entity class, 定义它们之间的关系
+ “is-a”relationship (Inheritance);  [Generalization 归化 空心箭头指向父类](#Generalization%20归化%20空心箭头指向父类)
+ Aggregation relationship; [Aggregation (has-a relationship) 聚合 a 是b 的一部分 空心菱形](#Aggregation%20(has-a%20relationship)%20聚合%20a%20是b%20的一部分%20空心菱形)
+ Association relationship;[Associations](#Associations)
4. Identify the multiplicity between classes [identify multiplicities and relationships 识别多重性和关系](#identify%20multiplicities%20and%20relationships%20识别多重性和关系)
+ One to One; 
+ One to many;
+  Many to many (必须避免)
5. 把收集到的abstract noun 填入attribute 里，检查是否合适
## Three Types of Classes
==Model = Entity Classes;   View = Boundary Classes;  Controller = Control Classes==
![](pic/Pasted%20image%2020221028193759.png)
![](pic/Pasted%20image%2020221028200652.png)

### Entity Class 实体类 Model
+  Models “long-lived” information  模型“长期存在的”信息 
+ Usually “passive” But they may still contain complex algorithms.  Examples: Property, Agent, Real Estate Company通常是“被动的”——但它们可能仍包含复杂的算法。 • 示例：物业、代理、房地产公司
+ ![](pic/Pasted%20image%2020221028193822.png)

### Boundary Class 边界类 View
+ Class that lives on the system’s  “automation boundary”存在于系统“自动化边界”上的类
+ Models the interaction between  product and environment  (actor)  • 对产品和环境（参与者）之间的交互进行建模
+ Associated with input or output  • 与输入或输出相关联
+ ![](pic/Pasted%20image%2020221028194027.png)

### Control Class 控制类 Controller
+ Mediate interaction between  boundary and entity classes.  调解边界和实体类之间的交互。
+ Models complex computations and  algorithms  为复杂的计算和算法建模
+  Sometimes relate to use cases – but  not always.  有时与用例相关——但并非总是如此
+  For simple program, possibly the class  that contains the main() method 对于简单程序，可能是包含 main() 方法的类
+ ![](pic/Pasted%20image%2020221028200632.png)

### class communication
![](pic/Pasted%20image%2020221028200821.png)

## ==重点Sequence diagram==
![](pic/Pasted%20image%2020221028202912.png)
+ The realization of a specific scenario of a use case is  depicted using an interaction diagram 使用交互图来描述用例的特定场景的实现
+ Models the ==flow of logic== within the system 对系统内的逻辑流进行建模
+  Describes how—and in what order—a group of objects  works together  描述一组对象如何以及以何种顺序协同工作
+ Shows the ==interactions between objects.  显示对象之间的交互==
+  Plan and understand the detailed functionality of an existing or future scenario.  规划和理解现有或未来场景的详细功能
+ Models the details of a use case – a use case scenario为用例的细节建模 用例场景

### ==Sequence Diagram for Use Case==
+ ==Boundary class (view) for presenting something to user only !==
+  ==Control class (controller) for verifying inputs and interacting with entity class!==
+ ==Entity Class (model) for doing something that we really want==
+ ==User 的部分==
+ ==Forward pass使用实线==
+ ==Back pass 使用虚线==

How to refine the scenario and use it to show the  interactions between objects 如何细化场景并使用它来显示对象之间的交互
+ Use the information from the class diagram   使用类图中的信息
+ Then, add boundary and control class  添加边界和控制类
+  If required, you can add more arrows to show inner working of  the system  您可以添加更多箭头以显示系统的内部工作
+ Add as much of information as possible 添加尽可能多的信息

![](pic/Pasted%20image%2020221028204434.png)
![](pic/Pasted%20image%2020221028202912.png)
+ Message sent from a Class A object to a  Class B object corresponds to a method in  Class B 从 A 类对象发送到 B 类对象的消息对应于 B 类中的一个方法
+ Actor interacts with the system via  UserInterface obj (boundary class view) Actor 通过 UserInterface 与系统交互
+ there are 8 actions sent by the Actor into the system. Therefore, in the sequence diagram, there must be exactly 8 messages sent to the Boundary classes Actor 向系统发送了 8 个动作。因此，在序列图中，必须恰好有 8 条消息发送到 Boundary 类
+ Boundary classes interacts with the  entities via control object(s) 边界类通过控制对象与实体交互
+ user's input will be verified in controller  

## ==重点选考UML state chart==
==动态建模，使用特定场景的状态图对对象的行为进行建模==
+ 起点黑圆圈 终点黑圆圈套一个同心圆环
+ 不用跨级返回循环
+ 可以画登录 没时间的话从mainpage开始画
+ 起始点->各个state->state之间过程、操作->终止点
+ ![](pic/Pasted%20image%2020221028220044.png) 当前界面用户可以看见什么内容 主要功能选项 可不写


https://sparxsystems.com/resources/tutorials/uml2/state-diagram.html
![](pic/Pasted%20image%2020221028210257.png)
![](pic/Pasted%20image%2020221028210514.png)
![](pic/Pasted%20image%2020221028210751.png)
![](pic/Pasted%20image%2020221028210944.png)

Scenario
> The door can be in one of three states: "Opened", "Closed" or "Locked". It can respond to the events Open, Close, Lock and Unlock. Notice that not all events are valid in all states; for example, if a door is opened, you cannot lock it until you close it. Also notice that a state transition can have a guard condition attached: if the door is Opened, it can only respond to the Close event if the condition doorWay->isEmpty is fulfilled门可以处于以下三种状态之一：“打开”、“关闭”或“锁定”。它可以响应打开、关闭、锁定和解锁事件。请注意，并非所有事件在所有状态下都有效；例如，如果一扇门是打开的，在您关闭它之前您无法锁定它。另请注意，状态转换可以附加一个警戒条件：如果门已打开，则只有在满足 doorWay->isEmpty 条件时才能响应关闭事件
> ![](pic/Pasted%20image%2020221028210134.png)

![](pic/Pasted%20image%2020221028210700.png)
![](pic/Pasted%20image%2020221028210711.png)
![](pic/Pasted%20image%2020221028210720.png)


# WEEK 6
## WEEKLY QUIZ

content in  week6 FLUX.pdf
![](pic/week6FLUX.pdf)



# WEEK 7
## WEEKLY QUIZ
![](pic/Pasted%20image%2020220911153012.png)
![](pic/Pasted%20image%2020220911153036.png)
![](pic/Pasted%20image%2020220911153048.png)

# WEEK 8 SE Code of Ethics  

## WEEKLY QUIZ
![](pic/Pasted%20image%2020220917130031.png)
![](pic/Pasted%20image%2020220917130052.png)
![](pic/Pasted%20image%2020220917130108.png)


# WEEK 10
## WEEKLY QUIZ
![](pic/Pasted%20image%2020221009165146.png)
![](pic/Pasted%20image%2020221009165157.png)

# WEEK 12
## WEEKLY QUIZ
![](pic/Pasted%20image%2020221023200704.png)
![](pic/Pasted%20image%2020221023200727.png)

# Exam note
+ 尽管部分开卷考试， 但是基本没时间看书！ （提前复习很重要）
+ 考试时间： 2小时10分钟
+ 需要用笔画图， 因此带好铅笔和橡皮
+ 题目类型：
1. Ass1
2. Ass2 （initial class + sequence class + state (或者unified process or UML use case diagram)）
3. Ass4
4. Ass5
5. 没有Programming 题目，没有 ER-digram for class diagram
6. 除了作业相关的题目，可能还有10分以内的非作业内容，比如说IP等


# Sample exam and question
check Extra%20questions%20(1).pdf
check SampleExamQuestions.pdf
check pic/SampleSolutions.pdf

# Extra exercise

![](pic/Pasted%20image%2020221028221618.png)
## 1. functional requirement select some function and write down: [Functional requirements](#Functional%20requirements) 
+ download photo
+ system read photo
+ tag
+ upload
+ watermark

## 2. Non functional requirement:[Non-functional requirements](#Non-functional%20requirements)
+ colour theme can be switch for easier reading
+ API linked  to system
+ flag design icon to show different options
+ system accept file type


## 3. User story [==必考User stories==](#==必考User%20stories==)
+ 功能性需求选择来写
+ as a staff, i want to add a watermark so that user can identify their photo
+ as a user, i want to upload photo to the cloud so that i can view the photo in different device anywhere anytime


## 4. Acceptance criteria [==必考Acceptance criteria==](#==必考Acceptance%20criteria==)

>  as a staff, i want to add a watermark so that user can identify their photo

 Acceptance criteria 1 
+ desktop system select click choose page
+ staff login
+ staff choose photos on XX page, 
+ add watermark
+ confirm and response within 2 second

> as a user, i want to upload photo to the cloud so that i can view the photo in different device anywhere anytime

 Acceptance criteria 2
+ d

## 5. Initial class diagram 20pts [==重点Initial Class Diagram==](#==重点Initial%20Class%20Diagram==)
+ desktop user client staff system
+ ![](pic/Pasted%20image%2020221029115600.png)
+ api
+ ![](pic/Pasted%20image%2020221029115736.png)

![](pic/Pasted%20image%2020221029122046.png)

[My Initial class diagram in lucidchart](https://lucid.app/lucidchart/a4026035-3501-4a58-bd72-e21ef3b3d8c3/edit?viewport_loc=-324%2C159%2C2281%2C1036%2C0_0&invitationId=inv_3d939728-1cf9-48da-8b9b-8975c434fd64
)

## 6. Sequence diagram 20 pts [==重点Sequence diagram==](#==重点Sequence%20diagram==)
![](pic/Pasted%20image%2020221029124320.png)
![](pic/Pasted%20image%2020221029150951.png)
