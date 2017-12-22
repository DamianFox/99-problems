#!/usr/bin/env python3
from itertools import groupby

###################################
# P09 Pack consecutive duplicates of list elements into sublists.
def pack(l):
	newList = []
	for k, g in groupby(l):
		newList.append(list(g))

	return newList
###################################

# P31 Determine whether a given integer number is prime.
def isPrime(n):
	if n < 2:
		return False
	if n == 2:
		return True
	else:
		for i in range(2, n):
			if n % i == 0:
				return False
		return True


# P32 Determine the greatest common divisor of two positive integer numbers.
def gcd(x, y):
    if y > x:
        if y % x == 0:
            return x
        else:
            return gcd(y % x, x)
    else:
        if x % y == 0:
            return y
        else:
            return gcd(y, x % y)


# P33 Determine whether two positive integer numbers are coprime.
def coprime(x, y):
	if gcd(x, y) == 1:
		return True
	else:
		return False


# P34 Calculate Euler's totient function phi(m).
def phi(num):
	counter = 0
	for i in range(1, num+1):
		if coprime(i, num):
			counter += 1
	return counter


# P35 Determine the prime factors of a given positive integer.
def primeFactors(num):
	primeFactors = []

	if (isPrime(num)):
		primeFactors.append(n)
		return primeFactors

	for i in range(2, num):
		while (isPrime(i) and num % i == 0):
				primeFactors.append(i)
				num = num/i

	return primeFactors


# P36 Determine the prime factors of a given positive integer.
def primeFactorsMult(num):
	primeFactorsList = primeFactors(num)
	packList = pack(primeFactorsList)
	newList = []

	for item in packList:
		length = len(item)
		l = (item[0], length)
		newList.append(l)

	return newList


# P39 A list of prime numbers between a given range.
def isPrimeInterval(x, y):
	newList = []
	for i in range(x, y+1):
		if isPrime(i):
			newList.append(i)
	return newList


if __name__ == "__main__":

	assert isPrime(100) == False
	assert isPrime(7) == True

	assert gcd(36, 63) == 9

	assert coprime(35, 64) == True

	assert phi(10) == 4

	assert primeFactors(315) == [3, 3, 5, 7]

	assert primeFactorsMult(315) == [(3, 2), (5, 1), (7, 1)]

	assert isPrimeInterval(100, 170) == [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167]