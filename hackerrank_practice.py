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

def sockMerchant(n, ar):
    # Write your code here
    pairs = 0
    used = []
    for x in ar:
        if x not in used:      
            pairs += round((ar.count(x) -ar.count(x) % 2) /2)
            used.append(x)
    return pairs

print(sockMerchant(7,[1,2,1,2,1,3,2]))



        
        
    