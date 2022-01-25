import json


def pick(l: list, index: int) -> int:
    return l[index]

d = {'key': 'value'}
# print(d)  # {'key': 'value'}

d['mynewkey'] = 'mynewvalue'

for i in range(10):
    d[i] = i

# print(d)  # {'key': 'value', 'mynewkey': 'mynewvalue'}

class Person:

    def __init__(self, name, age, b):
        self.__name = name
        self.__age = age
        self.__b = b

    def myfunc(self):
        print(f"Hello my name is {self.__name} i'm {self.__age} years old")

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

class B:

    def __init__(self, field):
        self.__field = field

    def get_field(self):
        return self.__field

p1 = Person("John", 36, B("fld"))
# p1.myfunc()

# json_object = json.dumps(p1, default=lambda o: o.__dict__, 
#             sort_keys=True, indent=4)
# print(json_object)

print(p1.to_json())
