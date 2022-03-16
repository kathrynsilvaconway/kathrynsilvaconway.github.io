# def diagonalDifference(arr):
#     n = len(arr)
#     ltor_total = 0
#     rtol_total = 0
#     m = 0
#     q = 0
#     r = n - 1
#     s =0

#     while n > m:
#         ltor_total += arr[m][q]
#         m += 1
#         q += 1

#     while r > (-1):
#         rtol_total += arr[s][r]
#         s += 1
#         r -= 1   
#     total = ltor_total-rtol_total
#     return abs(total)

# print (diagonalDifference([[1,2,3],[4,5,6],[9,8,9]]))

# def plusMinus(arr):
#     l = len(arr)
#     a_count = 0
#     b_count = 0 
#     c_count = 0
#     for x in arr:
#         if x > 0:
#             a_count += 1
#         if x < 0:
#             b_count += 1
#         if x == 0:
#             c_count += 1
#     a = a_count/l
#     b = b_count/l
#     c = c_count/l
#     print("{:.6f}".format(a))
#     print("{:.6f}".format(b))
#     print("{:.6f}".format(c))
   

# print(plusMinus([1,1,0,-1,-1]))
  
# def staircase(n):
#     stringy = []
#     st = ''
#     for x in range(n):
#         stringy.append(' ')
#     while n > 0:
#         stringy[n-1] = '#'
#         print(st.join(stringy))
#         n -= 1
# print(staircase(6))
# def miniMaxSum(arr):
#     sum = 0
#     skip = 0
#     totals = []
#     while skip < len(arr):
#         for x in range(len(arr)):
#             if x != skip:
#                 sum += arr[x]
#         skip += 1

#         totals.append(sum)
#         sum = 0
#     a = min(totals)
#     b = max(totals)
#     print(a,b)
# print(miniMaxSum([1,2,3,4,5]))

# def kangaroo(x1, v1, x2, v2):
#     # Write your code here
#     while x2 < 100000000:
#         x1 += v1
#         x2 += v2
#         if x1 == x2:
#             return "YES"
#     return "NO"

# print(kangaroo(2081, 8403, 9107, 8400))

# def getTotalX(a, b):
#     mults_of_first = []
#     factor_of_2 = []
#     count = 0
#     num = a[0]

#     while num <= b[-1]:
#         for x in a:
#             if num % x == 0:
#                 mults_of_first.append(1)
#         if len(mults_of_first) == len(a):
#             for y in b:
#                 if y % num == 0:
#                     factor_of_2.append(1)
#         if len(factor_of_2) == len(b):
#             count += 1
#         mults_of_first = []
#         factor_of_2 = []
#         num += 1
#     return count    

# print(getTotalX(a=[3,4], b=[24,48]))

# def breakingRecords(scores):
#     mini = scores[0]
#     maxi = scores[0]
#     mini_count = 0
#     maxi_count = 0
#     for x in scores:
#         if x < mini:
#             mini_count += 1
#             mini = x
            
#         if x > maxi:
#             maxi_count += 1
#             maxi = x
#     print(maxi_count,mini_count)

# print(breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]))

# def birthday(s, d, m):
#     count = 0
#     total = sum(s[:m])
#     if total == d:
#         count += 1
#     for x in range(m, len(s)):
#         total += s[x]
#         total -= s[x-m]
#         if total == d:
#             count += 1
#     return count
    

# print(birthday(s=[1, 2, 1, 3, 2],d=3,m=2))

# def divisiblesumpairs(n,k,ar):
#     count = 0
#     for x in range(len(ar)):
#         for y in range(x + 1, n):
#                 if (ar[x] + ar[y]) % k == 0:
#                         count += 1
#     return count

# print(divisiblesumpairs(6,5,[1,2,3,4,5,6]))

# def migratoryBirds(arr):
#     counts = {}
#     highs = []
#     highest = 0
#     for x in arr:
#         counts[x] = arr.count(x)
#     print(max(counts.values()))
#     for key, value in counts.items():
#         if value > highest:
#             highest = value
#     for key, value in counts.items():
#         if value == highest:

