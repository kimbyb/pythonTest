class A:
    def __init__(self, x, y):
        pass

class B(A):
    #TTP-03 should suggest fix and add super().__init__(x,y)
    def __init__(self, x, y):
        pass