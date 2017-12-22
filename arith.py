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
# https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
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


# P35 Determine the prime factors of a given positive integer. (To be improved)
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


# P36 Determine the prime factors of a given positive integer
def primeFactorsMult(num):
	primeFactorsList = primeFactors(num)
	packList = pack(primeFactorsList)
	newList = []

	for item in packList:
		length = len(item)
		l = (item[0], length)
		newList.append(l)

	return newList

# P39 A list of prime numbers.
# Given a range of integers by its lower and upper limit, construct a list of all prime numbers in that range.
def isPrimeInterval(x, y):
	newList = []
	for i in range(x, y+1):
		if isPrime(i):
			newList.append(i)
	return newList


if __name__ == "__main__":
	number = 100
	print("isPrime " + str(number) + ": " + str(isPrime(number)))
	print("\n")

	n = 100
	z = 50
	print("gcd " + str(n) + " " + str(z) + ": " + str(gcd(n,z)))
	print("\n")

	z = 8
	print("phi " + str(z) + ": " + str(phi(z)))
	print("\n")

	z = 315
	print("primeFactors " + str(z) + ": " + str(primeFactors(z)))
	print("\n")

	z = 315
	print("primeFactorsMult " + str(z) + ": " + str(primeFactorsMult(z)))
	print("\n")

	n = 100
	z = 215
	print("isPrimeInterval " + str(n) + " " + str(z) + ": " + str(isPrimeInterval(n,z)))
	print("\n")