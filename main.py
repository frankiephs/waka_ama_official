# Display folder year
import os

path = "waka_parent"

dir_list = os.listdir(path)

print(dir_list)



# separate the output
print()

# number of files in the folder
years_and_files = {}

for every_item in dir_list:
  years_and_files[every_item] = len(os.listdir(path + "/" + every_item)) # put inside the dictionary
  
print(years_and_files) # shows the results