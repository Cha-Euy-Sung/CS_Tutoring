# About HW. 
# hawkidN.py
# numbers 0-4


#------------------------------------------------
# [Comprehensions]

# The genral form of a simple list comprehension is :

#       [ expression(x) for x in sequence ]

# Where sequence can be any of ther sequence type (list,tuples, strings, ranges) as well as sets.


# More complx comprehensions, with filltering statements and nested iterative consturcts are also possible:

#         [ expression(x,y) for x in sequence1 for y in sequence2 ... if condition(x,y) ]


# for example : 


#    [ (x, y) for x in range(3) for y in range(3) if x != y]
#    [(0,1), (0,2), (1,0), (1,2,), (2,0), (2,1)]

#---------------------------------------------------------------------------------

# {x+y for x in range(3) for y in range(3) }   = type: set
# ��ġ�°� �˾Ƽ� ������
# >>> {0,1,2,3,4}

# {x:y for x in range(3) for y in range(3) if x !=y }      = type : dictionary
# {0:2, 1:2, 2:1 }     # Ű�� (element)�� 3���� ������, ��ųʸ��� ������ Ű �� �������� ������. (ex. x=0 �϶�, ������ ���� 1,2 ������ 2�� �������̶�, {0:2}��


# [ x.upper() for x in "testing" ]
# >>> ['T', 'E', 'S', 'T','I', 'N', 'G']


# ''.join([x.upper() for x in "testing"])
# >>> 'TESTING'


# string.join(L) uses string to paste together elements of L
# ** careful! order metters:
# >>> '-+-'.join({str(x) for x in range(5)})
# >>> '0-+-1-+-3-+-2-+-4' 
# set�� �������ĵ� ���°� �ƴϰ�, ����ȰŸ� ����� ������, ������ ���ĵ��� ���� ���� ����. �Է�Ƽ ����

#-----------------------------------------------------------------------------------------------------------


# TUPLE

# (x+1 for x in range(1000000))
# >>> <generator object <genexpr> at 0x7ff39ld35990>


# Function

# In addition to a rich set of data types, python, like other languages, comes with a rich sset of built in functions -- and mudules

# Fundamental to the notion of prgramming, however, is the ability to extend the lanuage by writing your own function.

# 'def' is used to define initate a function definition. The syntax is :


# def fname(argument list):
# <boy of definition, indented>

# ** indent : �߿��� �ܾ� 

# �̰� �ѹ� �غ��� def foo(x=0,y=0):
# return x+y
# >>> foo(3)


# -------------------------------------------------------------


# Example :

# Write a function create() that takes three inputs, l,e, and t, where l represents the length, e represents the datum, and t is a Bollean indicating the type of the returned value.

# The function should return a lists (if t is True, the default) or a tuple (if t is False) consisiting of l copies (default is 0) of e (default is 'foo')


#  you will need 



def create(l=0, e='foo', t=True):
    r=[e for i in range(l)]
    if not t :
        r = tuple(r)
    return(r)

print(create(l=5))
