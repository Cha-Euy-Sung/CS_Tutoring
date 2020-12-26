#!/usr/bin/python3
# Alberto Maria Segre
#
# Copyright 2015, The University of Iowa.  All rights reserved.
# Permission is hereby given to use and reproduce this software 
# for non-profit educational purposes only.

# Let L be a list of nonnegative integers, where min is the smallest
# element and max is the largest element. Write an expression that
# specifies a new tuple consisting of max copies of min followed by
# min copies of max.
#L=[1, 3, 5, 4, 4, 6, 2]
(min(L),)*max(L) + (max(L),)*min(L)
