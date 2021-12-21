# compare the ascii value of two strings. Not case sensitive, ignoring all non alpha:
# def compare(s1,s2):
#     count1, count2 = 0, 0
#     if s2 == "":
#         return True
#     for x in s1.upper():
#         if x.isalpha() != True:
#             s1.replace(x,'')
#             count1 += ord(x)
#     for x in s2.upper():
#             count2 += ord(x)
#     print(s1, s2)
#     return True if count1 == count2 else False

# print(compare("!!", "7476"))

# def compare(s1,s2):
#     count1, count2 = 0, 0
#     if s2 == "":
#         return True
#     for x in s1.upper():
#         if x.isalpha() == True:
#             count1 += ord(x)
#     for x in s2.upper():
#         if x.isalpha() == True:
#             count2 += ord(x)
#     return True if count1 == count2 else False

# print(compare("!!", "7476"))
# def two_oldest_ages(ages):
#     oldest = []
#     oldest.append(list(set(ages))[-2])
#     oldest.append(list(set(ages))[-1])
#     return oldest
