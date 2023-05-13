import doaiot_lab2_a.bmi as bmi

def test_bmi_uw():
    result = bmi.calc_bmi(1.73,40)
    assert(result == -1)
def test_bmi_nw():
    result = bmi.calc_bmi(1.73,60)
    assert(result == 0)
def test_bmi_ow():
    result = bmi.calc_bmi(1.73,85)
    assert(result == 1)