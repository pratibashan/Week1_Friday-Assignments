

# finding the smallest element in the array

numbers = [12,24,35,200,46,57,1,68,500,79,90,101,5]
small = 0
for index in range(0,len(numbers)):
    
    if (small == 0):
        small = numbers[index]
        print(small)
    elif(small >0 and small > numbers[index]):     
        small = numbers[index]
print(f"The smallest number in the array {numbers} is {small}") 
    
