# Accessing and Manipulating Time in ModelE / ModelE中的时间访问与操作

---

Tracking the evolution of time is an essential aspect of the model infrastructure, and it is relied upon to control the activation of a variety of physical processes and diagnostics.
跟踪时间的演化是模型基础设施的一个重要方面，它被用于控制各种物理过程和诊断输出的激活。

With the introduction of the requirement to support planets other than Earth including different orbital parameters (i.e. different calendar properties), it was essential to improve the encapsulation of time management to ensure consistent treatment.
随着引入支持地球以外行星（包括不同的轨道参数，即不同的日历属性）的要求，必须改进时间管理的封装以确保一致的处理。

---

## Typical Usage / 典型用法

Most model developers should only need to know how to access certain time-related quantities such as hour, day, month, year, etc.
大多数模型开发者只需要知道如何访问某些时间相关的量，如小时、日、月、年等。

Originally these were provided through a set of public module variables (integers) in MODEL_COM.
最初，这些是通过MODEL_COM中的一组公共模块变量（整数）提供的。

However, in the new implementation, a single module variable, ModelEClock should be used for access any information about the current time in the model.
然而，在新实现中，应使用单个模块变量ModelEClock来访问模型中当前时间的任何信息。

The details of how this works will be presented later, but generally access appears in the following forms:
其工作原理的细节将在后面介绍，但通常访问形式如下：

```fortran
year = modelEclock%getYear()     ! integer
month = modelEclock%getMonth()   ! integer
abbrev = modelEclock%getAbbrev() ! character(...)
day = modelEclock%getDayOfYear() ! integer
date = modelEclock%getDate()     ! integer
hour = modelEclock%getHour()     ! integer
```

If multiple items are needed there is also a subroutine call:
如果需要多个项目，还有一个子程序调用：

```fortran
call modelEclock%get(year=year, month=month, ...)
```

All arguments are optional - keywords are required.
所有参数都是可选的——关键字是必需的。

---

Another convenient interface is to check to see if this this is the first timestep in a new day:
另一个方便的接口是检查这是否是新的一天中的第一个时间步：

```fortran
if (modelEclock%isBeginningOfDay()) then
  ...
end if
```

In the future there may be separate clock objects inside some model components.
将来，某些模型组件内部可能有独立的时钟对象。

Such clocks could be used to manage subcycling and other esoteric purposes.
此类时钟可用于管理子循环和其他特殊用途。

---

## Implementation Details / 实现细节

The time management facility is constructed with a number of interacting classes.
时间管理设施由多个相互交互的类构成。

Those with little experience with object-oriented programming may find some of the terminology and design somewhat difficult to follow.
那些对面向对象编程经验较少的人可能会觉得某些术语和设计有些难以理解。

The major classes and their primary responsibilities are as follows:
主要的类及其主要职责如下：（原文拼写：repsonsibilities）

---

### Rational / 有理数

This class implements a rational number of the form (w + n/d) where {w,n,d} are all 8-byte integers.
此类实现形式为(w + n/d)的有理数，其中{w,n,d}都是8字节整数。

### BaseTime / 基准时间

BaseTime objects contain time since some arbitrary epoch, measured in seconds.
BaseTime对象包含自某个任意纪元以来的时间，以秒为单位测量。

BaseTime is a subclass (i.e. it extends) Rational and is the fundamental representation of time in the model.
BaseTime是Rational的子类（即它扩展了Rational），是模型中时间的基本表示。

The choice of Rational rather than floating point is not immediately obvious, but stems from the requirement to ensure that questions such as "What day is it?" have well-defined answers even on time boundaries.
选择有理数而不是浮点数乍看之下不太明显，但源于确保诸如"今天是哪一天？"之类的问题即使在时间边界上也有明确定义答案的要求。

### AbstractCalendar / 抽象日历

This base class is used to relate BaseTime objects (i.e. raw seconds) to more useful time units such as hour, day, month, etc.
此基类用于将BaseTime对象（即原始秒数）与更有用的时间单位（如小时、日、月等）关联起来。

Multiple subclasses of AbstractCalendar have been implemented to support the original pseudo-Julian calendar as well as configurable calendars suitable for exoplanets.
已实现AbstractCalendar的多个子类，以支持原始的伪儒略历以及适用于系外行星的可配置日历。

(See other document on Orbits and Calendars.)
（参见关于轨道和日历的其他文档。）

### Time / 时间

This class extends BaseTime, but includes a calendar component.
此类扩展了BaseTime，但包含一个日历组件。

Time objects can therefore be queried for hour, month, etc.
因此可以查询Time对象的小时、月份等信息。

One can think of it as a BaseTime plus an interpretation for ease-of-use.
可以将其理解为BaseTime加上一种便于使用的解释。

### TimeInterval / 时间间隔

This class represents the amount of time that between two events.
此类表示两个事件之间的时间量。

This class is not yet used in the model, but may eventually support so-called "alarms" for periodic processes.
此类在模型中尚未使用，但最终可能支持所谓的"警报"用于周期性过程。

### ModelClock / 模型时钟

This class combines a Time object (currentTime) and a BaseTime object (dt).
此类结合了一个Time对象（currentTime）和一个BaseTime对象（dt）。（原文拼写：currenTime）

ModelEClock is an object of this time, and as mentioned in the introduction, serves as the main interface for all time management during the simulation.
ModelEClock是此类的对象，如介绍中所述，它作为模拟期间所有时间管理的主要接口。

All queries (e.g. hour, day, month, etc) are relayed to the currentTime component, and time is advanced through calls to the nextTick() method.
所有查询（如小时、日、月等）都被传递给currentTime组件，时间通过调用nextTick()方法推进。

---

**注：原文中存在三处拼写错误；译文已更正并在对应中文行中标注（原文拼写：...）以保留可追溯性。**
- "repsonsibilities" → "responsibilities"
- "AbsractCalendar" → "AbstractCalendar"
- "currenTime" → "currentTime"

---

**Document End / 文档结束**
