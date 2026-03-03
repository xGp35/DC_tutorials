# Import the pytest library
import pytest # type: ignore
import pandas as pd

# Define the fixture decorator
@pytest.fixture
# Name the fixture function
def prepare_data():
    return [i for i in range(10)]

# Create the tests
def test_elements(prepare_data):
    assert 9 in prepare_data
    assert 10 not in prepare_data

# Define the fixture for returning the length
@pytest.fixture
def list_length():
    return 10

# Define the fixture for a list preparation
@pytest.fixture
def prepare_list(list_length):
    return [i for i in range(list_length)]

#We can call th functions as variables because
#when the code runs using pytest from start to finish, any function with decorator @pytest.fixture runs first
#Once that has run it creates assigns the return value of the function to the function object
#so the function object acts like a vaiable object


def test_9(prepare_list):
    assert 9 in prepare_list
    assert 10 not in prepare_list


@pytest.fixture
def prepare_data():
    data = [i for i in range(10)]
    # Return the data with the special keyword
    yield data
    # Clear the data list
    data.clear()
    # Delete the data variable
    del data

def test_elements(prepare_data):
    assert 9 in prepare_data
    assert 10 not in prepare_data


@pytest.fixture
def data():
    df = pd.read_csv('/usr/local/share/games.csv')
    # Return df with the special keyword
    yield df
    # Remove all rows in df
    df.drop(df.index, inplace=True)
    # Delete the df variable
    del df

def test_type(data):
    assert type(data) == pd.DataFrame

def test_shape(data):
    assert data.shape[0] == 1512