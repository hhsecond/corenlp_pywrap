# adding main package path to syspath
import os, sys
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../core'))
if not path in sys.path:
    sys.path.insert(1, path)
del path


from pyco_nlp import CoreNLP as cn

def test_full_annotator_list_len():
    assert len(cn.annotator_full_list) == 15, 'number of full annotator list has been changed'
