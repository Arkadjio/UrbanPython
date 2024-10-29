def test_function():
    print("Hello World")
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

a = test_function()
print(a)
b = inner_function
print(b)
