"""
groupby() 方法使用。
"""
from itertools import groupby
from operator import itemgetter
from pprint import pprint

rows = [
    {'address': '中国，北京，大兴', 'date': '2020/01/03'},
    {'address': '中国，北京，海淀', 'date': '2020/02/02'},
    {'address': '中国，北京，朝阳', 'date': '2020/01/05'},
    {'address': '中国，北京，通州', 'date': '2020/01/23'},
    {'address': '中国，北京，通州', 'date': '2020/02/02'},
    {'address': '中国，北京，大兴', 'date': '2020/02/13'},
    {'address': '中国，北京，大兴', 'date': '2020/01/03'},
]

# 按照date对rows分组显示，使用groupby需要先对rows排序
rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('  ', i)


# 也可以直接使用字典，用空间换时间，不需要排序，更快
from collections import defaultdict

rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

pprint(rows_by_date)
