def log(func):
    def wrapper(*args, **kwargs):
        print("Calling constructor")
        return func(*args, **kwargs)
    return wrapper


class A:
    def __init__(self):
        print("A")


class B(A):
    # TTP-16 super().__init__() should be added
    @log
    def __init__(self):
        pass

