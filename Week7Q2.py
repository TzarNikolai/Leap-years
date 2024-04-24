#step 1
#Take first input, 
#gather first and last digit of list, 
#check length of list, 
#calculate sum of first and last or sum of one if applicable 

input_1 = (input("List 1: "))
first_digit = int(input_1[0])
last_digit = int(input_1[-1])
if len(input_1) == 1:
    sum_of_1 = first_digit
else:
    sum_of_1 = first_digit + last_digit

#Repeat step 1 but for second input
input_2 = (input("List 2: "))
first_digit = int(input_2[0]) 
last_digit = int(input_2[-1])
if len(input_2) == 1:
    sum_of_2 = first_digit
else:
    sum_of_2 = first_digit + last_digit 

#see if first or second input is greater or the same and print the outcome
if sum_of_1 > sum_of_2:
    print(f"Output: {sum_of_1}")
elif sum_of_1 < sum_of_2:
    print(f"Output: {sum_of_2}")
else:
    print("output: Same")

