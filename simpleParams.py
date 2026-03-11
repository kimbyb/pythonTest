class A:
    def __init__(self, x):
        pass

class B(A):
    #TTP-01 should suggest fix and add super().__init__(x)
    def __init__(self, x):
        pass