class A:
    def __init__(self, x, /):
        print("A:", x)

class B(A):
    #TTP-07 should suggest fix and add __init__(self, x, /):  super().__init__(x)
    def __init__(self, x):
        print("B:", x)
        pass

B(5)