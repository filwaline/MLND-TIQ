import helper

def question1(s,t):
	kmp = helper.KMP(t)
	return kmp.search(s)


def question2(a):
	return helper.dp(a)


def question3(file):
	G = helper.Graph(file)
	mst = helper.PrimMST(G)
	edges = {str(v):[] for v in xrange(G.V)}
	for i in xrange(1,G.V):
		v,w = mst.edges()[i].vertexes()
		weight = mst.edges()[i].weight()
		edges[str(v)].append((str(w),weight))
		edges[str(w)].append((str(v),weight))
	return edges
	


def question4():
	pass


def question5():
	pass


#################   TEST   #####################
def test1():
	testcases = [['', 'a'],
	['udacity', 'ad'],
	['test', 'bbb'],
	['vasbads',''],
	['Compress your one Python and one text file into a .zip, and submit.', ' one'],
	['Compress your one Python and one text file into a .zip, and submit.', 'one file']]

	print '#####################'
	print 'test question1\'s solution'
	for tc in testcases:
		print '----------------------'
		print 's: %s'%tc[0]
		print 't: %s'%tc[1]
		try:
			print question1(tc[0],tc[1])
		except RuntimeError:
			print 'null pattern'
		except SyntaxError:
			print 'non-ASCII character appears'
	print '----------------------'
	print '#####################'

def test2():
	testcases = ['agbdba','',',,,...','hello,world','Was it a car or a cat I saw?','put it up, please','A man, a plan, a canal, Panama!',
	'race car','Amor, Roma','stack cats','aabbcabbac','taco cat']

	print '#####################'
	print 'test question2\'s solution'
	for tc in testcases:
		print '----------------------'
		print 'string: %s'%tc
		print 'result: %s'%question2(tc)
	print '----------------------'
	print '#####################'

def test3():
	testcases = ['tinyEWG.txt','mediumEWG.txt']
	print '#####################'
	print 'test question3\'s solution'
	for tc in testcases:
		print '----------------------'
		print 'result: %s'%question3(tc)
	print '----------------------'
	print '#####################'

def test4():
	pass

def test5():
	pass

if __name__ == '__main__':
	#test1()
	#test2()
	test3()
	test4()
	test5()