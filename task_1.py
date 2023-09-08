# import logging
# from datetime import datetime
#
# FORM = '{levelname} - {asctime} - {msg}'
# logging.basicConfig(level=logging.INFO, filename='datetime.log', encoding='utf-8',
#                     format=FORM, style='{')
# logger = logging.getLogger(__name__)
#
# MONTHS = ("", 'янв', 'фев', 'мар', "апр", "мая", "июн", "июл", "авг", "сен", "окт", "ноя", "дек")
# WEEKDAYS = ("по", "вт", "ср", "че", "пя", "су", "во")
#
#
# def get_date(string: str) -> datetime:
#     year = datetime.now().year
#     count, weekday, month = string.split()
#     month = MONTHS.index(month[:3])
#     weekday = WEEKDAYS.index(weekday[:2])
#     count = int(count[0])
#     logger.info(f'{count}, {weekday}, {month}, {year}')
#     spam_count = 0
#     for day in range(1, 31 + 1):
#         date = datetime(day=day, month=month, year=year)
#         if date.weekday() == weekday:
#             spam_count += 1
#             if spam_count == count:
#                 return date
#
#
# if __name__ == '__main__':
#     print(get_date('2-я пятница апреля'))
#     print(get_date('1-й четверг декабря'))
#     print(datetime.now().weekday())



# import logging
#
# FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'
# logging.basicConfig(level=logging.ERROR, filename='ZeroDivError.log', encoding='utf-8',
#                     format=FORMAT, style="{")
# logger = logging.getLogger(__name__)
#
#
# def func_div_two(a, b) -> float:
#     try:
#         res = a / b
#     except ZeroDivisionError as e:
#         logger.error(f'Ошибка деления числа {a} на число {b}')
#         return float('inf')
#     return res
#
#
# if __name__ == '__main__':
#     print(func_div_two(8, 0))


