from conftest import *


class TestBurger:

    def test_set_buns_success(self, new_burger, mock_bun):
        new_burger.set_buns(mock_bun)
        assert new_burger.bun == mock_bun

    @pytest.mark.parametrize('ingredient', [mock_sauce, mock_filling])
    def test_add_ingredient_success(self, new_burger, ingredient):
        new_burger.add_ingredient(ingredient)
        assert ingredient in new_burger.ingredients and len(new_burger.ingredients) == 1

    @pytest.mark.parametrize('index', [0, 1])
    def test_remove_ingredient_success(self, index, new_burger, mock_sauce, mock_filling):
        new_burger.add_ingredient(mock_sauce)
        new_burger.add_ingredient(mock_filling)
        remove_ingredient = new_burger.remove_ingredient(index)
        assert remove_ingredient not in new_burger.ingredients and len(new_burger.ingredients) == 1

    def test_move_ingredient_success(self, new_burger, mock_sauce, mock_filling):
        new_burger.add_ingredient(mock_sauce)
        new_burger.add_ingredient(mock_filling)
        new_burger.move_ingredient(0, 1)
        assert new_burger.ingredients[0] == mock_filling and new_burger.ingredients[1] == mock_sauce

    def test_get_price_success(self, new_burger, mock_bun, mock_sauce, mock_filling):
        new_burger.set_buns(mock_bun)
        new_burger.add_ingredient(mock_sauce)
        new_burger.add_ingredient(mock_filling)
        price = mock_bun.get_price()*2 + mock_sauce.get_price() + mock_filling.get_price()
        assert price == new_burger.get_price()

    def test_get_receipt_success(self, new_burger, mock_bun, mock_sauce, mock_filling):
        new_burger.set_buns(mock_bun)
        new_burger.add_ingredient(mock_sauce)
        new_burger.add_ingredient(mock_filling)
        new_burger.get_receipt()
        assert new_burger.get_receipt() == (f'(==== {mock_bun.get_name()} ====)\n'
                                            f'= sauce {mock_sauce.get_name()} =\n'
                                            f'= filling {mock_filling.get_name()} =\n'
                                            f'(==== {mock_bun.get_name()} ====)\n'
                                            f'\n'
                                            f'Price: {new_burger.get_price()}')

# pytest tests/test_burger.py
