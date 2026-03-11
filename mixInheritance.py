class LoggingMixin:
    def log(self):
        print("log")


class A:
    def __init__(self):
        print("A")


class B(LoggingMixin, A):
    # TTP-17 super().__init__() should be added. No other changes
    def __init__(self):
        pass