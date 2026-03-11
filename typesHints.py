class A:
    def __init__(self, x: int):
        self.x = x


class B(A):
    # TTP-14 PEP-484 super().__init__() added. X type is untouched
    def __init__(self, x: int):
        pass