#-*- coding: utf-8 -*-
from korean import hangul
from itertools import chain
import re
import sys

#파이썬2.x 한글 호환을 위해 sys 모듈 리로드

reload(sys)
sys.setdefaultencoding('utf-8')



"""
Trie 노드 클래스
"""
class TrieNode(object):
	def __init__(self, key, data=None):
		self.key = key
		self.data = data
		self.children = {}

"""
한글 자소를 기준으로 단어를 저장하는 Trie 클래스
"""
class TrieUTF8(object):
	def __init__(self):
		self.head = TrieNode(None)
	
	"""
	insert(self, string)
	단어 삽입 메소드
	"""
	def insert(self, word):
		word = unicode(word)
		current_node = self.head
		word_splitted = []
		#단어를 자소 단위로 분리 (초성, 중성, 종성)
		for char in word:
			consonants = hangul.split_char(char)
			word_splitted.append(consonants)
		#종성이 없는 경우를 필터링
		word_splitted = filter(lambda x: x != u'', list(chain(*word_splitted)))
		#Trie에 삽입
		for char in word_splitted:
			if char not in current_node.children:
				current_node.children[char] = TrieNode(char)
			current_node = current_node.children[char]
		current_node.data = word
		return 0

	"""
	prefix_search(self, string)
	접두사 기반 검색
	"""
	def prefix_search(self, prefix):
		prefix = unicode(prefix)
		current_node = self.head
		result = []
		subTrie = None
		prefix_splitted = []
		"""
		접두사를 자소 단위로 분리
		글자가 완성형이 아닌 경우 그대로 포함함 (ex: 'ㅆ') 
		"""
		for char in prefix:
			try:
				consonants = hangul.split_char(char)
				prefix_splitted.append(consonants)
			except:
				prefix_splitted.append((char))
		#종성이 없어서 발생하는 공백 문자 필터링	
		prefix_splitted = filter(lambda x: x != u'', list(chain(*prefix_splitted)))
		
		#BFS 기반으로 prefix 탐색
		for char in prefix_splitted:
			if char in current_node.children:
				current_node = current_node.children[char]
				subTrie = current_node
			else:
				return []

		#subTrie 내에서 완성형 단어 탐색		
		queue = list(subTrie.children.values())

		while queue:
			q = queue.pop()
			if q.data != None:
				result.append(q.data)
			queue += list(q.children.values())

		return result


def find_keywords(source='', prefix=''):

	if source == '' or prefix == '':
		return []

	source = str(source)
	
	#정규식을 이용해 공백문자와 한글을 제외한 모든 글자 삭제
	hangul_regex = re.compile('[^ ㄱ-ㅣ가-힣]+')
	source = hangul_regex.sub('', source)
	#공백 문자로 단어를 구분하여 Trie에 삽입
	word_list = source.split(u' ')
	
	trie = TrieUTF8()
	for word in word_list:
		trie.insert(word)

	#접두사 기반 검색 결과 반환
	return trie.prefix_search(prefix)

if __name__ == '__main__':

	for word in find_keywords('동해물과 백두산이 마르고 닳도록, 하느님이 보우하사 우리나라 만세~', ''):
		print word



