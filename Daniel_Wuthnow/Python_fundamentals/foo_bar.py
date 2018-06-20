def isPrime(n):
	if n%2==0:
		return False
	k = 3
	while k*k <= n:
		if n % k ==0:
			return False
		k+=2
	return True


def isSquare(x):
	ans = 0
	while ans*ans < x:
		ans += 1
	if ans*ans != x:
		# print str(x)+" is not square"
		return False
	else:
		# print str(x)+" is square"
		return True



for i in range(100,100000):
	
	if isPrime(i):
		print str(i)+"Foo"
	elif isSquare(i):
		print str(i)+"Bar"
	else:
		print str(i) + "FooBar"	


