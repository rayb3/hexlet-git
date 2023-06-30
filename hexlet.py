import requests

# def has_upper_case(string):
#     return string.lower != string


# # print(has_upper_case("qWe"))
# def is_even(number):
#     return number % 1 == 0


# print(is_even(6))      # => True
# print(not is_even(10))

# print(False or '')
# result = 10 % 2 == 0 and 'yes' or 'no'  # 'yes'
# print(result)
# print(True or 'yes')


# def string_or_not(string):
#     return isinstance(string, str)


# print(string_or_not(True))


# def normalize_url(url):
#     if url[:7] == "http://":
#         url = "https://"+url[7:]
#     elif url[:8] != "https://":
#         url = "https://"+url

#     return url


# print(normalize_url(""))


# def print_numbers(number):
#     i=number
#     while i > 0:
#         print(i)
#         i-=1
# print_numbers(0)

# def join_numbers_from_range(number1,number2):
#     i=number1
#     sum=""
#     while i<=number2:
#         sum+=str(i)
#         i+=1
#     return sum

# print(join_numbers_from_range(2,5))

# a= "Qwqe"
# print(len(a))
# def my_substr(string,lenString):
#      result=""
#      i=0
#      while i<lenString:
#          result +=string[i]
#          i+=1
#      return result
# print(my_substr("qweqweqwe",4))

# def is_prime(number):
#     if number < 2:
#         return False

#     divider = 2

#     while divider <= number / 2:
#         if number % divider == 0:
#             return False

#         divider += 1

#     return True

# print(is_prime(5))

# def is_contains_char(string, char):
#     i=0
#     while i<len(string):
#         if (string[i].lower()==char) or (string[i].upper()==char):
#             return True
#         i+=1

# print(is_contains_char('Awesomeness', 'd'))
# def reverse_string(text):
#     # Начальное значение
#     result = ''
#     # char - переменная, в которую записывается текущий символ
#     for char in text:
#         # Соединяем в обратном порядке
#         result = char + result
#         print(char)
#     # Цикл заканчивается, когда пройдена вся строка
#     return result


# print(reverse_string('go!'))  # => '!og'

# def sum(numbers):
#     result = 0
#     for num in numbers:
#         result += int(num)

#     return result

# print(sum("12345"))  # 15
# def filter_string(string, char):
#     result = ""
#     for current_char in string:
#         if (current_char.lower() != char.lower()):
#             result += current_char

#     return result.strip()


# print(filter_string("I look back if you are lost", "i"))


# def sum_of_series(finish):
#     n = 1
#     while n <= finish:

#         n = n + 1


# sum_of_series(5)


# def is_palindrome(string):
#     reversed_string=""
#     for char in string:
#         reversed_string = char+reversed_string
#     if string.strip()==reversed_string.strip():
#         return True
#     return False
# print(is_palindrome(" radar"))

# def is_vowel(char):
#     vowels = 'aeiouyауоыиэяюёе'
#     return char.lower() in vowels

# def count_vowels(string):
#     count_char=0
#     for char in string:
#         if is_vowel(char):
#             count_char+=1
#     return count_char
# print(count_vowels("qweasd"))
# CONST= 2134
# CONST= 256
# print(CONST)
# string = 1,2,34
# print(string)

# name_and_age = ('Bob', 42)

# name=name_and_age[0]
# name  # 'Bob'

# print(name)

# def sort_pair(pair):
#     number1,number2=pair
#     if number1>number2:
#       (number1,number2)=number2,number1
#     return (number1,number2)

# print(sort_pair((5,2)))

# def survivor(n):
#     i=2
#     while i<=n/2:
#         if n % i == 0:
#             return False
#         i+=1
#     return True
# print(survivor(11))


# def massiv(string):
#     i=0
#     print(len(string))
#     while i<len(string):
#         if i%2==0 and i !=0:
#             string=string.replace(string[i],"")


#         i+=1
#     return string

