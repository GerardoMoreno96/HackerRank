"""Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given  scores. 
Store them in a list and find the score of the runner-up."""

import sys

if __name__ == '__main__':
    # n = int(input())
    # arr = map(int, input().split())
    arr = [2,3,6,6,5]
    first = -99999999
    second = 0
    for i in arr:
        if i > first:
            second = first
            first = i
        elif i > second and i!=first:
            second = i
    print(second)
