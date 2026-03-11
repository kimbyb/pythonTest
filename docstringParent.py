class A:
    def __init__(self, x):
        """Parent constructor"""
        self.x = x

class B(A):
    # TTP-13 PEP-257 super().__init__() added to child. Parent untouched
    def __init__(self, x):
        pass