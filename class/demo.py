"""

封装，继承， 多态
print(dir(math))  查看 math 模块的属性和方法

"""


class Animal:
    # 类属性（所有实例共享）
    species = "Unknown"  
    animal_count = 0  # 记录创建的 Animal 实例数

    def __init__(self, name, age):
        # 实例属性
        self.name = name          # 公有实例属性（外部可访问）
        self.__age = age          # 私有实例属性（外部无法直接访问）

        # 修改类属性（统计实例数量）
        Animal.animal_count += 1
    
    # 获取私有属性的方法（封装）
    def get_age(self):
        return self.__age
    
    # 修改私有属性的方法（封装）
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("年龄必须大于 0！")
    
    # 类方法（可以访问和修改类属性）
    @classmethod
    def set_species(cls, species):
        cls.species = species
    
    @classmethod
    def get_animal_count(cls):
        return cls.animal_count


    # 普通方法（实例方法）
    def make_sound(self):
        return "Some sound"
    



# 继承（子类）
class Dog(Animal):
    # 子类特有的类属性
    species = "Canine"  

    def __init__(self, name, age, breed):
        super().__init__(name, age)  # 继承父类属性、方法
        self.breed = breed           # 独有的属性
    
    # 重写父类方法（多态）
    def make_sound(self):
        return "Woof!"




# 另一个子类
class Cat(Animal):
    species = "Feline"

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        return "Meow!"




# 测试
a1 = Animal("Generic Animal", 5)
dog1 = Dog("Buddy", 3, "Labrador")
dog2 = Dog("Max", 4, "Bulldog")
cat1 = Cat("Kitty", 2, "Black")

# 访问实例属性
print(dog1.name)  
print(cat1.name)  

# 访问私有属性（错误）
# print(dog1.__age)  # AttributeError: 'Animal' object has no attribute '__age'

# 通过方法访问私有属性
print(dog1.get_age())

# 访问和修改类属性
print(f'类属性：....')
print(Animal.species)  
print(Dog.species)  

# 修改类属性
Animal.set_species("Mammal")
print(Dog.species)  
print(Cat.species)


# 调用方法
print(dog1.make_sound())  
print(f'///')

# 访问类方法和静态方法
print(Dog.get_animal_count())  # 统计创建的 Animal 对象数量

# 打印属性方法，
print('dir dog1: ', dir(dog1))
print('dir Dog', dir(Dog))




