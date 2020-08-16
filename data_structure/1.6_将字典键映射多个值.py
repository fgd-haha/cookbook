"""在字典中将建映射到多个值上"""

from collections import defaultdict
from pprint import pprint

# defaultdict 会检查键不存在时，自动初始化
d = defaultdict(list)

d['a'].append(1)
d['b'].append(1)
d['a'].append(2)

pprint(d)
