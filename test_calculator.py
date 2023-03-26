import calculator

def test_addition():
    assert calculator.calculate("2 + 2") == 4

def test_subtraction():
    assert calculator.calculate("5 - 3") == 2

def test_multiplication():
    assert calculator.calculate("4 * 6") == 24

def test_division():
    assert calculator.calculate("10 / 2") == 5

def test_invalid_expression():
    try:
        calculator.calculate("2 + abc")
        assert False, "Exception not raised"
    except Exception as e:
        assert str(e) == "Invalid expression: 2 + abc"

if __name__ == '__main__':
    test_addition()
    test_subtraction()
    test_multiplication()
    test_division()
    test_invalid_expression()
    print("All tests pass") 
