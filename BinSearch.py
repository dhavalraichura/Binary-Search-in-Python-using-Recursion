data = []
def finput():
    n = input("Enter the data or type 'done' to end\n")
    data.append(n)
    if data[len(data)-1] != 'done' or int(len(data)) == 0:
        finput()
    else:
        data.remove('done')
finput()
data.sort()
target = int(input("Enter the value to be searched\n"))
lp = 0
hp = len(data)
def binSearch(lp,hp):
    mp = int((hp+lp)/2)
    if target == int(data[mp]):
        return mp
    elif target > int(data[mp]):
        return binSearch(mp+1,hp)
    elif target < int(data[mp]):
        return binSearch(lp,mp-1)
    else:
        return mp
result = binSearch(lp,hp)+1
print("The position is: "+str(result))