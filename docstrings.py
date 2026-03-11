class A:
    def __init__(self):
        pass


class B(A):
    # TTP-12 PEP-257 super().__init__() added after docstring
    def __init__(self):
        """Initialize B"""
        pass