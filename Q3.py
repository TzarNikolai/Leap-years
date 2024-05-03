def calc_mean(numbers_array):
    sum_of_list = 0 
    for i in range(len(numbers_array)):
        for j in range(len(numbers_array[i])):
            sum_of_list += int(numbers_array[i][j])
            average = sum_of_list/len(numbers_array[i][j])        
        return average
    
filename = input("File name: ")
with open(filename, 'r') as file:
    lines = file.readlines()
    numbers_array = []
    for line in lines:
        numbers_array.append(line.split())


print_mean = calc_mean(numbers_array)
for i, avg in enumerate(print_mean):
    print(f"Average of line {i+1}:{avg}")

   
      
