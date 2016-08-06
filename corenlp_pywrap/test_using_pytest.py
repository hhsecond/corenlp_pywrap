import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath)

import pywrap as p

class Test_common():
	cn = p.CoreNLP
	def test_localurl(self):
		assert '127.0.0.1' in self.cn.url\
			or 'localhost' in self.cn.url,\
			'script is pointing to cloud'
	def test_no_sentiments(self):
		assert 'SENTIMENT' not in map(
			str.upper, self.cn.annotator_full_list),\
			'Sentiment is not supported'

class Test_basic():
	pass