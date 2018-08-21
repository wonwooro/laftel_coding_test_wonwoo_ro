from create_coupon import create_coupon


if __name__ == "__main__":
	data = 100000
	for coupon in create_coupon(data):
		print coupon