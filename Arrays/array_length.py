sample1 = [1, 1, 0, 1, 1, 1]
sample2 = [1, 0, 1, 1, 0, 1]
sample3 = [2, 3, 1, 4, 13, 1, 1, 1, 23, 1, 1, 1, 459, 1, 1, 1, 1, 1]
sample4 = [0]
sample5 = []


# def find_max_number_of_ones(lst):
#     counter = 0
#     for number in lst:
#         if number == 1:
#             counter += 1
#     print(f"This is how many times one appears. {counter} times.")


def find_max_consecutive_ones(nums):
    lst_of_ones = []
    counter = 0
    for number in nums:
        if len(nums) == 0 or number == 0:
            return
        if number == 1:
            counter += 1
        elif number !=1:
            lst_of_ones.append(counter)
            counter = 0

    max_ones = max(lst_of_ones)
    return max_ones


value1 = find_max_consecutive_ones(sample1)
value2 = find_max_consecutive_ones(sample2)
value3 = find_max_consecutive_ones(sample3)
value4 = find_max_consecutive_ones(sample4)
value5 = find_max_consecutive_ones(sample5)

print(value1, value2, value3, value4, value5)

