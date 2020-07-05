# Raw palindrome check:
# sentence = 'anita lava la tina'
# list_of_words = [letter for letter in sentence.strip().replace(' ', '')]
# print(list_of_words)
#
# b = list_of_words.pop(0)
# e = list_of_words.pop(-1)
# print(b == e)
# print(list_of_words)


# recursive palindrome check
def is_palindrome(list_of_words):
    # print(list_of_words)
    if len(list_of_words) <= 1:
        return True
    if list_of_words.pop(0) == list_of_words.pop(-1):
        return is_palindrome(list_of_words)
    else:
        return False

# l = ['a', 'b', 'a']
# n fn                               values
# 1 r=is_palindrome(['b'])(call 2)   list_of_words = ['a', 'b', 'a'] -> ['b']
# 2 r=True                           list_of_words = ['b']

sentence = 'anita lava la tina'
list_of_words = [letter for letter in sentence.strip().replace(' ', '')]
print(is_palindrome(list_of_words))
