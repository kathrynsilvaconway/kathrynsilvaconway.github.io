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
#     return sorted(ages[:-2])
# print(two_oldest_ages([84, 48, 27, 63, 25, 67, 90, 25, 63, 76, 69, 58, 86, 58, 0, 86, 23, 90, 81]))
# # print(two_oldest_ages([1, 5, 87, 45, 8, 8])
# class Person:
    
#     def __init__(self, name):
#         self.name = name

#     def greet(self, your_name):
#         return f"Hello {your_name}, my name is {self.name}"

# jack = Person("Jack")
# jill = Person("Jill")
# print(jack.greet("jill"))

# class Person():

#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.full_name = first_name + ' '+last_name

# return a float round to two decimal places:
# def solution(n):
#     return float(format(n, ".2f"))
# Easier:
# def solution(n):
#     return round(n, 2)


