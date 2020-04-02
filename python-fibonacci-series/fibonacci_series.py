def non_recur_fibo(n):
	curr = 0
	prev = 1
	lastprev = 0
	series = '0 1'
	
	for i in range(2, n):
		curr = prev + lastprev
		series += ' ' + str(curr)
		lastprev = prev
		prev = curr

	return series

def recur_fibo(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return recur_fibo(n - 1) + recur_fibo(n - 2)

n=int(input("Enter the terms: "))

print('Number of fibonacci terms in a series', n)

print('Series (non-recursive): ', non_recur_fibo(n))

print('Series (recursive): ', end = '')
for i in range(n):
	print(str(recur_fibo(i)) + ' ', end = '')