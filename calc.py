def average(numbers):
	# Ошибка: если список пуст, будет ZeroDivisionError
	return sum(numbers) / len(numbers)

if __name__ == "__main__":
	test_data = [10, 20, 30, 40]
	print(f"Среднее: {average(test_date)}")

