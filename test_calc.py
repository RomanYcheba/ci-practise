import calc

def test_average():
	assert calc.average([1, 2, 3]) == 2.0
	assert calc.average([10, 20]) == 15.0

def test_empty_list():
	assert calc.average([]) == 0 # Это завалится с ошибкой
