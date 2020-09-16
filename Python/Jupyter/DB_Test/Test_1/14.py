def f3(list):
    for i in range(len(list)):
        print(list[len(list) - (i + 1)])
    # reversed_list = [
    #     list[len(list) - (i+1)] for i in range(len(list))
    # ]
    # print(reversed_list)


f3([1, 2, 3])
f3([])
f3([3, 2, 1])