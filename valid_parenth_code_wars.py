# def likes(names):
#     if not names:
#         return "no one likes this"
#     if len(names) == 1:
#         return (str(names[0])+' likes this')
#     if len(names) == 2:
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

def find_it(seq):
    count = 0
    for x in seq:
        count+= 1
        if count % 2 == 0:
            count = 0
    else:
        return x

print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))