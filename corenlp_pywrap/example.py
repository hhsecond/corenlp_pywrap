import pywrap as p
cn = p.CoreNLP()
r = cn.arrange('This is Sherin, He is good but I am bad')
for key, val in r.items():
	print(key, val)