# print(massiv("1234567891"))

# # def survivor(n):
# #     i=2
# #     while i<n:
# #         if n % i == 0:
# #             return False
# #         n-=n//i
# #         i+=1
# #     return True
# # print(survivor(5))


# string="1234567892"
# print(string[4::5])


# def is_palindrom(n):
#     b=bin(n)
#     b=str(b)
#     print(type(b))
#     print(b[2:])
#     b2=b[2:]
#     b2=b2[::-1]
#     print(b2)
#     return b[2:]==b2
# print(is_palindrom(7))

# string="qwe qwe qwe"

# print(" ".join(string.split(" ")[:2]))

# def minimumSum(num):
#     num = str(num)
#     num = sorted(num)

#     print(num)
#     print(num[0],num[2])
#     print(num[0]+num[2],num[1]+num[3])
#     print(num[0]+num[1],num[2]+num[3])
#     return int(num[0]+num[2])+int(num[1]+num[3])

# print(minimumSum(5021))
# string="qweqwrew123"
# num_list = [i for i in string]
# print(num_list)

# def runningSum(nums):
#     print(nums)
#     nums=nums.split(" ")
#     # for i in range(1,len(nums)):
#     #     #nums+=nums[i-1]
#     #     print(i)
#     #     nums[i]=nums[i]+nums[i-1]
#     return nums

# print(runningSum("qwewqewqewqe"))
# acc = (1, 2, 3, 4, 5, "123qwe")
# print(acc)


# def letter_multiply(text:str,letter:str,multiply:int) -> str:

#     text=text.replace(letter,letter*multiply)
#     return text
# print(letter_multiply("qweweq","e",4))

# def fib(num):
#     num0 = 0
#     num1 = 1
#     num2 = 0
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     i = 2
#     while i <= num:
#         num2 = num0+num1
#         num0 = num1
#         num1 = num2
#         i += 1

#     return num2


# print(fib(0))

# def binary_sum(first_bianry,second_binary):
#     result=int(first_bianry,base=2) + int(second_binary,base=2)
#     return (f'{result:b}')#bin(result)[2:]
# print(binary_sum("1001","10"))

# def fizz_buzz(begin, end):
#     result = ""
#     if begin==end:
#         return str(begin)
#     while begin <= end:
#         if begin % 3 == 0 and begin % 5 == 0:
#             result += "FizzBuzz "
#         elif begin % 3 == 0:
#             result += "Fizz "
#         elif begin % 5 == 0:
#             result += "Buzz "

#         else:
#             result += f'{str(begin)} '

#         begin += 1
#     return result.strip()


# print(fizz_buzz(11, 18))


# def is_vertical(line1):
#     x1=line1[0][0]
#     x2=line1[1][0]
#     y1=line1[0][1]
#     y2=line1[1][1]
#     if x1==x2 and y1!=y2:
#         return True
#     else:
#         return False
# def is_horizontal(line1):
#     x1=line1[0][0]
#     x2=line1[1][0]
#     y1=line1[0][1]
#     y2=line1[1][1]
#     if y1==y2 and x1!=x2:
#         return True
#     else:
#         return False
# def is_degenerated(line1):
#     x1=line1[0][0]
#     x2=line1[1][0]
#     y1=line1[0][1]
#     y2=line1[1][1]
#     if y1==y2 and x1==x2:
#         return True
#     else:
#         return False
# def is_inclined(line1):
#     x1=line1[0][0]
#     x2=line1[1][0]
#     y1=line1[0][1]
#     y2=line1[1][1]
#     if y1!=y2 and x1!=x2:
#         return True
#     else:
#         return False
# line1=(42, 100), (42, 100)
# print(is_vertical(line1))


# response = requests.get('https://myodds.bet/')
# result=response.json()
# print(response.text)

# response10=requests.get('https://myodds.bet/')
# print(response10.text)

