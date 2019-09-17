def sumRec(A):
	res = 0

	for i in A:
		if type(i) == list:
			res += sumRec(i)
		else:
			res += i

	return res

A=[1,[2,3],[[[[[4,5],[6,7]]]]]]
print(sumRec(A))




