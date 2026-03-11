class A:
    pass

class B(A):
    # TTP-09 should have no warning
    def __init__(self):
        pass