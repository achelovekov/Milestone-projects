def get_center(string,position):
    center_sign = string[position]
    start = end = position
    for i in range(position+1,len(string)):
        if string[i] != center_sign:
            break
        end+=1
    
    return start,end  

def get_polindrom(string,start,end):
    left_border = start - 1
    right_border = end + 1
    if string[left_border:start] != '' and string[end:right_border] != '':
        if string[left_border:start] == string[end:right_border]:
            return get_polindrom(string,left_border,right_border)
        else:
            return string[start:end]
    else: 
        return string[start:end]  

def flp(string):
    if len(string) == 0:
        return ''
    
    position = 0
    temp = ''

    while position < len(string):
        start,end = get_center(string,position)
        largest_polindrom = get_polindrom(string,start,end+1)
        if len(largest_polindrom) > len(temp):
            temp = largest_polindrom
        position = end+1
        largest_polindrom = temp
    return largest_polindrom

s = 'ababababa'
print(flp(s))