# Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

import re


class MyDate():
    def __init__(self, datestr):
        yearnum, monthnum, daynum = self.parse_datestr(datestr)
        if MyDate.verify_ymd(yearnum, monthnum, daynum):
            self.yearnum = yearnum
            self.monthnum = monthnum
            self.daynum = daynum

    def __str__(self):
        return "MyDate(%04d-%02d-%02d)" % (self.yearnum, self.monthnum, self.daynum)

    # Первый, с декоратором @classmethod, должен извлекать число, месяц,
    # год и преобразовывать их тип к типу «Число».
    @classmethod
    def parse_datestr(cls, datestr):
        match = re.match(r'(\d{4})-(\d{2})-(\d{2})', datestr)  # ([12]\d{3})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])
        if match:
            return int(match.group(1)), int(match.group(2)), int(match.group(3))
        else:
            raise ValueError("date format " + datestr + " doesn't match pattern YYYY-MM-DD")

    # Второй, с декоратором @staticmethod, должен проводить валидацию числа,
    # месяца и года (например, месяц — от 1 до 12).
    @staticmethod
    def verify_ymd(yearnum, monthnum, daynum):
        if not (yearnum >= 1000 and yearnum <= 2999):
            raise ValueError("wrong year: " + str(yearnum))
        if not (monthnum >= 1 and monthnum <= 12):
            raise ValueError("wrong month: " + str(monthnum))
        if not (daynum >= 1 and daynum <= 31):
            raise ValueError("wrong day: " + str(daynum))
        return True


try:
    d = MyDate('3456-ЩЩ-ММММ')
    print(d)
except Exception as e:
    print(e)

try:
    d = MyDate('3456-12-31')
    print(d)
except Exception as e:
    print(e)

try:
    d = MyDate('1212-21-23')
    print(d)
except Exception as e:
    print(e)

try:
    d = MyDate('1456-12-41')
    print(d)
except Exception as e:
    print(e)

try:
    d = MyDate('2019-12-31')
    print(d)
except Exception as e:
    print(e)
