# # read file - read
# a = open("student.txt","r")
# data = a.read()
# print(data)
# a.close()
  
# # remove old data and write new data onlyy - write
# file = open("student.txt","w")
# data = file.write("Aman is also genzz")
# file.close()

# # pehle ka data remove ni krta bs new data add krnta h  - append
# file = open("student.txt","a")
# file.write("\n Aman is also a genzz")
# file.close()

# # craete new file
# file = open("new_file.txt","x")

# # readline() - read one line at a time
# file = open("student.txt","r")
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.close()


# #readlines() - read more then one lines at a time as a list format
# file = open("student.txt","r")
# data = file.readlines()
# print(data)
# file.close()

# # professional open file with W
# with open("student.txt", "r") as file:
#     data = file.read()

# print(data)


# # again 
# with open("student.txt","a") as file:
#     data = file.write("\nhey sneha how are u bro ?")


