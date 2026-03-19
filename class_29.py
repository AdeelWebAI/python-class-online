#=====> getters and setters in python <========

class MyClass:
    def __init__(self,value):
        self._value = value
        
    def show(self):
        print(f"Value is {self._value}")
    # def value(self):
    #     return self._value
    @property
    def ten_value(self):
        return 10 * self._value

obj = MyClass(10)
print(obj.ten_value)
# obj.show()