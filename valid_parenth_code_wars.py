# def likes(names):
#     if not names:
        # return "no one likes this"
#     if len(names) == 1:
#         return (str(names[0])+' likes this')
    # if len(names) == 2:
#         return (str(names[0])+' and '+str(names[1])+' like this')
#     if len(names) == 3:
#         return (str(names[0])+', '+str(names[1])+' and '+str(names[2]+' like this'))
#     if len(names) > 3:
#         x = len(names) - 2
#         x = str(x)
#         return(str(names[0])+', '+str(names[1])+' and '+x+' others likes this')
# print(likes(names=['Peter', 'Jane', 'Brian', 'Cow', 'Marshall']))

# def find_outlier(integers):
#     even = []
#     odd = []
#     for x in integers:
#         if x % 2 == 0:
#             even.append(x)
#         if x % 2 != 0:
#             odd.append(x)
#     if len(even) == 1:
#         return even[0]
#     else:
#         return odd[0]

# print(find_outlier(integers=[2, 4, 0, 100, 4, 12, 2601, 36]))

# def find_outlier(integers):
#     even = [x for x in integers if x%2==0]
#     odd = [x for x in integers if x%2!=0]
#     return even[0] if len(even) < len(odd) else odd[0]

# print(find_outlier(integers=[2, 4, 0, 100, 4, 12, 2601, 36]))

# turn string into list
# iterate through items

# 
# def validpar(string):
    # stack = []
    # dict = {')':'('}
    # for x in string:
    #     if x in dict:
    #         if stack and stack[-1] == dict[x]:
    #             stack.pop()
    #         else: return False
    #     elif x == ')' or x == '(': 
    #         stack.append(x)
    # return True if not stack else False
# print(validpar('(((((((((((((((((((((((((((((())))))))))))))))))))))))))))))'))
# def valid_parentheses(string):
#     cnt = 0
#     for char in string:
#         if char == '(': cnt += 1
#         if char == ')': cnt -= 1
#         if cnt < 0: return False
#     return True if cnt == 0 else False
# def dupEncode(string):
#     list = []
#     result = []
#     string = string.lower()
#     for x in string:
#         list.append(x)
#     for y in list:
#         if list.count(y) < 2:
#             result.append('(')
#         else: result.append(')')
#     print_it = ''.join(result)
#     return print_it
# print(dupEncode('Success1!'))

# def countCharacters(string):
#     dict = {}
#     string = string.lower()
#     for x in string:
#         dict[x] = string.count(x)
#     return dict
# print(countCharacters('Success'))

# def decodeMorse(morse_code):
#     code = morse_code
#     code = code.replace('   ',' * ')
#     code = code.split()
#     list = []
#     m = {
#     '.-': 'A',
#     '-...': 'B',
#     '-.-.': 'C',
#     '-..': 'D',
#     '.': 'E',
#     '..-.': 'F',
#     '--.': 'G',
#     '....': 'H',
#     '..': 'I',
#     '.---': 'J',
#     '-.-': 'K',
#     '.-..': 'L',
#     '--': 'M',
#     '-.': 'N',
#     '---': 'O',
#     '.--.': 'P',
#     '--.-': 'Q',
#     '.-.': 'R',
#     '...': 'S',
#     '-': 'T',
#     '..-': 'U',
#     '...-': 'V',
#     '.--': 'W',
#     '-..-': 'X',
#     '-.--': 'Y',
#     '--..': 'Z',
#     '-----': '0',
#     '.----': 1,
#     '..---': 2,
#     '...--': 3,
#     '....-': 4,
#     '.....': 5,
#     '-....': 6,
#     '--...': 7,
#     '---..': 8,
#     '----.': 9
#     }
    
#     for x in code:
#         if x in m  and x != "*":
#             list.append(m[x])
#         else:
#             list.append(" ")
#     return "".join(list).strip()
        
    
# print(decodeMorse('.... . -.--   .--- ..- -.. .'))

# from typing import Collection


# def find_it(seq):
#     for x in seq:
#         if seq.count(x) % 2 != 0:
#             return x    
# print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))

# def snail(map):
#     pattern = []
#     while len(map) > 0:
#         pattern += map[0]
#         del map[0]

#         if len(map) > 0:
#             for x in map:
#                 pattern.append(x[-1])
#                 del x[-1]
#             if len(map) > 0:
#                 pattern += map[-1][::-1]
#                 del map[-1]
#             for x in reversed(map):
#                 pattern.append(x[0])
#                 del x[0]
        

