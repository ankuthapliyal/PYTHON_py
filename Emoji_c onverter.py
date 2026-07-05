# msg = input("Enter Your Message: ")

# msg = msg.replace("H", "😂")
# msg = msg.replace('P', "😍")
# msg = msg.replace('N', "👌")
# msg = msg.replace('!', "😒")
# msg = msg.replace('Y', "👍")
# msg = msg.replace('Lo', "😘")
# msg = msg.replace('M', "😎")
# msg = msg.replace('U', "🎶")
# msg = msg.replace('S', "😔")
# msg = msg.replace('A', "😡")
# print(msg)

# str = "Hello World"
# print(str[0:11:2])
# print(str[0:6:-1])  # empty string
# print(str[-5:-1:2])
# print(str[::-1]) #string revers
# print(len(str))
# s = "hello "+ "world"
# print("*" * 5)
# del str
# print(str)

# a = 3
# print(id(a))

# x = 5
# b = x # aliasing
# print(id(x))
# print(id(b))
# import sys
# a = "corona"
# b = a
# c = b
# print(id(a))
# print(id(b))
# print(id(c))
# print(sys.getrefcount(a))

l1 = [1,2,3]  #cloning
l2 = l1[:]
l2.append(4)
print(l1)
print(l2)