class A:
    def __init__(self):
        pass


class B(A):
    # TTP-02 should suggest fix and add super().__init__()
    def __init__(self):
        pass