# import os

# folders = os.listdir("data")

# print(os.getcwd())
# os.chdir("/Users")
# print(os.getcwd())
# # print(folders)

# # for folder in folders:
# #     print(folder)
# #     print(os.listdir(f"data/{folder}"))

#sicret code language
import random
import string

message = input("Enter message: ")
words = message.split()

coding = input("1 for Coding or 0 for Decoding: ")
coding = coding == "1"

newwords = []

if coding:
    for word in words:
        if len(word) >= 3:
            r1 = ''.join(random.choices(string.ascii_letters, k=3))
            r2 = ''.join(random.choices(string.ascii_letters, k=3))

            strnew = r1 + word[1:] + word[0] + r2
            newwords.append(strnew)
        else:
            newwords.append(word[::-1])

    print("Encoded:", " ".join(newwords))

else:
    for word in words:
        if len(word) >= 3:
            strnew = word[3:-3]
            strnew = strnew[-1] + strnew[:-1]
            newwords.append(strnew)
        else:
            newwords.append(word[::-1])

    print("Decoded:", " ".join(newwords))