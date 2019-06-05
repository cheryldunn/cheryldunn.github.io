def method_one():
    print("look I'm a method")

def method_two(name):
    print("about to call our first method for " +name)
    method_one()

method_two("Brandon")
