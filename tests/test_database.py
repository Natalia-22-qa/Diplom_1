from conftest import *


class TestDatabase:

    def test_available_buns_are_3_true(self, mock_database):
        buns_list = mock_database.available_buns()
        assert len(buns_list) == 3

    def test_available_ingredients_are_6_true(self, mock_database):
        ingredients_list = mock_database.available_ingredients()
        assert len(ingredients_list) == 6

# pytest tests/test_database.py
