def worker(arr,key,libs,path):
    if key in path:
        print(f"Looped dependencies")
        return False
    else:
        path.append(key)
    for value in arr[key]:
        if value in arr.keys():
            worker(arr,value,libs,path)
        else:
            if value not in libs:
                libs.append(value)
            continue
    if key not in libs:
        libs.append(key)
        
def lib(arr,key=None):
    if key == None:
        key = random.choice(list(arr.keys()))
        
    libs=[]
    path=[]
    
    worker(arr,key,libs,path)
    
    return libs,path

def search(arr):
    libs_all = []
    while len(arr)>0:
        libs,path = lib(arr)
        
        for i in libs:
            if i in libs_all:
                libs.remove(i)
        
        libs_all += libs
        for i in path:
            del arr[i]
        
    return libs_all

'''
How to execute:

arr1 = {
    'A' : ['B','C','D'],
    'B' : ['D','E','F'],
    'F' : ['G','H','L'],
    'X' : ['Y','Z']
}

search(arr1)

'''