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
		if(i == n-1):
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
	return list == newList

# P07 Flatten a nested list structure.
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
def encodeDirect(encodeDirectList):
	newList = []
	currentList = []
	current = encodeDirectList[0]
	counter = 1
	for i in range(1,length(encodeDirectList)):

		if((encodeDirectList[i] == current) and (i == (length(encodeDirectList)-1))):
			counter += 1
			item = (counter, current)
			newList.append(item)

		elif((encodeDirectList[i] != current) and (i == (length(encodeDirectList)-1))):
			item = (counter, current)
			newList.append(item)
			counter = 1
			item = (counter, encodeDirectList[i])
			newList.append(item)

		elif(current != encodeDirectList[i-2] and current != encodeDirectList[i]):
			item = (1, current)
			newList.append(current)
			current = encodeDirectList[i]

		elif(current == encodeDirectList[i-2] and current != encodeDirectList[i]):
			item = (counter, current)
			newList.append(item)
			current = encodeDirectList[i]
			counter = 1

		elif(encodeDirectList[i] == current):
			counter += 1

	return newList


# P14 Duplicate the elements of a list.
def dupli(dupliList):
	newList = []
	encodeList = encode(dupliList)
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


# P16 Drop every N'th element from a list.
def drop(dropList, n):
	itemsToRemove = []
	for i in range(len(dropList)):
		if ((i == n) or (i % n == 0 and i != 1 and i != 0)):
			itemsToRemove.append(dropList[i-1])

	for i in range(len(itemsToRemove)):
	 	dropList.remove(itemsToRemove[i])

	return dropList


# P17 Split a list into two parts; the length of the first part is given.
def split(splitList, n):
	newSplitList = []
	i = 0
	while(i<n):
		newSplitList.append(splitList[0])
		splitList.pop(0)
		i += 1
			
	return [newSplitList, splitList]


# P17 Split a list into two parts; the length of the first part is given.
def split1(splitList, n):
	return [splitList[:n], splitList[n:]]


# P18 Extract a slice from a list.
def slice(sliceList, min, max):
	newSliceList = []
	for i in range(len(sliceList)):
		if(i>=min-1 and i<max):
			newSliceList.append(sliceList[i])
	return newSliceList


# P18 Extract a slice from a list.
def slice1(sliceList, min, max):
	return sliceList[min-1:max]


# P19 Rotate a list N places to the left.
def rotate(rotateList, num):
	return rotateList[num:]+rotateList[0:num]


# P20 Remove the K'th element from a list.
def removeAt(removeAtList, num):
	del removeAtList[num-1]
	return removeAtList


# P21 Insert an element at a given position into a list.
def insertAt(item, list, num):
	return list[:num-1]+[item]+list[num-1:]


if __name__ == "__main__":
	myList = ['a', 'b', 'c', 'd']
	myList1 = ['a', ['b', ['c', 'd'], 'e'], 'f']
	myList2 = ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']
	myList3 = ['a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd']
	myList4 = ['a', 'b', 'c']
	myList5 = [(4, 'a'), 'b', (2, 'c'), (2, 'a'), 'd', (4, 'e')]
	myList6 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k']
	myList7 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k']
	myList8 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k']
	myList9 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

	assert myLast(['a', 'b', 'c', 'd']) == 'd'

	assert myButLast(['a', 'b', 'c', 'd']) == 'c'

	assert elementAt(['a', 'b', 'c', 'd'], 3) == 'c'

	assert length(['a', 'b', 'c', 'd']) == 4

	assert reverse(['a', 'b', 'c', 'd']) == ['d', 'c', 'b', 'a']

	assert palindrome(['a', 'b', 'c', 'd']) == False

	assert flatten(['a', ['b', ['c', 'd'], 'e'], 'f']) == ['a', 'b', 'c', 'd', 'e', 'f']

	assert compress(myList2) == ['a', 'b', 'c', 'a', 'd', 'e']

	assert pack(myList2) == [['a', 'a', 'a', 'a'], ['b'], ['c', 'c'], ['a', 'a'], ['d'], ['e', 'e', 'e', 'e']]

	assert encode(myList2) == [(4, 'a'), (1, 'b'), (2, 'c'), (2, 'a'), (1, 'd'), (4, 'e')]

	assert encodeModified(myList2) == [(4, 'a'), 'b', (2, 'c'), (2, 'a'), 'd', (4, 'e')]

	assert decode(myList5) == ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']

	assert encodeDirect(myList2) == [(4, 'a'), 'b', (2, 'c'), (2, 'a'), 'd', (4, 'e')]

	assert dupli(myList3) == ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd']

	assert repli(myList4, 3) == ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']

	assert drop(myList6, 3) == ['a', 'b', 'd', 'e', 'g', 'h', 'k']

	assert split(myList7, 3) == [['a', 'b', 'c'], ['d', 'e', 'f', 'g', 'h', 'i', 'k']]

	assert slice(myList8, 3, 7) == ['c', 'd', 'e', 'f', 'g']

	assert rotate(myList9, 3) == ['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']

	assert removeAt(myList, 2) == ['a', 'c', 'd']

	myList = ['a', 'b', 'c', 'd']
	
	assert insertAt('alfa', myList, 2) == ['a', 'alfa', 'b', 'c', 'd']


