# Import the pytest library
import pytest
from datetime import datetime

def multiple_of_two(num):
    if num == 0:
        raise(ValueError)
    return num % 2 == 0

def test_numbers():
    assert multiple_of_two(2) is True
    assert multiple_of_two(3) is False

def test_zero():    
    with pytest.raises(ValueError):
        multiple_of_two(0)

def get_unique_values(lst):
    return list(set(lst))

day_of_week = datetime.now().isoweekday()
condition_string = 'day_of_week == 6'
# Add the conditional skip marker and the string here
@pytest.mark.skipif(condition_string)
def test_function():
	# Complete the assertion tests here
    assert get_unique_values([1,2,3]) == [1,2,3]
    assert get_unique_values([1,2,3,1]) == [1,2,3]