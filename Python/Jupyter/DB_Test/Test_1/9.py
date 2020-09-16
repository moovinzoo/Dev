def selSort(nums):
    n = len(nums)

    for bottom in range(n-1):
        mp = bottom
        for i in range(bottom+1, n):
            if nums[i] < nums[mp]:
                mp = i
        tmp = nums[bottom]
        nums[bottom] = nums[mp]
        nums[mp] = tmp

    return nums


nums_1 = [1, 2, 5, -2, 3, 6, 4]
print(nums_1)
print(selSort(nums_1))