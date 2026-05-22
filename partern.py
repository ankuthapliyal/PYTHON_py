# rows = 5
# for i in range(1,rows + 1):
#     print(' ' * (rows - 1) +
#     '*' * (2 * i-1))
   
# rows =5
# for i in range(rows, 0, -1):
#     print(' ' * (rows -1) +
#      '*' * (2*i-1))

rows =5
# upper half
for i in range(rows + 1):
    print(' ' * (rows -1) +
     '*' * (2*i-1))
#  lower half
for i in range(rows- 1, 0,
    -1):
    print(' ' * (rows -1) +
     '*' * (2*i-1))