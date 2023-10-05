spam = ["Uche","Loveth","Isabella","Zeal"]

def list_convertor(the_list=list):
    newvalue = ""
    if len(the_list) == 0:
        return "this list is empty."
    elif len(the_list) == 1:
        return the_list[0]
    elif len(the_list)>= 2:
        for item in range(len(the_list)-1):
            newvalue +=  str(the_list[item]) +" , "
        newvalue +="and "+ str(the_list[-1])
    return newvalue



    
spam=[1,2]

print(list_convertor(spam))