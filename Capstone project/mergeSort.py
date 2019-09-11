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

def mergeSort(A):
	if len(A) > 1: 
		m = len(A) // 2
		l = A[:m]
		r = A[m:]
		mergeSort(l) 
		mergeSort(r)
		merge(A,l,r)


if __name__ == '__main__':
	A = [7,1,5,3,2,4,8,6,17,5,19,20,434,2]
	mergeSort(A)
	print(A)		


