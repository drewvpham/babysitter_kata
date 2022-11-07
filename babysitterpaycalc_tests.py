from babysitterpaycalc import pay_calc

def test_should_pay_12_for_one_regular_hour_shift():
    assert pay_calc(5, 6, 6) == 12

def test_should_pay_24_for_two_regular_hours():
    assert pay_calc(5, 7, 7) == 24

def test_should_pay_8_for_one_bedtime_hour_before_midnight():
    assert pay_calc(5, 6, 5) == 8

def test_should_pay_20_for_one_hour_each_regular_and_bedtime_before_midnight():
    assert pay_calc(5, 7, 6) == 20

def test_should_pay_16_for_one_hour_worked_after_midnight():
    assert pay_calc(12, 1, 4) == 16

def test_should_pay_32_for_two_midnight_hours():
    assert pay_calc(12, 2, 4) == 32