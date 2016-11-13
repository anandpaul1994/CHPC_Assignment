x=input('Enter the number ')
epsilon=0.0000000001
low =0.0
high = max(1.0,x)
mid = (high+low)/ 2.0
while abs(mid**3 -x)>= epsilon:
    if mid**3 <= x:
        low= mid
    else:
        high= mid
    mid = (high+low)/2.0
print 'The cube root is', mid
