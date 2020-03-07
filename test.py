d = {
	'a': 0,
	'b': 1,
}

def foo(**d):
	print(d)
	print(d['a'])

foo(**d)
