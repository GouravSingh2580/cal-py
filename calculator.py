def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        raise Exception("Invalid expression: {}".format(expression))

if __name__ == '__main__':
    expression = input("Enter a mathematical expression: ")
    try:
        result = calculate(expression)
        print("Result: ", result)
    except Exception as e:
        print("Error: ", e)
