#generates one value at a time, not the whole list.
#func(num) - yields one value from the num range 
def count_primes(num):
    for i in range(2,num+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            yield i