class A:
    def __init__(self, *, x: int):
        self.x = x


class B(A):
    # TTP-15 PEP-484 super().__init__(x=x) added. X type is untouched
    def __init__(self, x: int):
        pass