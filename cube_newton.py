n=input('Enter a number ')
x0=0.3*n
err=0.00000000001
while(abs((x0**3)-n)>err):
	fx=(x0**3)-n
	dfx=3*(x0**2)
	x0=x0-(fx/dfx)
print 'Cube root: ',x0
