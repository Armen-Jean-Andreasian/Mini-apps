import math


class Calculator:
    @staticmethod
    def taking_input():
        number_one = float(input("Enter a number. \n> "))

        operator_ = input(
            """Choose an operator:
----------------------
    +  : addition
    -  : subtraction
    /  : division
    *  : multiplication
    sq : squaring
    cb : cubing 
    rt : root division 
----------------------\n> """
        ).lower()
        number_two = float(input("Enter a second number. \n> "))

        result = Calculator.calculation(operator=operator_, number_1=number_one, number_2=number_two)

        return f"Result: {result}" if result else 'Wrong operator'

    @staticmethod
    def calculation(operator: str, number_1: float, number_2: float):
        if operator not in ("*", "/", "+", "-", "sq", "cb", "rt"):
            return False

        else:
            result_ = float()

            match operator:
                case '*':
                    result_ = number_1 * number_2

                case "/":
                    try:
                        result_ = number_1 / number_2
                    except ZeroDivisionError:
                        return 'Division by Zero is not allowed!'

                case "+":
                    result_ = number_1 + number_2

                case "-":
                    result_ = number_1 - number_2

                case "sq":
                    result_ = number_1 ** 2

                case  "cb":
                    result_ = number_1 ** 3

                case "rt":
                    result_ = math.sqrt(number_1)

            return result_


if __name__ == '__main__':
    print(Calculator.taking_input())
