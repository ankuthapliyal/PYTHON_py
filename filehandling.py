# READING A FILKE
# file = open("mast.txt","r")
# # print(file)
# text = file.read()
# line = file.readline()
# print(line)
# print(text)
# if not line:
#     print(line,type(line))
# file.close()

# with open("mast.txt","r") as f:
#     print(type(f))
#     f.seek(55)

#     print(f.tell())
#     data = f.read(5)
#     print(data)

# WRITING A FILE

# file = open("report.txt", "w")
# # file.write("Hello Anku")
# line = ['line 1\n','line 2\n','line 3\n']
# file.writelines(line)
# file.close()

# with open("report.txt", "w") as file:
#     file.write("Hey I am inside with")
# data = data.lower()

with open("report.txt","w") as f:
    f.write("Hello anku")
    f.truncate(1)

with open("report.txt","r") as f:
    print(f.read())
# if("live" in data):
#     print("Yes Live word id present in the file")
# else:
#     print("NO")

# file = open("report.txt", "a")
# file.write("\n Me apne corse m bhi padh raa ho.") 