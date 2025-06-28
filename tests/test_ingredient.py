from conftest import *


class TestIngredient:

    @pytest.mark.parametrize('type_ing, name, price', [Data.sauces, Data.fillings])
    def test_get_price_of_ingredient_true(self, type_ing, name, price, new_ingredient):
        assert new_ingredient.get_price() == price

    @pytest.mark.parametrize('type_ing, name, price', [Data.sauces, Data.fillings])
    def test_get_name_of_ingredient_true(self, type_ing, name, price, new_ingredient):
        assert new_ingredient.get_name() == name

    @pytest.mark.parametrize('type_ing, name, price', [Data.sauces, Data.fillings])
    def test_ingredient_name(self, type_ing, name, price, new_ingredient):
        assert new_ingredient.get_type() == type_ing

# pytest tests/test_ingredient.py
