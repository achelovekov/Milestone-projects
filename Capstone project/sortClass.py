import math

class Sort():
	def bubbleSortRecN(A, n):
		if n == 1:
			return A
		i = 0
		for i in range(len(A)-1):
	   		if(A[i] > A[i+1]):
		   		A[i],A[i+1] = A[i+1],A[i]

		return Sort.bubbleSortRecN(A,n-1)

	def bubbleSortRec(Arr):

		def swap(A):
			step = 0
			while step < len(A) - 1:
				i = 0
				while i in range(len(A) - 1):
					if(A[i]>A[i+1]):
					  A[i],A[i+1] = A[i+1],A[i]
					i+=1
				step += 1
			return A

		def insert_swap(B,A):
			A = swap(A)
			B[:len(B)-1] = A
			return swap(B)

		if len(Arr) > 1:
			sub = Arr[:len(Arr)-1]
			Sort.bubbleSortRec(sub)
			insert_swap(Arr,sub)

	def mergeSortRec(A):

		def merge(A,l,r):
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

		if len(A) > 1: 
			m = len(A) // 2
			l = A[:m]
			r = A[m:]
			Sort.mergeSortRec(l) 
			Sort.mergeSortRec(r)
			merge(A,l,r)

	def quickSortRec(A, left=0, right=None):

		def partition(A, left, right, pivot):

			while left <= right:
				while A[left] < pivot:
					left += 1
				while A[right] > pivot:
					right -= 1
				if left <= right:
					A[left],A[right] = A[right],A[left]
					left += 1
					right -= 1

			return left

		if right is None:
			right = len(A)-1

		if left >= right:
			return

		pivot = A[math.floor((left+right)/2)]

		index = partition(A,left,right,pivot)
		Sort.quickSortRec(A,left,index-1)
		Sort.quickSortRec(A,index,right)




