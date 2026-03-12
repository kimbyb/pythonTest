class A:
    def __init__(self, *args, **kwargs):
        print("A")


class B(A):
    # TTP-24 super().__init__(*args, **kwargs) should be added. No other changes
    def __init__(self, x, *args, **kwargs):
        self.x = x