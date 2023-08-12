import pytest
from account import *

class Test:
    def setup_method(self):
        self.a1 = Account('Jane')

    def teardown_method(self):
        del self.a1

    def test_init(self):
        assert self.a1.get_name() == 'Jane'
        assert self.a1.get_balance() == pytest.approx(0)
    
    def test_deposit(self):
        assert self.a1.deposit(-4) is False
        assert self.a1.get_balance() == pytest.approx(0)

        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == pytest.approx(0)

        assert self.a1.deposit(1.0) is True
        assert self.a1.get_balance() == pytest.approx(1.0)

    
    def test_withdraw(self):
        assert self.a1.withdraw(-5) is False
        assert self.a1.get_balance() == pytest.approx(0)

        assert self.a1.withdraw(0) is False
        assert self.a1.get_balance() == pytest.approx(0)

        assert self.a1.withdraw(150) is False
        assert self.a1.get_balance() == pytest.approx(0)
        self.a1.deposit(10)
        
        assert self.a1.withdraw(5.5) is True
        assert self.a1.get_balance() == pytest.approx(4.5)


    


    

