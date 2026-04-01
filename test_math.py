from math_operations import add_numbers

def test_add_numbers():
    # This is the actual test the GitHub Action runner will execute
    assert add_numbers(10, 5) == 15
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0