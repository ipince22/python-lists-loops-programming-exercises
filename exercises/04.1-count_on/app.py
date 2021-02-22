
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]
hello=[]

#your code go here:
for x in range(len(my_list)):
    if isinstance(my_list[x],dict):
        hello.append(my_list[x])
    elif isinstance(my_list[x],list):
        hello.append(my_list[x])


print(hello)
