#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_s = 0
    sum_w = 0
    if my_list:
        for pair in my_list:
            sum_s += pair[0] * pair[1]
            sum_w += pair[1]
        return sum_s/sum_w
    return 0
