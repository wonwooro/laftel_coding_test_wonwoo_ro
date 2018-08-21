#-*- coding: utf-8 -*-
from itertools import groupby
from operator import itemgetter

"""
function read(list)
수 배열을 받아, 연속된 수열을 "N~M" 형태로 묶은 문자열로 변환하여 반환함.
"""
def read(data):
	#결과 문자열 선언 및 초기화.
	result = ""
	#연속된 수열을 저장하는 리스트.
	mapped = []
	"""
	연속된 수들은 수 배열 안에서 "인덱스 - 수"의 결과 값이 같음.
	따라서 연속된 수열들을 "lambda (i, x): i - x"를 통한 groupby로 구할 수 있음.
	"""
	for key, group in groupby(enumerate(data), lambda (i, x): i - x):
		mapped.append(map(itemgetter(1), group))

	#찾은 연속된 수열들을 문자열로 변환
	sect_num = len(mapped)
	for i in range(sect_num):
		sect_len = len(mapped[i])
		if sect_len >= 2:
			result += str(mapped[i][0]) + '~' + str(mapped[i][sect_len - 1])
		else:
			result += str(mapped[i][0])
		if i != sect_num - 1:
			result += ', '

	#결과 반환
	return result


if __name__ == "__main__":
	res = read([1, 2, 3, 6, 8, 9, 10])
	print res