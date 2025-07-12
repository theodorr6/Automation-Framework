import pytest

@pytest.mark.usefixtures("init_driver")
class Test:

    def test_log_in(self, log_in):
        """Verify user can log in."""
        assert log_in.get_presence_of_confirm_message()
