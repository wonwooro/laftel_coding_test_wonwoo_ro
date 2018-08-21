#-*- coding: utf-8 -*-
from autocomplete import find_keywords

def printElements(list):
	for item in list:
		print item,
	print ''

if __name__ == "__main__":
	input = "동해물과 백두산이 마르고 닳도록, 하느님이 보우하사 우리나라 만세~"
	prefix = ['ㅁ', '우린', '록한']
	for p in prefix:
		print "Prefix: %s >>" % p
		printElements(find_keywords(input, p)) 
		print "-------------"