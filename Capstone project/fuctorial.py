def fuctorial_rec(n):
	if n == 2:
		return 2
	return n*fuctorial_rec(n-1)

def fuctorial_loop(n):
    res = n
    while n >=2 :
        res = res*(n-1)
        n-=1
    return res

print(fuctorial_loop(100))
print(fuctorial_rec(100))