# def rotate_left(triple):
#     my_list = list(triple)
#     #my_list.append(my_list.pop(0))
#     print(my_list.pop(0))
#     return (my_list)

# def rotate_right(tuple):
#     tuple0, tuple1, tuple3 = tuple
#     return (tuple3, tuple0, tuple1)
# tuple=('a','b','c')
# print(rotate_right(tuple))


# def dif(a,b):

#     #print(360%(b-a))
#     #print(b-a%360)
#     print((b-a)%360)
#     return min(((a-b)%360),((b-a)%360))
# print(dif(0,190))

# def is_power_of_three(num):
#     if num < 1:
#         return False
#     while num%3==0:
#         num/=3
#     if num==1:
#         return True
#     else:
#         return False


# print(is_power_of_three(27))

# def is_happy_ticket(string_num):

#     if len(string_num)%2!=0:
#         return False
#     half_string=int(len(string_num)/2)

#     sum1=0
#     for num in string_num[:half_string]:
#         sum1+=int(num)
#     print(sum1)
#     sum2=0
#     for num in string_num[half_string:]:
#         sum2+=int(num)
#     print(sum2)
#     print(range(5))
#     return sum1==sum2
# print(is_happy_ticket("2222"))

# def is_happy_ticket(string_num):

#     if len(string_num)%2!=0:
#         return False
#     first_part=string_num[:len(string_num)//2]
#     second_part=string_num[len(string_num)//2:]
#     sum_firt_part=0
#     sum_second_part=0
#     for i in range(len(string_num)//2):

#         sum_firt_part+=int(first_part[i])
#         sum_second_part+=int(second_part[i])

#     return sum_firt_part==sum_second_part
#     print(first_part)
#     print(second_part)
#     # sum1=0
#     # for num in string_num[:half_string]:
#     #     sum1+=int(num)
#     # print(sum1)
#     # sum2=0
#     # for num in string_num[half_string:]:
#     #     sum2+=int(num)
#     # print(sum2)
#     # print(range(5))
#     # return sum1==sum2
# print(is_happy_ticket("123456"))

# def is_perfect(num):
#     i=1
#     sum=0
#     if num<=0:
#         return False
#     while i<=num//2+1:
#         if num%i==0:
#             sum+=i
#         i+=1
#     return sum==num
# print(is_perfect(6))
# def invert_case(string):
#     result_string = ""
#     for char in string:
#         if string != " ":
#             if char == char.upper():
#                 result_string += char.lower()
#             else:
#                 result_string += char.upper()
#     return result_string


# print(invert_case("qweWE%"))

# def sum_of_square_digits(num):
#     sum=0
#     for char in str(num):
#         sum+=int(char)**2
#     return sum

# def is_happy_number(num):
#     if  num <10:
#         num=num**2
#     i=0
#     while i < 10:
#         num=sum_of_square_digits(num)
#         if num==1:
#             return True
#         i+=1
#     return False


# #print(sum_of_square_digits(49))
# print(is_happy_number(3))

# def encrypt(string):
#     result_string=""
#     i=0
#     while i< len(string):
#         if i+1!=len(string):
#             result_string+=f'{string[i+1]}{string[i]}'
#         else:
#             result_string+=f'{string[i]}'
#         i+=2
#     return result_string
# print(encrypt("qwe rf"))
# list_of_nums = [1, 2, 3]
# def is_list(list_of_nums):

#     return isinstance(list_of_nums,list)
# print(is_list(list_of_nums))

# import math


# def get_square_roots(num):
#     list_roots = []
#     if num == 0:
#         list_roots.append(0)
#     elif num < 0:
#         return list_roots
#     else:
#         list_roots.append(-  math.sqrt(num))
#         list_roots.append(round(math.sqrt(num),2))
#     return list_roots


# print(get_square_roots(54))

# def get_range(num):
#     i=0
#     listnum=[]

#     while i < num:
#         listnum.append(i)
#         i+=1
#     return listnum
# print(get_range(-1))