#             highs.append(key)

#     return min(highs)
# def migratoryBirds(arr):

#     counts = {}
#     highs= []
#     for x in arr:
#         counts[x] = arr.count(x)
#     qty = (max(counts.values()))
#     for x in arr:
#         if arr.count(x) == qty:
#             highs.append(x)
#     return min(highs)

# print(migratoryBirds([1,1,2,2,3]))
# print(migratoryBirds([1,1,2,2,3]))

# def migratoryBirds(arr):

#     counter = [0] * len(arr)
#     for x in range(len(arr)):    
#         counter[arr[x]] += 1  
#         print(counter)
#     return counter.index(max(counter))         
# print(migratoryBirds([1,1,2,2,3]))

# def dayOfProgrammer(year):
#     if year == 1918:
#         return (f'12.09.{year}')
#     if year <= 1919:
#         if year % 4 == 0:
#             return (f'12.09.{year}')
#         else:
#             return (f'13.09.{year}')
#     if year > 1919:
#         if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#             return (f'12.09.{year}')
#         else:
#             return (f'13.09.{year}')
            
# print(dayOfProgrammer(2017))

# def bonAppetit(bill, k, b):
#     eaten = 0
#     for x in range(len(bill)):
#         if x != k:
#             eaten += bill[x]
#     should_pay = eaten // 2
#     if b == should_pay:
#         print('Bon Appetit')
#     else:
#         print(b-should_pay)


# print(bonAppetit([3,10,2,9],1,12))

# def sockMerchant(n, ar):
#     # Write your code here
#     pairs = 0
#     used = []
#     for x in ar:
#         if x not in used:      
#             pairs += round((ar.count(x) -ar.count(x) % 2) /2)
#             used.append(x)
#     return pairs

# print(sockMerchant(7,[1,2,1,2,1,3,2]))
# import math
# def pageCount(n, p):
#     fr = p//2
#     if n % 2 == 1:
#         ba = (n-p)//2
#     else: 
#         ba = (n-p+1)//2
#     return min(fr, ba)
    

# print(pageCount(7,5))

# def countingValleys(steps, path):
    # level = 0
    # position = []
    # topo = []

    # for x in range(len(path)):
    #     if path[x] == "D":
    #         level -= 1
    #         position.append(level)
    #     else:
    #         level += 1
    #         position.append(level)
    # for y in range(len(position)):
    #     if position[y] == 0:
    #         if position[y-1] < 0:
    #             topo.append('valley')
    #         if position[y-1] > 0:
    #             topo.append('hill')
    # return topo.count('valley')
             


# print(countingValleys(8, 'DDUUUUDD'))

# def getMoneySpent(keyboards, drives, b):
#     combos = []
#     for x in keyboards:
#         for y in drives:
#             if x + y <= b:
#                 combos.append(x+y)
#     if combos != []:
#         return max(combos)
#     else:
#         return -1

# print(getMoneySpent([40,50,60], [5,8,12], 60))

# def catAndMouse(x, y, z):
#     x_dist = abs(x-z)
#     y_dist = abs(y-z)

#     if x_dist == y_dist:
#         return 'Mouse C'
#     elif x_dist < y_dist:
#         return ' Cat A'
#     else:
#         return 'Cat B'
# print(catAndMouse(4,44,44))


