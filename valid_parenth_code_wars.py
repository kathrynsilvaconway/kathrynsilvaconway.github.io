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
def dupEncode(string):
    list = []
    string = string.lower()
    for x in string:
        count = string.count(x)
    for x in string:
        print (count)
        
    
dupEncode('Success1!')
