class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)



print("__str__()")
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
      return f"{self.name}({self.age})"

  def my_func(self):
      print("My name is " + self.name)

p1 = Person("John", 36)

p1.my_func()
print(p1)


