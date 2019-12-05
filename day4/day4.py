start = 353096
stop = 843212


#part one 
def is_qualified(num):

    x = num
    num = str(num)

    if sorted(num) != list(num): #determine if the list is in order 
        return False
    elif len(set(num)) == len(num): #determine if there are duplicate numbers
        return False
    
    return True



#part two
def is_qualified_num(num):

    num = str(num)

    if sorted(num) != list(num): #determine if the list is in order
        return False
    for i in num:
        if num.count(i) == 2: #determine if the list has exactly two duplicate numbers
            return True
    return False


total = 0
end = stop + 1

for i in range(start, end):
    if is_qualified_num(i):
        total += 1
    

print(total)