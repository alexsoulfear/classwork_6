import math


def pretty_print(value):
    print_delimiter()
    print('Value:', value)
    print_delimiter('#', 20)


def print_delimiter(delimiter='*', num_repeat=40):
    print(delimiter * num_repeat)


def power(base, exp):
    print('Inside!')
    res = base ** exp
    return res

result = power(3, 4)
pretty_print(result)


def rectangle_square(length, width):
    return length * width

pretty_print(rectangle_square(10, 20))

print(math.cos(math.sin(math.pow(2, 3))))

my_pi = math.pi
def circle_square(radius):
    square = (radius ** 2) * my_pi
    return square


pretty_print(circle_square(5))


def add_and_multiply(a, b):
    add_result = a + b
    mult_result = a * b
    return add_result, mult_result

res1, res2 = add_and_multiply(2, 3)
print(res1, res2)


def many_params_func(*args):
    print(args[0])

# print(1, 2, 3, 4, 5, 6)
result_7 = print_delimiter()
print(result_7)