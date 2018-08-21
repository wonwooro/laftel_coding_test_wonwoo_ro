import read_numbers

if __name__ == "__main__":
	data = [[1], [1,3], [1,2,3], [1, 2, 3, 6, 8, 9, 10], [13, 14, 15, 16, 20, 23, 24, 25, 100]]
	for d in data:
		print (read_numbers.read(d))