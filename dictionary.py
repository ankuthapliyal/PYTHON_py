# student = {
#     "name": "Anku thapliyal",
#     "age" : 20,
#     "city":"Uttarakhand",
#     "roll_no": 25
# }

# print(type(student))
# print(student["name"])
# print(student["age"])

# # Method of dictionary

# student["city"] = "Chamoli"  #Update value
# print(student)
# student["Subject"] = "Python Programming" # add new key & value
# print(student)
# student.pop("Subject") #remove key
# print(student)
# print(student.keys())
# print(student.values())
# print(student.items())

# prectis Question

# marks = {}

# marks["Maths"] = 95
# marks["Chemistry"] = 85
# marks["Physics"] = 92
# print(marks)

dic = {"Name":"Rohit","Colleg" :"THDC-IHET","Marks": {"DSA":56, "M1": 45, "English": 68}} #2D dictionary
# print(dic["Marks"]["DSA"]) 
# print(dic)
# dic["Marks"]["DSA"] = 70
# print(dic["Marks"]["DSA"])
# print(dic)
# print(dic.get("Name"))
# dic["Age"] = 20
# dic["Marks"]["M2"] = 60
# print(dic)
# # del dic["Marks"]["M2"]
# print(dic)
# for i in dic:
#     print(i,dic[i])

print(min(dic))
print(max(dic))
print(sorted(dic,reverse=True))
print(dic.keys())
print(dic.values())