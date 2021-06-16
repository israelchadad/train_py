string = "Hello world"

friends = []
friends.append("israel")
friends.append("hilla")
friends.append("anael")
tpl = tuple(friends)
friends.remove("israel")

print(friends[0:2])
del friends
str_num = [1, 2, 1, 4, 5]
# print(max(str_num))
# print(string.find("d"))

train_file = open("train.txt", 'a')
train_file.write("\nyour kids - anael and oryan")
'''for data in train_file.readlines():
    print(data)'''

train_file.close()

fruits = ("apple", "banana", "banana", "cherry")

(green, yellow, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)
try:
    print(fruits.count("banana"))
except ValueError as Error:
    print(Error)

thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
# print(thisset)

thisset = {"apple", "banana", "cherry"}

# print("banana" in thisset)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
# print(thisdict)

string1 = "absdfgsab"
string = "abs"
# print(string in string1)
# print(string1.count(string))
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = (map(list, l))
# print(list(test))

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
# print(less_than_zero)

from functools import reduce

product = reduce((lambda x, y: x * y), [1, 2, 3, 4])


# print((product))


def rmv(numbers, num):
    for i in numbers:
        if (i % num == 0):
            numbers.remove(i)
    return numbers


# print(rmv([1, 2, 3, 4, 5], 2))


def palindrom(str):
    str1 = list(str)
    str1.reverse()
    return str1 == list(str)


# print(palindrom("jhuiftuf"))


def sorting(numbers):
    dict = {x: numbers.count(x) for x in range(101) if x in numbers}
    newArr = []
    for i in range(101):
        if (i in dict):
            n = [i] * dict[i]  # [i] ->key. dict[i]->value
            newArr.extend(n)
    return newArr


# print(sorting([1, 1, 1, 2, 4, 5, 67, 3, 3, 6, 32, 32, 32, 56, 78, 12, 23, 53, 32, 56, 78, 90, 65]))


def fibo(index):
    prev, next = 0, 1
    if (index < 2): return 1
    for i in range(index):
        prev, next = next, prev + next
    return prev


# print(fibo(1))

def char_that_repeat(string):
    for ch in string:
        if string.count(ch) > 1:
            return ch


# print(char_that_repeat('wooooow'))


def indexOfMaxCount(string):
    dict = {x: string.count(x) for x in string}
    maxV = max(list(dict.values()))
    for (key, value) in dict.items():
        if value == maxV:
            return {'letter': key, 'count': value, 'index': string.index(key)}


# print(indexOfMaxCount("abbbchfgabbbcaaa"))


def array_diff(a, b):
    return [x for x in a if x not in b]


# print(array_diff([1, 2, 2], [2]))


def spin_words(sentence):
    return ' '.join([sen[::-1] if len(sen) >= 5 else sen for sen in sentence.split()])
    # sentence = sentence.split(' ')
    # newSen = []
    # for sen in sentence:
    #     if (len(sen) >= 5):
    #         newSen.append(sen[::-1])
    #     else:
    #         newSen.append(sen)
    # return ' '.join(newSen)


print(spin_words("hello from israel"))


def vowels(senten):
    disVowels = ['a', 'e', 'i', 'o', 'u']
    return ''.join([sen if not sen.lower() in disVowels else '' for sen in senten])


# print(vowels('This website is for losers LOL!'))


def add_binary_guy(a, b):
    res, tRes = a + b, ''
    while (res):
        tRes += str(res % 2)
        res //= 2
    return tRes[::-1]


def add_binary(a, b):
    return bin(a + b)[2:]


# print(add_binary(5, 9))
def friend(x):
    return list(filter(lambda name: len(name) <= 4 and name.isalpha(), x))


# print(friend(['Ryan', '123', '4']))

def narcissistic(num):
    return num == sum([int(x) ** len(str(num)) for x in str(num)])


# print(narcissistic(371))

def persistence(n):
    array = []
    count = 0
    while (n):
        num = n % 10
        array.append(num)
        n //= 10
        if n == 0:
            if len(array) > 1:
                sum = reduce(lambda x, y: x * y, array)
                n = sum
                count += 1
                array.clear()
    return count


# print(persistence(25))


def weight_of_word(string):
    weightArr = []
    stringArr = string.split(' ')
    for word in stringArr:
        tempS = 0
        for ch in word:
            tempS += ord(ch) - 96
        weightArr.append(tempS)

    maxW = max(weightArr)
    return stringArr[weightArr.index(maxW)]

print(weight_of_word('aaa bb'))








