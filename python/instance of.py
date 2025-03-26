# Understanding isinstance() in Python

def demonstrate_isinstance_basics():
    # Basic integer check
    number = 10
    print(f"Is {number} an integer? {isinstance(number, int)}")  # True
    
    # Multiple type check
    decimal = 10.5
    print(f"Is {decimal} an int or float? {isinstance(decimal, (int, float))}")  # True

def demonstrate_inheritance():
    class Animal:
        pass
    
    class Dog(Animal):
        pass
    
    dog = Dog()
    print(f"Is dog an Animal? {isinstance(dog, Animal)}")  # True
    print(f"Direct type check: {type(dog) == Animal}")  # False
    print(f"Isinstance check: {isinstance(dog, Animal)}")  # True

def validate_numbers(a, b):
    """Example of type validation using isinstance"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float")
    return a + b

def filter_integers():
    """Example of filtering using isinstance"""
    mixed_list = [1, 'string', 3.14, None, 10]
    integers = [x for x in mixed_list if isinstance(x, int)]
    print(f"Filtered integers: {integers}")  # [1, 10]

def check_custom_class():
    """Example of checking custom class instances"""
    class MyCustomClass:
        pass
    
    obj = MyCustomClass()
    print(f"Is obj MyCustomClass instance? {isinstance(obj, MyCustomClass)}")  # True

if __name__ == "__main__":
    demonstrate_isinstance_basics()
    demonstrate_inheritance()
    
    try:
        print(validate_numbers(10, 20))  # Works
        print(validate_numbers("10", 20))  # Raises TypeError
    except TypeError as e:
        print(f"Error: {e}")
    
    filter_integers()
    check_custom_class()
