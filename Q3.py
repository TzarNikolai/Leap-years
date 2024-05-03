def calc_mean(sline):
   sum_of_list = 0 

   for i in range(len(sline)):
      sum_of_list += sline[i]
   average = sum_of_list/len(sline)        
   return average


filename = input("File name: ")
with open(filename, 'r') as file:
   lines = file.readlines()
   first_line = lines[:1]

   for line in first_line:
         sline = line.strip()
         sline = sline.split()
      
   calc_mean(sline)
   mean_of_num = calc_mean(sline)
   print(mean_of_num)

   
      