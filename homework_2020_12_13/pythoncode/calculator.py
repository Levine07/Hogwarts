class Calculator(object):
    @staticmethod
    def add(a, b):
        return round(a + b, 14)

    @staticmethod
    def sub(a, b):
        return round(a - b, 14)

    @staticmethod
    def mul(a, b):
        return round(a * b, 14)

    @staticmethod
    def div(a, b):
        return round(a / b, 14)
