"""
8.8_子类中扩展 property

1. property, setter, deleter 全部重新定义
2. 仅扩展部分方法时，使用 class.property.setter
"""


class Person:
    def __init__(self, name):
        self.name = name
        # Getter function

    @property
    def name(self):
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    # Deleter function
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson1(Person):
    """
    property, setter, deleter 全部重新定义
    """

    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson1, SubPerson1).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson1, SubPerson1).name.__delete__(self)


s = SubPerson1('ha')
print(s.name)


class SubPerson2(Person):
    """
    仅扩展部分方法时，使用 class.property.[getter|setter|deleter]
    """

    @Person.name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson2, SubPerson2).name.__set__(self, value)

s = SubPerson2('he')
s.name = 'hehe'

