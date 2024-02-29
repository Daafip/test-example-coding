from example import add
from example import subtract

def test_add():
	assert add(1,2)==3	

def test_substract():
	assert subtract(2,1)==1 

def helper():
	print('works')