# def possibleMagicSquares(s):
#     all_squares = [
#         [[8, 1, 6],[3, 5, 7],[4, 9, 2]], 
#         [[6, 7, 2],[1, 5, 9],[8, 3, 4]], 
#         [[2, 9, 4],[7, 5, 3],[6, 1, 8]], 
#         [[4, 3, 8],[9, 5, 1],[2, 7, 6]], 
#         [[6, 1, 8],[7, 5, 3],[2, 9, 4]], 
#         [[2, 7, 6],[9, 5, 1],[4, 3, 8]], 
#         [[4, 9, 2],[3, 5, 7],[8, 1, 6]], 
#         [[8, 3, 4],[1, 5, 9],[6, 7, 2]]]
#     minimum = float('inf')
#     for square in all_squares:
#         cost = 0
#         for row in range(len(square)):
#             for digit in range(len(square[row])):
#                 cost += abs(s[row][digit] - square[row][digit])
#         if cost < minimum:
#             minimum = cost
#     return minimum
# print(possibleMagicSquares([[4,9,2],[3,5,7],[8,1,5]]))
# from collections import Counter
# def pickingNumbers(a):
#     my_list = Counter(a)
#     print(my_list)
#     high = 0
#     for x in range(100):
#         high = max(high, my_list[x]+my_list[x+1])
#         print(my_list[x])
#     return high
    # each_count = 0
    # total = 0
    # for x in range(len(a)-1):
    #     if abs(a[x+1] - a[x]) < 2:
    #         each_count += 1
    #         if each_count > total:
    #             total = each_count
    #     else:
    #         each_count = 0
        
    # return total+1   
# print(pickingNumbers([1,1,2,2,4,4,5,5,5,]))

# from audioop import reverse


# def climbingLeaderboard(ranked, player):
    # answer = []
    # # ranked = list(set(ranked))
    # # ranked.sort(reverse = True)
    # ranks = {}
    # # for x in range(len(ranked)):
    # #     ranks[x+1] = ranked[x]
    # for y in player:
    #     ranked.append(y)
    #     ranked = list(set(ranked))
    #     ranked.sort(reverse=True)
    #     print(ranked)
    #     for x in range(len(ranked)):
    #         ranks[x+1] = ranked[x]
    #     for key, value in ranks.items():
    #         if value == y:
    #             answer.append(key)
    # return answer
    # ranked = list(set(ranked))
    # ranked.sort()
    # iter = 0
    # leng = len(ranked)
    # print(ranked)
    # ranks = []
    # for x in player:
    #     while iter < leng and ranked[iter] <= x:
    #         iter += 1
    #     ranks.append(leng-iter+1)
    # return ranks
  
# print(climbingLeaderboard([100,100,50,40,40,20,10], [5,25,50,120]))

# def hurdleRace(k, height):
#     tallest = max(height)
#     doses = tallest - k
#     return doses if doses >= 0 else 0

# print(hurdleRace(4, [1,6,3,5,2]))

# def designerPdfViewer(h, word):
    #create a dict where the letter is the key and the num in h is the value
    #iterate through word.
    # for each char, find key in dict and add value to list
    # width of each char is 1mm
    #height will be max value in the list
    # answer is width x height
#     width = len(word)
#     heights = {}
#     maxes=[]
#     alpha = 'abcdefghijklmnopqrstuvwxyz'
#     for x in range(len(alpha)):
#         heights[alpha[x]] = h[x]
#     print(heights)
#     for x in word:
#         maxes.append(heights[x])
#     print(type(heights[x]))
#     return width * max(maxes)
# print(designerPdfViewer([1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5], 'abc'))

# from operator import index


# def utopianTree(n):
#     height = 1
#     listy = []
#     if n == 1:
#         return height * 2
#     for x in range(n):
#         listy.append(x+1)
#     print(listy)
#     for x in listy:
#         if x % 2 != 0:
#             height = height*2
#             print('height is now:', height)
#         else:
#             height += 1
#             print('height is now:', height)
#     return height
# print(utopianTree(6))

# def angryProfessor(k, a):
#     on_time, late = 0,0
#     for x in a:
#         if x <= 0:
#             on_time += 1
#         else:
#             late += 1
#     print('on time:',on_time)
#     print('late:',late)
#     if on_time >= k:
#         return "NO"
#     else:
#         return 'YES'

# print(angryProfessor(2,[0,-1,2,1]))

# def beautifulDays(i, j, k):
#     rangey = []
#     days = 0
#     for x in range(i,j+1):
#         rangey.append(x)
#     for x in rangey:
#         num = x
#         flip_num = 0
#         while num != 0:
#             digit = num % 10
#             flip_num = (flip_num * 10) + digit
#             num//= 10
#         if (x-flip_num) % k == 0:
#             days +=1
#     return days     
# print(beautifulDays(20,23,6))

