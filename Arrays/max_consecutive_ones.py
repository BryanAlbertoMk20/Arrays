def findMaxConsecutiveOnes(nums):
    lst_of_ones = []
    counter = 0

    for number in nums:
        if number == 1:
            counter += 1
        elif number != 1 and counter != 0:
            lst_of_ones.append(counter)
            counter = 0
    lst_of_ones.append(counter)
    lst_of_ones.sort()
    largest = lst_of_ones[-1]
    return largest


lst1 = []
lst2 = [1,0,1,1,0,1]
lst3 = [1,2,3,3,11,1,1,1,11,1,1,1,1,1,1,1,1,4,6,7,4]


print(findMaxConsecutiveOnes(lst1))
print(findMaxConsecutiveOnes(lst2))
print(findMaxConsecutiveOnes(lst3))