"""
Without using any string methods, try to print the following:
123...N

Note that "..." represents the values in between."""

if __name__ == '__main__':
    n = int(input())
    num=0
    
    for i in range(n+1):
        num*=10
        num+=i
    print(num)
