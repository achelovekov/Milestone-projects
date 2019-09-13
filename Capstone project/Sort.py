class Sort():
	def bubbleSortRecN(A, n):
		if n == 1:
			return A
		i = 0
		for i in range(len(A)-1):
	   		if(A[i] > A[i+1]):
		   		A[i],A[i+1] = A[i+1],A[i]

		return Sort.bubbleSortRecN(A,n-1)

	def bubbleSortRecSwap(A):
		step = 0
		while step < len(A) - 1:
			i = 0
			while i in range(len(A) - 1):
				if(A[i]>A[i+1]):
				  A[i],A[i+1] = A[i+1],A[i]
				i+=1
			step += 1
		return A

	def bubbleSortRecInsert(B,A):
		A = Sort.bubbleSortRecSwap(A)
		B[:len(B)-1] = A
		return Sort.bubbleSortRecSwap(B)

	def bubbleSortRec(Arr):
		if len(Arr) > 1:
			sub = Arr[:len(Arr)-1]
			Sort.bubbleSortRec(sub)
			Sort.bubbleSortRecInsert(Arr,sub)

	def mergeSortMerge(A,l,r):
		i = j = k = 0
		while i<len(l) and j<len(r):
			if l[i] < r[j]:
				A[k] = l[i]
				i+=1
				k+=1
			else:
				A[k] = r[j]
				j+=1
				k+=1

		while i<len(l):
				A[k] = l[i]
				i+=1
				k+=1

		while j<len(r):
				A[k] = r[j]
				j+=1
				k+=1

	def mergeSortRec(A):
		if len(A) > 1: 
			m = len(A) // 2
			l = A[:m]
			r = A[m:]
			Sort.mergeSortRec(l) 
			Sort.mergeSortRec(r)
			Sort.mergeSortMerge(A,l,r)