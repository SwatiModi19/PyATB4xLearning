count =10

def increment():
    global count
    count = count+1
    print(count)

# count =0    --> local variabl not defined ans cannot access outside function
increment()
increment()
increment()
increment()
increment()
increment()
