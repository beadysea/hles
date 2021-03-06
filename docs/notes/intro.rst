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

================  =====  =====
Column weight ->  2's    1's  
----------------  -----  -----
decimal value     bit 1  bit 0
================  =====  =====
0                 0      0    
1                 0      1    
2                 1      0    
3                 1      1    
================  =====  =====

Extending this idea to 8 columns or 8 bits gives us the first real bit width used by
early microprocessors. 8 bits is referred to as a **byte** and with this width a processor 
can count and store binary numbers representing decimal 0 to 255. At first this may seem pretty 
pointless however start bolting bytes together then you can represent any number provided you have
enough bytes of memory to store it.

+-----------+----------+
| High Byte | Low Byte |   
+-----------+----------+

A 16 bit word capable of storing numbers 0 to 65,535

=========  ========  =========  ========
High Word            Low Word
-------------------  -------------------
High Byte  Low Byte  High Byte  Low Byte
=========  ========  =========  ========

32 bit word ( 0 to 4,294,967,295 )


So far we have touched on a few important ideas fundamental to how we write software today. 
First is that computers store information as binary numbers. We can think of a bit as the most 
primitive type of data. The idea of extensibility will be important as we continue to develop
our software writing skills. In the above discussion we saw extensibility in action when we 
extended size of data from bit to byte, then to 16 bit or 2byte Word and 32 bit or quad byte Word.

We've also touched on the idea of abstraction when we assigned the value of 0 to the more abstract
notion of OFF and the value 1 to the more abstract notion of ON. 
