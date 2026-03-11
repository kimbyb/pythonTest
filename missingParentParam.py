class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class B(A):
    # TTP-23 Should correct the __init__ and add y. Should insert  super().__init__(x, y)
    def __init__(self, x):
        self.x = x