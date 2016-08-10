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

class Test_serverconnection():
	sc_obj = p.CoreNLP()
	cur_url = sc_obj.url_calc()
	r = sc_obj.server_connection(cur_url, 'This is Sherin')
	r = r.json()
	
	def test_return_type(self):
		assert isinstance(self.r, dict), 'arrange function should return a'\
		 'requests object which is convertable to dictionary'
	
	def test_r(self):
		assert 'sentences' in self.r, 'value should be there'
		assert 'corefs' in self.r, 'value should be there.'
		assert len(self.r) == 2, 'should not have more than one value'

	def test_sentences(self):
		self.rs = self.r['sentences']
		assert len(self.rs) == 1, 'only one list'