# t = ([], [], []) * 3
# print(t)  # => ([], [], [], [], [], [], [], [], [])
# t[0].append(42)
# t[4].append(0)
# print(t)  # => ([42], [0], [], [42], [0], [], [42], [0], [])

# import copy
# l = [1,2,3,4,5]
# l_copy = l  # копируется внешний список, но не внутренние списки
# l_copy[0] = 55
# print(l)  # => [[0, 2], [3, 4]]
# print(l_copy)  # => [[0, 2], [3, 4]]


# a = []
# pair = (a, a,a)
# a.append(1)
# a.append(2)

# print(pair)  # => ([1, 2], [1, 2])


# l = [42]
# l.append(43)
# l.append(44)
# l[2] = l[0]
# l = l * 2
# print(l)

# def duplicate(list:list):
#     list*=2
#     return

# list=[1,2]
# duplicate(list)
# #print(list)
# list2=list.copy()
# list[0]=111
# print(list)
# print(list2)

# print("BRAKADABRA"[0:6][0:6][:-1])
# ab=[1,2,3]
# ab.extend([1,2,4,56])
# print(ab)
# def mod2(x):
#     return x % 2

# l = [1, 2, 3, 6, 5, 4]
# l.sort(key=mod2)
# print(l)  # => [2, 6, 4, 1, 3, 5]

# def rotate(list):
#     print(list)
#     if list!=[]:
#         list.insert(0,list.pop(-1))

#     return list

# print(rotate([1,2,3]))

# def rotated_left(data):
#     print(data)

#     return data[1:] + data[:1]

# def  rotated_right(data):
#     print(data)
#     return data[-1:] + data[:-1]
# print(rotated_right([1,2,3,4]))

# def find_index(value,items):
#     result=None
#     for i,item in enumerate(items):
#         if item==value:
#             result=i
#             break
#     return result

# print(find_index("b",["abs","b","c","b"]))


# def find_index(value, items):
#     for index, item in enumerate(items):
#         #print(index)
#         if item==value:
#             return index
# def find_second_index(value,items):
#     i=iter(items)

#     first_index=find_index(value,i)
#     if first_index==None:
#         return None
#     print(first_index)
#     second_index=find_index(value,i)
#     if second_index==None:
#         return None
#     print(second_index)
#     return first_index+second_index+1
# string="adb"
# print(find_second_index("b",string))

# def find_index(value, items):
#     count=0
#     for index, item in enumerate(items):
#         #print(index)
#         if item==value:
#             count+=1
#         if count==2:
#             return index


# string="adbcgb"
# print(find_index("b",string))

# def triangle(num):
#     s=[]
#     for i in range(num+1):
#         row=[1]*(i+1)
#         #print(row)
#         for j in range(i+1):
#             if j!=0 and j!=i:
#                 row[j]=s[i-1][j]+s[i-1][j-1]

#         s.append(row)

#     return s

# print(triangle(4))

# def triangle(row):
#     line = [1]
#     for i in range(row):
#         print(line[i])
#         line.append(int(line[i] * ((row - i) / (i + 1))))
#     return line
# print(triangle(4))

# def summary_ranges(items):
#     if items==[] or items==[1]:
#         return []
#     result=[]
#     for i,item in enumerate(items):
#         if  i!=len(items)-1:
#             if items[i+1]==items[i]+1:
#                 #if items[i] not in result:
#                 result.append(items[i])
#                 result.append(items[i+1])

#     for i,item in enumerate(result):
#         if i!=len(result)-1 and result[i]==result[i+1]:
#             result.pop(i)
#             #result.pop(i+1)
#     print(result)

#     result_str=str(result[0])

#     for i,item in enumerate(result):
#         if i!=len(result)-1 and result[i]+1!=result[i+1]:
#             result_str+="->"
#             result_str+=str(result[i])+" "
#             result_str+=str(result[i+1])
#     result_str+="->"+str(result[-1])
#     print(result_str)
#     result_list=[]
#     # for i, char in enumerate(result_str):
#     #     if i%2==0:
#     #         result_list.append(result_str[i]+result_str[i+1])
#     result_list=result_str.split(" ")
#     return result_list

