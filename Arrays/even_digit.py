
def find_even_numbers(nums):
    str_lst = [str(numbers) for numbers in nums]
    even_words = len([word for word in str_lst if len(word) % 2 == 0])
    return even_words

"use mapping "

"list of numbers"
lst = [12,345,2,6,7896]

print(find_even_numbers(lst))
