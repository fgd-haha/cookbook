"""
8.6_创建可管理的属性

你想给某个实例 attribute 增加除访问与修改之外的其他处理逻辑，比如类型检查或合法性验证。

解决方案:自定义某个属性的一种简单方法是将它定义为一个 property。
"""


class Person:
    """
    有三个相关联的方法，这三个方法的名字都必须一样。第一个方法是一
个 getter 函数，它使得 first name 成为一个属性。其他两个方法给 first name 属
性添加了 setter 和 deleter 函数。需要强调的是只有在 first name 属性被创建后，
后面的两个装饰器 @first name.setter 和 @first name.deleter 才能被定义。
property 的一个关键特征是它看上去跟普通的 attribute 没什么两样，但是访问它
的时候会自动触发 getter 、setter 和 deleter 方法。
    """

    def __init__(self, first_name):
        """
        在实现一个 property 的时候，底层数据 (如果有的话) 仍然需要存储在某个地方。
因此，在 get 和 set 方法中，你会看到对 first name 属性的操作，这也是实际数据保
存的地方。另外，你可能还会问为什么 init () 方法中设置了 self.first name 而
不是 self. first name 。在这个例子中，我们创建一个 property 的目的就是在设置
attribute 的时候进行检查。因此，你可能想在初始化的时候也进行这种类型检查。通
过设置 self.first name ，自动调用 setter 方法，这个方法里面会进行参数的检查，
否则就是直接访问 self. first name 了
        :param first_name:
        """
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


a = Person('Guido')
print(a.first_name)  # Calls the getter

a.first_name = 42  # Calls the setter, typeerror