# print(summary_ranges([1, 1, 3, 4, 5, -6, 8, 9, 10, 12, 14, 14]))


# def summary_ranges(numbers):
#     if not numbers:
#         return []

#     ranges = []
#     current_sequence = [numbers[0]]
#     sequences = [current_sequence]

#     for x, y in zip(numbers, numbers[1:]):
#         if (y - x) == 1:
#             current_sequence.append(y)
#         else:

#             current_sequence = [y]
#             sequences.append(current_sequence)

#     # здесь [0, 1, 2, 7, 5, 6] уже преобразован
#     # в [[0, 1, 2], [7], [5, 6]]

#     for sequence in sequences:
#         print(sequence)
#         if len(sequence) > 1:
#             first, last = sequence[0], sequence[-1]
#             ranges.append(f'{first}->{last}')

#     return ranges

# print(summary_ranges([1,2,3,7,5,6,1,2,3,4]))

# def length_of_last_word(string):
#     if not string:
#         return 0
#     list_of_string=string.split()

#     print(list_of_string)
#     if not list_of_string:
#         return 0
#     return len(list_of_string[-1])

# print(length_of_last_word(''))


# str="qwert qweqwe"
# str=str.split()
# str=" ".join(str)
# print(str)

# def multiply(first_m,second_m):
#     result=[]
#     for i,item_a in enumerate(first_m):
#         for j,item_b in enumerate(second_m):
#             print(first_m[i][j])
#             #print(second_m[i][j])
#             result.append(item_a+item_b)

#     # if len(a)>len(b):
#     #     combine_m=
#     return result

# a=[[1,2],[3,4]]
# b=[[1,3],[4,5]]
# print(multiply(a,b))

# first_matrix=[[1,2],[3,4]]
# second_matrix=[[7,3],[1,5]]
# length = len(first_matrix)
# result_matrix = [[0 for i in range(length)] for i in range(length)]
# for i in range(length):
#   for j in range(length):
#     for k in range(length):
#        result_matrix[i][j] += first_matrix[i][k] * second_matrix[k][j]

# print(result_matrix)

# def is_unique(word):
#     for x in word:
#         if word.count(x)>1:
#             return False
#     return True

# def find_longest(word):
#     answer=0
#     for i in range(len(word)):
#         for j in range(i,len(word)):
#             substring=word[i:j+1]
#             if is_unique(substring):
#                 answer=max(answer,len(substring))
#     return answer

# print(find_longest("qwerr"))

# def remove_char_from_str(list:list,ex_char:str)->list:
#     result_list=[]

#     for item in list[:]:
#         result_word=[]

#         for char in item:
#             if char!=ex_char:
#                 result_word.append(char)
#         result_list.append(''.join(result_word))
#         print(print(''.join(result_word)))
#     return result_list

# print(remove_char_from_str(["qwe","wqwsaas","fwefewfew"],"q"))

# def enlarge(image):

#     line_image=[]
#     for item in image:

#         str_result=''
#         for char in item:
#             str_result+=char*2

#         line_image.append(str_result)
#     print(line_image)
#     for item in line_image:
#         print(item)
# def show(image):
#     for line in image:
#         print(line)


# def enlarge(image):
#     result_image = []
#     if not image:
#         return []
#     for line in image:
#         str_line = ""
#         for char in line:
#             str_line += char*2
#         result_image.append(str_line)
#         result_image.append(str_line)
#     return result_image

# def enlarge(image):
#     output = []
#     for line in image:
#         str_line=""
#         for pixel in line:
#             # expand horizontally
#             str_line+=pixel*2
#         #print(row)
        
