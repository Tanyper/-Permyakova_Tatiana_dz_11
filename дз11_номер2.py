class Division:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль невозможно")


div = Division(10, 100)
print(Division.divide_by_null(10, 0))
print(Division.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))
