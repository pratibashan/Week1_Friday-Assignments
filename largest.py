

# Finding the largest in an array

numbers = [12,24,35,200,46,57,68,500,79,90,101]
large = 0
for index in range(0,len(numbers)):
    if(numbers[index]> large): 
        large = numbers[index]
        
print(f"The largest element in the array {numbers}\n is {large}")        
   