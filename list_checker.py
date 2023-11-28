import collections
list_ofobjects = [ 'a', 'b', 'a', 'b', 'c', 'd', 'e', 'a', 'b', 'h', 'u', 'i', 'x', 'b', 'e', 'h', 'j', 'w',"a" ]
store={}

for i in list_ofobjects:
    if i in store.keys():
        store[i] += 1
    else:
        store[i] = 1

print(store)



#todo store in dictionary
