"""
通过公共键对字典列表排序

itemgetter函数的使用
"""

rows = [
    {'fname': 'haha', 'lname': 'hehe', 'uid': 101},
    {'fname': 'taha', 'lname': 'cehe', 'uid': 102},
    {'fname': 'yaha', 'lname': 'behe', 'uid': 103},
    {'fname': 'uaha', 'lname': 'cehe', 'uid': 104},
    {'fname': 'iaha', 'lname': 'hyhe', 'uid': 106},
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
# 也可以使用lambda表达式，不过itemgetter效率更高 rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)

print(max(rows, key=itemgetter('uid')))
