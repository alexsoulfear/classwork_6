import re

while True:
    date = input("Enter date [DD.MM.YYYY]: ")
    if re.match('([0-2][0-9]|3[01]).\d\d\.\d\d\d\d', date):
        date_lst = date.split('.')
        date_lst[1], date_lst[0] = date_lst[0], date_lst[1]
        print('.'.join(date_lst))
        break
    else:
        print('Incorrect date!')