# from math import floor

# def viralAdvertising(n):
#     likes = 2
#     total = 2
#     for x in range(n-1):
#         shares = likes*3
#         print('todays shares:',shares)
#         likes=shares//2
#         total += likes
#     return total
# print(viralAdvertising(5))

# def saveThePrisoner(n, m, s):
#     diff = m % n

#     if (diff + s -1) % n == 0:
#         return 0
#     else:
#         return (diff+s-1) % n

    

# print(saveThePrisoner(5, 2, 1))

# def matchingStrings(strings, queries):
#     results = []
#     for x in queries:
#         if x in strings:
#             results.append(strings.count(x))
#         else:
#             results.append(0)
#     return results

# print(matchingStrings(['ab', 'ab', 'abc'],['ab', 'abc', 'bc']))

# def plusMinus(arr):
    # Write your code here
    # less = 0
    # equal = 0
    # more = 0
    # for x in arr:
    #     if x < 0:
    #         less+=1
    #     elif x == 0:
    #         equal += 1
    #     else:
    #         more += 1
    # print("{:.6f}".format(more/len(arr)))
    # print("{:.6f}".format(less/len(arr)))
    # print("{:.6f}".format(equal/len(arr)))

# print(plusMinus([1,2,0,-1,-1]))

# def miniMaxSum(arr):
#     high = 0
#     low = sum(arr)
#     for x in arr:
#         summy = sum(arr)-x
#         if summy > high:
#             high = summy
#         if summy < low:
#             low = summy
#     print(low, high)

# print(miniMaxSum([1,3,5,7,9]))

# def timeConversion(s):

#     if s[-2] == 'P' and s[:2] != '12':
#         s = str(int(s[:2]) + 12) +s[2:]
#     if s[-2] == 'A'and s[:2] == '12':
#         s = '00' + s[2:]
#     return s[:-2]
# print(timeConversion('12:45:54PM'))

# def reverseBits(n):
#     flip =0
#     for x in range(32):
#         bit = (n >> 1) | 1
#         flip = flip | (bit << 31 -x)
#     return flip
        
# print(reverseBits(2147483647))

# def diagonalDifference(arr):
#     ltor = 0
#     rtol = 0
#     iter = 0
#     iter2 = -1
#     for x in range(len(arr)):
#         ltor += arr[x][iter]
#         iter += 1
#     for x in range(len(arr)):
#         rtol += arr[x][iter2]
#         iter2 -= 1
#     return abs(ltor - rtol)

# print(diagonalDifference([[1,2,3],[4,5,6],[9,8,9]]))

# def countingSort(arr):
#     counter = [0] * 100
#     for x in arr:
#         counter[x] += 1
#     return counter

# print(countingSort([63, 54, 17, 78, 43, 70, 32, 97, 16, 94, 74, 18, 60, 61, 35, 83, 13, 56, 75, 52, 70, 12, 24, 37, 17, 0, 16, 64, 34, 81, 82, 24, 69, 2, 30, 61, 83, 37, 97, 16, 70, 53, 0, 61, 12, 17, 97, 67, 33, 30, 49, 70, 11, 40, 67, 94, 84, 60, 35, 58, 19, 81, 16, 14, 68, 46, 42, 81, 75, 87, 13, 84, 33, 34, 14, 96, 7, 59, 17, 98, 79, 47, 71, 75, 8, 27, 73, 66, 64, 12, 29, 35, 80, 78, 80, 6, 5, 24, 49, 82]))

def pangram(s):

    # variable that is all alpha
    # iter over alphabet
    # if iter is not in the string , return 'not pangram' if
    # we get to the end w/o returning 'not pangram', we know it is a pangram.
    # but then we have to iterate through the enitre string very time. maybe
    #  something more efficient? also, make alpha lower. and skip spaces
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    s = s.replace(' ','')
    s = s.lower()
    for x in alpha:
        if x not in s:
            return 'not pangram'
    return 'pangram'

print(pangram('The quick brown fox over the lazy dog'))