########################### question 1 ###################################
class KMP:
	def __init__(self,pattern):
		self.pattern = pattern
		self.M = len(pattern)
		self.R = 256 # ASCII 

		if self.M == 0:
			raise RuntimeError

		# init DFA
		self.dfa = [[0 for m in xrange(self.M)] for r in xrange(self.R)]
		self.dfa[ord(self.pattern[0])][0] = 1
		X = 0 # restart state

		# construct DFA
		for j in xrange(1,self.M):
			for r in xrange(self.R):
				self.dfa[r][j] = self.dfa[r][X] 			
			self.dfa[ord(self.pattern[j])][j] = j + 1	
			X = self.dfa[ord(self.pattern[j])][X]       # update restart state


	def search(self,text):
		j = 0
		for i in xrange(len(text)):
			j = self.dfa[ord(text[i])][j]
			if j == self.M:
				return True
		return False

##########################################################################




######################## question 2 ##########################################
import re
def dp(string):
	a = re.sub(r'\W',"",string) 
	a = a.lower()
	N = len(a)
	state = [[None for i in xrange(N)] for j in xrange(N)]

	for i in xrange(N):
		state[i][i] = 1

	step = 1
	longest = 0
	p,q = 0,1
	while step < N:
		for i in xrange(N):
			try:
				if a[i:i+step] == a[i+step:i:-1]:
					state[i][i+step-1] = step + 1
					if step + 1 > longest:
						longest = step + 1
						p,q = i,i+step+1
				else:
					state[i][i+step-1] = max(state[i][i+step-2],state[i+1][i+step-1])
			except IndexError:
				break
		step += 1

	return a[p:q] 

####################################################################




###################### question 3  ######################################
import heapq
class PriorityQueue:
	def __init__(self):
		self.hq = []

	def push(self,item):
		heapq.heappush(self.hq,item)

	def popMin(self):
		return heapq.heappop(self.hq)

	def isEmpty(self):
		if len(self.hq) > 0:
			return False
		return True

class UnionFind:
	def __init__(self,N):
		self.ID = [i for i in xrange(N)]
		self.wr = [1 for i in xrange(N)] # root weight
		self.N = N
		self.count = N

	def find(self,p):
		if self.ID[p] == p:
			return p
		else:
			self.ID[p] = self.find(self.ID[p])
			return self.ID[p]


	def union(self,p,q):
		pRoot = self.find(p)
		qRoot = self.find(q)
		if pRoot == qRoot:
			return
		if self.wr[pRoot] > self.wr[qRoot]:
			self.ID[qRoot] = pRoot
			self.wr[pRoot] += self.wr[qRoot]
		else:
			self.ID[pRoot] = qRoot
			self.wr[qRoot] += self.wr[pRoot]
		self.count -= 1
		

	def isConnect(self,p,q):
		if self.find(p) == self.find(q):
			return True
		return False

class Edge:
	def __init__(self,v,w,weight):
		self.__v = int(v)
		self.__w = int(w)
		self.__weight = float(weight)

	def weight(self):
		return self.__weight

	def other(self,vertex):
		if vertex == self.__v:
			return self.__w
		elif vertex == self.__w:
			return self.__v
		else:
			raise RuntimeError('unknown vertex')

	def either(self):
		return self.__v

	def vertexes(self):
		return self.__v,self.__w

	def __str__(self):
		return 'v:%s, w:%s, weight:%s'%(self.__v,self.__w,self.__weight)

	def __lt__(self,edge):
		return self.weight() < edge.weight()

	def __le__(self,edge):
		return self.weight() <= edge.weight()

	def __eq__(self,edge):
		return self.weight() == edge.weight()

	def __gt__(self,edge):
		return self.weight() > edge.weight()

	def __ge__(self,edge):
		return self.weight() >= edge.weight()

class Graph:
	def __init__(self,file):
		with open(file,'rt') as f:
			self.V = int(f.readline())
			self.E = int(f.readline())
			self.edges = []
			for e in xrange(self.E):
				line = f.readline()
				v,w,weight = line.split()
				self.edges.append(Edge(v,w,weight))

class Kruskal:
	def __init__(self,G):
		self.mst = []
		self.pq = PriorityQueue()
		self.uf = UnionFind(G.V)

		for edge in G.edges:
			self.pq.push(edge)
		while not self.pq.isEmpty() and len(self.mst) < G.V - 1:
			e = self.pq.popMin()
			v,w = e.vertexes()
			if self.uf.isConnect(v,w):
				continue
			self.uf.union(v,w)
			self.mst.append(e)

	def edges(self):
		return self.mst

######################################################################

