"""
Without using any string methods, try to print the following:
123...N

Note that "..." represents the values in between."""

if __name__ == '__main__':
    n = int(input())
    num=0
    count=0
    for i in range(n+1):
        numReplica=i
        while(numReplica>=1): 
            count+=1
            numReplica = numReplica/10
        num*=(pow(10,count))
        num+=i
        count=0
    print(num)
