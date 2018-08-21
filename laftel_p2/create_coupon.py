#-*- coding: utf-8 -*-
import time
import sha
from base64 import b32encode
from random import shuffle
from random import randrange
millitime = lambda: int(round(time.time() * 1000))

"""
function generate_prime_numbers (int, int)
구간 [lower, upper] 사이에 존재하는 모든 소수들의 배열을 생성하여 반환함.
"""
def generate_prime_numbers(lower, upper):
	prime_numbers = []
	for number in range(lower, upper):
		if number > 1:
			for i in range(2, int(number ** 0.5) + 1):
				if (number % i) == 0:
					break
			else:
				prime_numbers.append(number)
	return prime_numbers
"""
function create_coupon(int)
쿠폰 코드 리스트를 생성하여 반환함. (기본 10개)
쿠폰 코드 생성을 위해 SHA-1 알고리즘 사용.
"""
def create_coupon(number_of_coupons = 10):
	#최소 쿠폰 개수는 10개이므로, 쿠폰 수가 10 미만일 시 10으로 초기화.
	if number_of_coupons < 10: number_of_coupons = 10
	#쿠폰 코드 리스트 초기화.
	coupon_list = []
	"""
	다섯 자리 소수 리스트를 생성.
	다섯 자리 소수는 쿠폰 코드의 중복을 방지하기 위하여 사용. (그보다 적은 자리의 소수는 연번 발생의 우려가 있음)
	"""
	prime_numbers = generate_prime_numbers(10000, 99999)
	shuffle(prime_numbers)
	prime_len = len(prime_numbers)
	#SHA-1 베이스 키
	key = "This coupon was issued from Laftel in 2018-08-21. "
	#쿠폰 리스트 생성
	for i in range(number_of_coupons + 1):
		"""
		베이스 키에 적용될 증분 계산: 현재시간(밀리초) * 무작위 소수
		베이스 키에 더하여 쿠폰 코드 중복 생성을 방지
		"""
		p = randrange(0, prime_len - 1)
		hex_increment = hex(millitime() * prime_numbers[p])
		#SHA-1 해시 생성
		m = sha.new(key + str(hex_increment))
		"""
		쿠폰 코드는 종이에 인쇄하거나 손으로 쓸 수 있어야 하므로, 가독성을 위해 base32로 SHA-1 digest를 인코딩함.
		인코드된 digest (총 26자리) 에서 24자리를 취함. 
		"""
		encoded = b32encode(m.digest())[:24]
		#쿠폰 코드 가독성을 위해 4자리마다 하이픈 추가
		coupon = '-'.join(encoded[j : j + 4] for j in range(0, len(encoded), 4))
		coupon_list.append(coupon)
	#결과 반환
	return coupon_list


if __name__ == "__main__":
	for coupon in create_coupon(100000):
		print coupon