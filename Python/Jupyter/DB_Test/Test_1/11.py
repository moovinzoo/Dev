def f12(list):
    for i in range(len(list) - 1):
        for j in range(i, len(list)):
            if list[i] < list[j]:
                print(False)
                return
    print(True)

    
(f12([]))
(f12([5, 4, 3, 2, 1]))
(f12([5, 4, 3, 2, 0]))
(f12([5, 4, 5, 2]))
