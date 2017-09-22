#!/usr/bin/env python3
from itertools import groupby


# P01 Find the last box of a list.
def myLast(list):
	return list[-1]


# P02 Find the last but one box of a list.
def myButLast(list):
	return list[-2]


# P03 Find the K'th element of a list.
def elementAt(list, n):
	for i in range(length(list)):
		if(i == n):
			return list[i]


# P04 Find the number of elements of a list (without built-in function).
def length(list):
	counter = 0
	for char in list:
		counter += 1
	return counter


# P05 Reverse a list.
def reverse(list):
	newList = []
	l = length(list)
	for i in range(l):
		newList.append(list[l-(i+1)])

	return newList


# P06 Find out whether a list is a palindrome.
def palindrome(list):
	newList = reverse(list)
	if(list == newList):
		return True
	else:
		return False

# P07 Flatten a nested list structure. (To be fixed)
def flatten(l):
	nList = myFlatten(l, [])
	return nList

def myFlatten(l, newList):
	if not l:
		return list(newList)
	else:
		item = l[0]
		others = l[1:]
		l.pop(0)
		if isinstance(item, list):
			return myFlatten(item+others, newList)
		else:
			newList.append(item)
			return myFlatten(l, newList)

'''
def flatten(nestedList):
    def aux(listOrItem):
        if isinstance(listOrItem, list):
            for elem in listOrItem:
                for item in aux(elem):
                    yield item
        else:
            yield listOrItem
    return list(aux(nestedList))
'''

# P08 Eliminate consecutive duplicates of list elements.
def compress(list):
	newList = []
	current = list[0]
	newList.append(current)
	for i in range(1,length(list)):
		if(list[i] != current):
			newList.append(list[i])
			current = list[i]

	return newList


# P09 Pack consecutive duplicates of list elements into sublists without built-in.
def pack(list):
	newList = []
	currentList = []
	current = list[0]
	for i in range(1,length(list)):

		if((list[i] == current) and (i == (length(list)-1))):
			currentList.append(current)
			currentList.append(current)
			newList.append(currentList)

		elif((list[i] != current) and (i == (length(list)-1))):
			currentList.append(current)
			newList.append(currentList)
			currentList = []
			currentList.append(list[i])
			newList.append(currentList)

		elif(current != list[i-2] and current != list[i]):
			currentList.append(current)
			newList.append(currentList)
			currentList = []
			current = list[i]

		elif(current == list[i-2] and current != list[i]):
			currentList.append(current)
			newList.append(currentList)
			currentList = []
			current = list[i]

		elif(list[i] == current):
			currentList.append(current)

	return newList


# P09 Pack consecutive duplicates of list elements into sublists.
def pack1(l):
	newList = []
	for k, g in groupby(l):
		newList.append(list(g))

	return newList

# P10 Run-length encoding of a list.
def encode(list):
	packList = pack(list)
	newList = []
	for item in packList:
		len = length(item)
		l = (len, item[0])
		newList.append(l)

	return newList

# P11 Modified run-length encoding.
def encodeModified(list):
	packList = pack(list)
	newList = []
	for item in packList:
		len = length(item)
		if(len == 1):
			l = item[0]
		else:
			l = (len, item[0])
		
		newList.append(l)

	return newList

# P12 Decode a run-length encoded list.
def decode(list):
	newList = []
	encodeList = encodeModified(list)
	for item in encodeList:
		if isinstance(item[0], int):
			for i in range(0, item[0]):
				newList.append(item[1])
		else:
			newList.append(item[0])

	return newList

# P13 Run-length encoding of a list (direct solution).
def encodeDirect(list):
	newList = []
	currentList = []
	current = list[0]
	counter = 1
	for i in range(1,length(list)):

		if((list[i] == current) and (i == (length(list)-1))):
			counter += 1
			item = (counter, current)
			newList.append(item)

		elif((list[i] != current) and (i == (length(list)-1))):
			item = (counter, current)
			newList.append(item)
			counter = 1
			item = (counter, list[i])
			newList.append(item)

		elif(current != list[i-2] and current != list[i]):
			item = (1, current)
			newList.append(current)
			current = list[i]

		elif(current == list[i-2] and current != list[i]):
			item = (counter, current)
			newList.append(item)
			current = list[i]
			counter = 1

		elif(list[i] == current):
			counter += 1

	return newList


# P14 Duplicate the elements of a list.
def dupli(list):
	newList = []
	encodeList = encode(list)
	for n,l in encodeList:
		for i in range(n*2):
			newList.append(l)

	return newList


# P15 Replicate the elements of a list a given number of times.
def repli(list, n):
	newList = []
	encodeList = encode(list)
	for l in list:
		for i in range(n):
			newList.append(l)

	return newList

if __name__ == "__main__":
	myList = ['a', 'b', 'c', 'd']
	print(myList)
	print("myLast: " + myLast(myList))
	print("\n")

	print(myList)
	print("myButLast: " + myButLast(myList))
	print("\n")

	print(myList)
	print("elementAt 3: " + elementAt(myList, 3))
	print("\n")

	print(myList)
	print("length: " + str(length(myList)))
	print("\n")

	print(myList)
	print("reverse: " + str(reverse(myList)))
	print("\n")

	print(myList)
	print("palindrome: " + str(palindrome(myList)))
	print("\n")

	myList = ['a', ['b', ['c', 'd'], 'e'], 'f']
	print(myList)
	print("flatten: " + str(flatten(myList)))
	print("\n")

	myList = ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']
	print(myList)
	print("pack: " + str(pack(myList)))
	print("\n")

	print(myList)
	print("encode: " + str(encode(myList)))
	print("\n")

	print(myList)
	print("encodeModified: " + str(encodeModified(myList)))
	print("\n")

	print(myList)
	print("decode: " + str(decode(myList)))
	print("\n")

	print(myList)
	print("encodeDirect: " + str(encodeDirect(myList)))
	print("\n")

	myList = ['a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd']
	print(myList)
	print("dupli: " + str(dupli(myList)))
	print("\n")

	myList = ['a', 'b', 'c']
	print(myList)
	print("repli with 3: " + str(repli(myList, 3)))
	print("\n")








