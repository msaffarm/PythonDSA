primeList = [2] # list of all prime numbers upto n
n = int(input("Insert N:\t"))
isPrime = False
for num in range(2,n+1):
	if all((bool(num%p) for p in primeList)):# use generator instead of list comprehension=> much faster
		primeList.append(num)
print(primeList)
