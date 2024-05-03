def calc_mean(numbers_array):
    averages = []  
    for line in numbers_array:
        sum_of_line = 0
        for num_str in line:
            sum_of_line += int(num_str)
        line_average = sum_of_line / len(line)
        averages.append(line_average)
    return averages

filename = input("File name: ")
with open(filename, 'r') as file:
    lines = file.readlines()
    numbers_array = []
    for line in lines:
        numbers_array.append(line.split())

averages = calc_mean(numbers_array)

for i, avg in enumerate(averages):
    print(f"The average of line {i+1} is {avg}")
   
