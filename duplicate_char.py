string = input("enter the string whose duplicate characters you want to find:")
def duplicates_char(s):
    elements = {}
    for i in s:
        if elements.get(i,None) != None:
            elements[i]+=1
        else:
            elements[i] = 1
    return [k for k,v in elements.items() if v>1]
print("the duplicate character in",string,"is")
print(duplicates_char(string))
