# Python program to convert text
# file to JSON


import json


# the file to be converted to
# json format
filename = 'data.txt'

# dictionary where the lines from
# text will be stored
json_list = []
# dict1 = {}

with open('data.txt',  encoding="utf8") as data_file:
    data_file.seek(0)
    # print(data_file.readlines())
    # json_list = data_file.readlines()
    dict1 = {}
    for line in data_file:
        command, description = line.strip().split(None, 1)
        dict1[command] = description.strip()
        if(len(dict1) == 4):
            json_list.append(dict1)
            dict1 = {}


print(json_list)
out_file = open("test1.json", "w")
json.dump(json_list, out_file, indent = 4,)
out_file.close()
# for line in data_file:
# # creating dictionary
# with open(filename) as fh:

# 	for line in fh:

# 		# reads each line and trims of extra the spaces
# 		# and gives only the valid words
#         print(line)
#         # if line == "":
#         #     print("empty")
# 		# command, description = line.strip().split(None, 1)

# 		# dict1[command] = description.strip()

# # creating json file
# # the JSON file is named as test1
# # out_file = open("test1.json", "w")
# # json.dump(dict1, out_file, indent = 4, sort_keys = False)
# # out_file.close()
