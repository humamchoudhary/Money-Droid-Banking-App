class Test:
    def __init__(self):
        self.name = "Test"
        return self


class Test2(Test):
    def __init__(self):
        self.Test = super().__init__()
        self.username = "Test2"


x = Test2()

print(type(x) is Test2)
