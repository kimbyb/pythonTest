class A:
    def __init__(self, x=10):
        print(x)

class B(A):
    #TTP-05 should suggest fix and add super().__init__(x,y)
    def __init__(self):
        pass