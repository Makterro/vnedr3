import pytest
from main import calculate_monthly_payment

def test_calculate_monthly_payment():
    assert calculate_monthly_payment(100000, 20, 20) == 1698.82