#         #print(row)
#         # expand verticaly
#         output.extend([str_line,str_line])
#         print(output)
#     return output
# frame = [
#     '* *',
#     '**'
# ]
# #print(enlarge(frame))
# show(enlarge(frame))



# def transposed(matrix):
    
#     result_list=[]
#     result=[]

#     for i in range(len(matrix[0])):
#         result_list=[]
#         for j in range(len(matrix)):
#             result_list.extend([matrix[j][i]])
            
#         result.append(result_list)
#     for item in result:
#         print(item)
#     return result

   
#     result=[[matrix[i][j]for j in range(len(matrix))]
#             for i in range(len(matrix[0]))]
#     print(result)
#     for item in result:
#         print(item)    
#     return result    
    


# m1=[[1,2],[4,6],[6,7]]
# #m2=[[1,2,3],[3,4,5],[4,5,9]]

# for item in m1:
#     print(item)

# transposed(m1)
# def transposed(matrix):
#     result = []
#     #for item in matrix:
#     for column in zip(*matrix):
#         print(column)
#         result.append(list(column))
#     print(result)
#     return result

# def rpn_calc(rpn_list:list)->int:
#     result_list=[]

#     print(rpn_list)
#     for item in rpn_list:
#         if item not in ["+","-","*","/"]:
#             result_list.append(item)
#         else:
#             right=result_list.pop()
#             left=result_list.pop()
#             if item=="+":
#                 result_list.append(left+right)
#             if item=="-":
#                 result_list.append(left-right)
#             if item=="*":
#                 result_list.append(left*right)
#             if item=="/":
#                 result_list.append(left/right)

#     return result_list[0]

# print(rpn_calc([7, 2, 3, '*', '-']))

# def chuncked(number,seq):
#     result=[]
#     seq[:number]
#     for i,item in enumerate(seq):
#         if i != number:
#             result+=item
#             seq.replace(item,"")
#         else: break
#     print(seq)
#     return result

# print(chuncked(2,"qwe123"))

# def chunked(number,seq):


#     if seq==[]:
#         return []
#     elif seq=="":
#         return []
#     elif number>=len(seq):
#         return [seq]

#     chunk_list=[]
#     for i in range(0,len(seq),number):
#         print(i)
#         chunk_list+=[seq[i:i+number]]
#     return chunk_list


# print(chunked(4,''))
# def mirror_matrix(matrix):
#     if matrix==[]:
#         print([])
#     elif len(matrix[0])==1:
#         print(matrix)
#     else: 

#         if len(matrix[0])%2==0:
#             half_len=len(matrix[0])//2+1
#             print(half_len)
#             for item in matrix:
#                 delimetr=1
#                 for j in range(len(item)):
#                     if j+2>half_len:
#                         item[j]=item[j-delimetr]
#                         delimetr+=2
#         else:
#             half_len=len(matrix[0])//2+1
#             print(half_len)

#             for item in matrix:
#                 delimetr=2
#                 for j in range(len(item)):
#                     if j+1>half_len:
#                         item[j]=item[j-delimetr]
#                         delimetr+=2
#         print(matrix)
# l = [
#             ['aa', 'bb', 'cc','dd',22,66],
#             ['11', '22', '33','dd',66,22],
#         ]

# 3
# 4
# 5
# 6
# 7
# # BEGIN
# def mirror_matrix(matrix):
#     if matrix:
#         half_len = len(matrix[0]) // 2
#         print(half_len)
#         for line in matrix:
#             line[half_len:] = line[-half_len-1::-1]
#     print(matrix)
# # END

# mirror_matrix(l)

# def hamming_weight(num):
#     b_num=bin(num)[2:]
#     sum_b=0
#     for char in b_num:
#         if char!="0":
#             sum_b+=int(char)
#     return sum_b
# def hamming_weight(x):
#     s = ''
#     while x:
#         x, r = divmod(x, 2)
#         print(x,r)
#         s += str(r)
#     return s
# print(hamming_weight(101))


    



