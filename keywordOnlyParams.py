class A:
    def __init__(self, *, x):
        print(x)

class B(A):
    #TTP-06 should suggest fix and add super().__init__(x=x)
    def __init__(self, x):
        pass