# def bonus_time(salary, bonus):
#     if bonus == True:
#         salary = salary * 10
    # return (f"${salary}")

# Best Practice Vote:
# def bonus_time(salary, bonus):
#     return "${}".format(salary * (10 if bonus else 1))
# print(bonus_time(10000, True))

# return a string with no spaces:
# def no_space(x):
#     return x.replace(' ','')

# def points(games):
#     points = 0
#     for x in games:
#         if x[0] > x[-1]:
#             points += 3
#         elif x[0] < x[-1]:
#             points += 0
#         else:
#             points += 1
#     return points
# print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))

# def square_sum(numbers):
#     sum = 0
#     for x in numbers:
#         sum += x ** 2
#     return sum
# print(square_sum([1,2,2]))

# def square_sum(numbers):
#     return sum(x ** 2 for x in numbers)
# print(square_sum([1,2,2]))

# def are_you_playing_banjo(name):
#     return f'{name} plays banjo'  if name.lower()[0] == 'r' else f'{name} does not play banjo'
# print(are_you_playing_banjo('Bow'))

# cow = iter(range(1, 30000))
# print(type(cow))


# def points(games):
#     count = 0
#     for x in games:
#         if x[0] > x[-1]:
#             count += 3
#         elif x[0] < x[-1]:
#             count += 0
#         else:
#             count += 1
#     return count

#     def square_sum(numbers):
#         return sum(x ** 2 for x in numbers)

# 1
# def say_hello(name, city, state):
#     string = 'Hello, '
#     for x in name:
#         string += x
#         string += ' '
#     string = string[:-1]
#     string += '! Welcome to '
#     string += city
#     string += ", "
#     string += state
#     string += '!'
#     return string
 


# print(say_hello(['John', 'Smith'], 'Phoenix', 'Arizona'))

# def say_hello(name, city, state):
#     return "Hello, {}! Welcome to {}, {}!".format(" ".join(name), city, state)
# print(say_hello(['John', 'Smith'], 'Phoenix', 'Arizona'))

def grader(score):
    if score < .6 or score > 1:
        return 'F'
    elif score >= .9:
        return 'A'
    elif score >= .8:
        return 'B'
    elif score >= .7:
        return 'C'
    elif score >= .6:
        return 'D'