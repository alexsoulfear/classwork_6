s = "I'm learning Python"
print(s, type(s))

s2 = '''
abc
def
ghj
'''
print(s2, type(s2))

"""
My comment line1
My comment line2 
My comment line3 
"""

path = 'C:\\temp\\new\\folder'
path2 = r'C:\temp\new\folder'
print(path)
print(path2)


s3 = 'My favourite symbol is: \u26BD'
print(s3)


# wave  = "~"
# boat = "\U0001F6A3"
# seagull = "\u033C"
# fish = "\U0001F41F"
# penguin = "\U0001F427"
# wale = "\U0001F40B"
# octopus = "\U0001F419"
#
#
# row = wave*10 + boat + wave*15 + "\n"
# fish_row = wave*4 + fish + wave*21 + "\n"
# wale_row = wave*10 + wale + wave*15 + "\n"
# penguin_row = wave*7 + penguin + wave*18 + "\n"
# octopus_row = wave*17 + octopus + wave*8 + "\n"
#
# sea = (row + fish_row + wale_row + penguin_row + octopus_row)
# print (sea)



s4 = 'Hillel'
print(s4[0])
print(s4[0:3])
print(s4[:3])
print(s4[3:0])
print(s4[3:])
print(s4[3:200])
print(s4[:200])
print(s4[:])
print(' ')

       #01234567
time = '09:02:01'
hours = int(time[:2])
print(hours)
minutes = int(time[3:5])
print(minutes)
seconds = int(time[6:])
print(seconds)

total_seconds = hours*(60*60) + minutes*60 + seconds
print(total_seconds)

time = '9:12:1'
lst = time.split(':')
print(lst)
print(type(lst))
hours   = int(lst[0])
minutes = int(lst[1])
seconds = int(lst[2])
total_seconds = hours*(60*60) + minutes*60 + seconds
print(total_seconds)

str = 'abcd'
var1 = 42
print(type(var1))
var1 = '42'
print(type(var1))
print(len('a'))
print(len(''))

s1 = 'Hillel'
print(s1[ 1: 3])
print(s1[-5:-3])
print(s1[1:-3])
print(s1[-5:3])

print(s1[-2:])
print(s1[:2])

s2 = '__init__'
print(s2[2:-2])

s3 = list('abababababab')
print(s3[:])
print(s3[::])
print(s3[::1])
print(s3[::2])
print(s3[1::2])
print(s1[::-1])
print(s1)