### continue statment -> it will skip the iteration and move to next iteration

for i in range(0, 10):
    if i % 2 == 0:
        continue
print(i)

## |i|condition|o/p|
## |0|0%2== 0 --> True|| continue --> skip no output
## |1|1%2== 0 --> False|| 1
## |2|2%2== 0 --> True|| continue --> skip no output
## |3|3%2== 0 --> False|| 3

# for i in range(0, 10):
#     if i % 2 == 0:
#         continue
#     else:
#         print(i)

