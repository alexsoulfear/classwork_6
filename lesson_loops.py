# print('Hello world!')
# print('Hello world!')
# print('Hello world!')
# print('Hello world!')
# print('Hello world!')
import random

for i in range(10):
    if i % 2 == 0:
        print('Hello world!', i)
    else:
        print('Happy Pi day!', i)

for i in range(10, 20, 4):
    print('Iteration#:', i)

for i in range(100, 20, -5):
    print('Iteration#:', i)

for i in range(2, 101, 2):
    print('Iteration#:', i)

def sum_of_n(n):
    total_num = 0
    for i in range(1, n+1):
        # total_num = total_num + i
        total_num += i
    return total_num

print('Total num:', sum_of_n(100))
print('Total num:', sum_of_n(10))
print('Total num:', sum_of_n(1000))




# # i++; ++i;
# i += 1;
# i = i + 1;
print('--------------------')
for char in 'abc':
    print(char)

for digit in '3457143857304':
    print(digit)

for month in ['Jan', 'Feb', 'Mar']:
    print(month)

for week_day in ('Mo', 'Tu', 'Wd'):
    print(week_day)


def count_titles(text):
    total_count = 0
    for word in text.split(' '):
        word = word.strip('.,:!?')
        if word.istitle():
            print(word)
            total_count += 1
    return total_count


text = 'Ваши действия в режиме инкогнито будут недоступны другим пользователям этого устройства. Однако закладки и скачанные файлы сохранятся.'
print('Total count:', count_titles(text))


def camelize_var_name(var_name):
    result = ''
    for part_name in var_name.split('_'):
        result += part_name.capitalize()
    return result

print(camelize_var_name('snake_style_var'))
print(camelize_var_name('snake_style_very_long_var_name'))
print(camelize_var_name('a_b_c_d_e_f'))


def mean_whatever_on_n(n, lower_bound, upper_bound):
    total_num = 0
    for _ in range(n):
        rand_num = random.randint(lower_bound, upper_bound)
        print(rand_num)
        total_num += rand_num

    return total_num/n

print('Mean:', mean_whatever_on_n(12, 100, 200))
# print('Mean:', mean_whatever_on_n(12, 1000, 2000))
# print('Mean:', mean_whatever_on_n(12, 10, 20))
# print('Mean:', mean_whatever_on_n(12, -20, -10))
# print('Mean:', mean_whatever_on_n(12, 11, 22))


def min_of_n(n, lower_bound, upper_bound):
    # current_min = upper_bound
    current_min = float('inf')
    for i in range(n):
        rand_num = random.randint(lower_bound, upper_bound)
        print(rand_num)

        if current_min > rand_num:
            current_min = rand_num

    return current_min

print('#################')
print('Min:', min_of_n(12, -200, -100))


def max_of_n(n, lower_bound, upper_bound):
#    current_max = lower_bound
    current_max = -float('inf')
    for i in range(n):
        rand_num = random.randint(lower_bound, upper_bound)
        print(rand_num)

        if current_max < rand_num:
            current_max = rand_num

    return current_max
print('Max:', max_of_n(12, 20, 100))