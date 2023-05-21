class MyClass:
    def __init__(self, value):
        self.value = value

def process_list(my_list: list[MyClass]):
    for item in my_list:
        if not isinstance(item, MyClass):
            raise TypeError("Invalid item in the list")
        # Perform operations on the item

# Example usage
my_list = [MyClass(1), MyClass(2), MyClass(3)]
process_list(my_list)