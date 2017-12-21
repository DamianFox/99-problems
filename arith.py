#!/usr/bin/env python3

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
    else:2
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




if __name__ == "__main__":
	number = 100
	print("isPrime " + str(number) + ": " + str(isPrime(number)))
	print("\n")

	n = 100
	z = 50
	print("gcd " + str(n) + " " + str(z) + ": " + str(gcd(n,z)))
	print("\n")