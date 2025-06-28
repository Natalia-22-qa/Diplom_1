from unittest.mock import Mock
from praktikum.ingredient import Ingredient
import pytest
from praktikum.database import Database
from praktikum.burger import Burger
from data import Data
from praktikum.bun import Bun


@pytest.fixture
def new_bun(name, price):
    bun = Bun(name, price)
    return bun

@pytest.fixture
def new_ingredient(type_ing, name, price):
    ingredient = Ingredient(type_ing, name, price)
    return ingredient

@pytest.fixture
def new_burger():
    burger = Burger()
    return burger

@pytest.fixture()
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = Data.buns[0]
    mock_bun.get_price.return_value = Data.buns[1]
    return mock_bun

@pytest.fixture()
def mock_sauce():
    mock_sauce = Mock()
    mock_sauce.get_type.return_value = Data.sauces[0]
    mock_sauce.get_name.return_value = Data.sauces[1]
    mock_sauce.get_price.return_value = Data.sauces[2]
    return mock_sauce

@pytest.fixture()
def mock_filling():
    mock_filling = Mock()
    mock_filling.get_type.return_value = Data.fillings[0]
    mock_filling.get_name.return_value = Data.fillings[1]
    mock_filling.get_price.return_value = Data.fillings[2]
    return mock_filling

@pytest.fixture()
def mock_database():
    mock_database = Database()
    return mock_database

#conftest