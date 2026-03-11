class A:
    def __init__(self):
        pass


class B(A):
    # TTP-08 should have no warning 
    def __init__(self):
        super().__init__()