Introduction
============

The aim of this course is to introduce you to the process of writing software designed to
solve engineering problems. While based on the requirements of the SQA unit of the same name,   
the approach taken in this course is..



Basic machine architecture
==========================

Before we dive into the world of high level software, let's think about how a computer works.
What does it really do, down at the silicon level?

Well every modern computing device - your phone, laptop, tablet, tv etc works on the principle of
a transistor switch having two possible states - ON or OFF. Let's represent **ON** with the value
**1** and **OFF** with the value **0** \.

We can now think of this single transistor as a device capable of storing a numerical value, 
a binary digit. We shorten **bi**\nary digi\ **t** to **bit**. So a single transistor can store
a **bit** of numerical information. A zero (0) or a (1).

Of course if we want to store a lot of information we are going to need more **bits**, 
billions and trillions of them for today's world, but let's no get ahead of ourselves. 
If we have two bits then we can start with the idea of counting using the same process we use in
decimal.

================  =====  =====  =========================
Column weight ->  2's    1's
================  =====  =====  =========================
decimal value     bit 1  bit 0
================  =====  =====  =========================
0                 0      0
1                 0      1      Can't count higher than 1
2                 1      0      so two represented by 1 0
3                 1      1
=======           =====  =====  ==========================

