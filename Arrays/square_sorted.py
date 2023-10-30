def sorted_squares(nums):
    squared_nums = [numbers ** 2 for numbers in nums]
    sorted_squared_nums = sorted(squared_nums)
    return sorted_squared_nums


lst1 = [-7,-3,2,3,11]
lst2 = [-4,-1,0,3,10]

print(sorted_squares(lst1),sorted_squares(lst2))

