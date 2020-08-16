"""让字典保持有序"""

from collections import OrderedDict, defaultdict
from pprint import pprint

d1 = OrderedDict()
d1['foo'] = 1
d1['bar'] = 2
d1['spam'] = 3
d1['grck'] = 4
pprint(d1)

d2 = dict()
d2['foo'] = 1
d2['bar'] = 2
d2['spam'] = 3
d2['grck'] = 4
pprint(d2)
