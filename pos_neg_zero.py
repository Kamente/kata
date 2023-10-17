import math
import os
import random
import re
import sys


def plusMinus(arr):
    arr_len = len(arr)
    pos_count = 0
    neg_count = 0
    zero_count = 0

    for i in range(arr_len):
        if arr[i] > 0:
            pos_count += 1
        elif arr[i] < 0:
            neg_count += 1
        else:
            zero_count += 1


print(f"{pos_count}/{arr_len}")


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
