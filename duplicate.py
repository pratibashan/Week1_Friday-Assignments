

#removing duplicates from an array


names_duplicates = ["Alex","John","Mary","Steve","John", "Steve"]
names_no_duplicate = []

for name in names_duplicates: 
    if not name in names_no_duplicate:
        names_no_duplicate.append(name) 
print(names_no_duplicate)         
        



#names_no_duplicate = []
#for index in range(0,len(names_duplicates)):
#    #print(names_duplicates[name])
#    #for name1 in range(0,len())
#
#    if len(names_no_duplicate) == 0:
#        # array is empty 
#    else: 
#
#    if(names_no_duplicate[index] != names_duplicates[index]):
#        names_no_duplicate.append(names_duplicates[index]) 
#print(names_no_duplicate)  
#
#    #if (names[name] == names[name]):
#    #    names = names.remove(names[name])
##print(names)
    

