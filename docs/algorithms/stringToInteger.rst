.. _String To Integer:

String To Integer
------------------


Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

     >>> '123a123'
     123
     >>> '+123'
     123

实现 ``C`` 语言中的 ``atoi`` 方法，转换字符串为整数。

**实现思路**
-----------

    1. 字串为空或者全是空格，返回0； 
    2. 字串的前缀空格需要忽略掉；
    3. 忽略掉前缀空格后，遇到的第一个字符，如果是‘+’或‘－’号，继续往后读；如果是数字，则开始处理数字；如果不是前面的2种，返回0；
    4. 处理数字的过程中，如果之后的字符非数字，就停止转换，返回当前值；
    5. 在上述处理过程中，如果转换出的值超出了int型的范围，就返回int的最大值或最小值。

**代码**
---------

    .. interalinclude:: ../../src/stringToInteger.py
        :language: python
        