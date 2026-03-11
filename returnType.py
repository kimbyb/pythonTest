class A:
    def __init__(self, x: int) -> None:
        self.x = x


class B(A):
    # TTP-22 Should insert super().__init__(x) without change of returns
    def __init__(self, x: int) -> None:
        self.x = x