class calculator:
    """Prime check from ``prime_number_class_objects.py``.

    The loop is ``range(2, n - 1)``. For ``n < 3`` that range is empty, and
    the ``for``/``else`` path prints ``prime``.
    """

    def __init__(self, a):
        self.num1 = a

    def prime(self):
        for i in range(2, self.num1 - 1):
            if self.num1 % i == 0:
                print("not prime")
                break
        else:
            print("prime")
