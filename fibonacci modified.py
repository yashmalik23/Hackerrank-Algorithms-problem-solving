import sys

def fibonacciModified(t1, t2, n):
    a=[]
    a.append(t1)
    a.append(t2)
    for i in range(2,n):
        a.append(a[i-2]+a[i-1]*a[i-1]) 
    return a[n-1]

if __name__ == "__main__":
    t1, t2, n = input().strip().split(' ')
    t1, t2, n = [int(t1), int(t2), int(n)]
    result = fibonacciModified(t1, t2, n)
    print(result)