#     return pattern
# print(snail([[1, 2, 3], [4, 5, 6 ], [7, 8, 9]]))

# def cakes(recipe, available):
#     list = []
#     for key, value in recipe.items():
#         if key not in available:
#             return 0
#         else:
#             how_much = available[key] // recipe[key]
#             list.append(how_much)
#     return sorted(list)[0]
                    

# print(cakes(recipe = {"flour": 500, "sugar": 200, "eggs": 1},
# available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))
# def fib(x):
#     if x == 0:
#         return 0
#     elif x == 1:
#         return 1
#     elif x > 1:
#         return fib(x-2)+ fib(x-1)
# for x in range(0, 11):
#     print(fib(x))

# def nesting(array, other):
#     array = str(array)
#     other = str(other)
#     array_str = ''
#     other_str = ''
#     for x in array:
#         if x == '[' or x == ']' or x == ',' or x == ' ' or x == "'":
#             array_str += x
#     for x in other:
#         if x == '[' or x == ']' or x == ',' or x == ' ' or x == "'":
#             other_str += x
#     print(array_str)
#     print(other_str)
#     if array_str == other_str:
#         return True
#     else:
#         return False
# print(nesting([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ]))

# look up how to use permutations
# def permutations(string):
#     import itertools
#     this_list = []
#     result = list(itertools.permutations(string))
#     for x in result:
#         this_list.append(''.join(x))
#     return list(set(this_list))

# print(permutations('aabb'))

# import ipaddress
# def ip_add(integer):
#     return str(ipaddress.ip_address(integer))
# print(ip_add(3232235777))

# ignore caps.
# ignore letters that appear only once.
# return a str that displays max letters 
# and which str they came from.
# type out letters, don't return count.
# prefix with 1: for str 1 and 2: for str 2.
# if max is same for both, prefix with =:

# filter

# def mix(s1, s2):
#     s1_filter = []
#     s2_filter = []
#     new_list = []
#     for x in s1:
#         if x.islower() and s1.count(x) > 1:
#             s1_filter.append(x)

#     for x in s2:
#         if x.islower() and s2.count(x) > 1:
#             s2_filter.append(x)
#     for x in s1_filter:
#         if x not in s2_filter:
#             stringy = ('1:'+ x*s1_filter.count(x)+'/')
#             new_list.append(stringy)
#         else:
#             if s1_filter.count(x) > s2_filter.count(x):
#                 stringy = ('1:'+ x*s1_filter.count(x)+'/')
#                 new_list.append(stringy)
#             elif s1_filter.count(x) < s2_filter.count(x):
#                 stringy = ('2:'+ x*s1_filter.count(x)+'/')
#                 new_list.append(stringy)
#             else:
#                 stringy = ('=:'+ x*s1_filter.count(x)+'/')
#                 new_list.append(stringy)
#     for x in s2_filter:
#         if x not in s1_filter:
#             stringy = ('2:'+ x*s2_filter.count(x)+'/')
#             new_list.append(stringy)
#     new_list = set(new_list)
#     new_list = sorted(new_list, key=len)
#     new_list =list(reversed(new_list))
#     new_list = sorted(new_list)
#     new_list = ''.join(new_list)
#     new_list = new_list.rstrip(new_list[-1])
#     return new_list
    
            
# print(mix("Are they here", "yes, they are here"))
# def dbl_linear(n):
#     u = [1]
#     x = 0
#     y = 0
#     while len(u) <= n:
#         first = (2 * u[x] + 1)
#         second = (3 * u[y] + 1)
#         if first > second: 
#             u.append(second)
#             y += 1
#         elif second > first:
#             u.append(first)
#             x += 1
#         else:
#             u.append(first)
#             x += 1
#             y += 1
#     print(first, second)
#     return u[n]
    
# print(dbl_linear(13))

def top_3_words(text):
    counts = {}
    top_list = []
    check_for_letters = []
    for x in text:
        if x.isalpha() == False and x is not "'" and x is not " ":
            text = text.replace(x, '')
            text = text.lower()
        for y in x:
            if y.isalpha():
                check_for_letters.append(x)
    if len(check_for_letters) == 0:
        return []

    text = list(text.split())
    for x in text:
        counts[text.count(x)] = x
        counts = dict(sorted(counts.items()))
    for key, value in counts.items():
        top_list.append(value)
    top_list = list(reversed(top_list))
    if len(top_list) > 3:
        return top_list[:3]
    if len(top_list) <= 3:
        return top_list
print(top_3_words(("''")))