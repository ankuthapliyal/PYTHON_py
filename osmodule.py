import os

if (not os.path.exists("data")):
    os.mkdir("data")

for i in range(0,101):
    os.mkdir("data/Day{}".format(i+1))