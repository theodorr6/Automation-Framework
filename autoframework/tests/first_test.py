import pytest

@pytest.mark.usefixtures("init_driver")
class Test():

    def test_first(self):
        assert True
