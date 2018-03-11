a = 10
b = 20

if b != 0:
    result = a / b
    print('Result:', result)
else:
    print('Division be zero error!')

if b == 0:
    print('Division be zero error!')
else:
    result = a / b
    print('Result:', result)


age = 12
adult_allowed_age = age > 16

if adult_allowed_age:
    print('Movie is allowed to watch')
else:
    print('Movie is NOT allowed to watch')


def is_zero(number):
    result = number == 0
    if result:
        return True
    else:
        return False
    # return result

b = 0
if is_zero(b):
    print('b is zero')
else:
    print('b is NOT zero')

name = 'Google'
if 'e' in name or 'E' in name:
    print('INSIDE')

if 'e' in name.lower():
    print('INSIDE')



def is_millennial(year_of_birth):
    if year_of_birth >= 1985 and year_of_birth <= 2000:
        return True
    else:
        return False


if is_millennial(1985):
    print('I\'m millenial!')
else:
    print('I\'m NOT millenial!')

number = ''
#if number:
if number != '':
    print('Is interpreted as True:', number)
else:
    print('Is interpreted as False:', number)



def is_leap_year(year) -> bool:
    # if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    #     return True
    # else:
    #     return False
    # return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


for i in range(2100):
    print('%d is leap year: %s' % (i, is_leap_year(i)))


data = input('Enter your name: ')
print(data)
age = int(input('Enter your age: '))
print(age, type(age))
height = float(input('Enter your height: '))
height = height
print(height, type(height))
