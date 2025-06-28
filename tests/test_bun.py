from conftest import *

class TestBun:

    @pytest.mark.parametrize('name, price', Data.all_buns)
    def test_get_name_of_bun_true(self, name, price, new_bun):
        assert new_bun.get_name() == name

    @pytest.mark.parametrize('name, price', Data.all_buns)
    def test_get_price_of_bun_true(self, name, price, new_bun):
        assert new_bun.get_price() == price

# pytest tests/test_bun.py
