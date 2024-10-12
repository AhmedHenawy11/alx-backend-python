#!/usr/bin/env python3
"""Write a type-annotated function sum_mixed_list which takes a list
mxd_lst of integers and floats and returns their sum as a float.
"""

import typing


def sum_list(input_list: typing.List[typing.Union[int, float]]) -> float:
    '''returns their sum as a float
    '''
    return float(sum(input_list))
