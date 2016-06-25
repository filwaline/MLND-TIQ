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
class indexedMinHeap:
	def __init__(self):
		self.hq = []
		self.k2v = {}
		self.v2k = {}

	def push(self,key,value):
		heapq.heappush(self.hq,value)
		self.k2v[key] = value
		self.v2k[value] = key

	def popMin(self):
		value = heapq.heappop(self.hq)
		key = self.v2k.pop(value)
		del self.k2v[key]
		return key

	def change(self,key,value):
		lastvalue = self.k2v[key]
		del self.v2k[lastvalue]
		self.hq[self.hq.index(lastvalue)] = value
		self.v2k[value] = key
		self.k2v[key] = value

	def exist(self,key):
		try:
			self.k2v[key]
			return True
		except KeyError:
			return False

	def isEmpty(self):
		if len(self.hq) > 0:
			return False
		return True

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


class Graph:
	def __init__(self,file):
		with open(file,'rt') as f:
			self.V = int(f.readline())
			self.E = int(f.readline())
			self.adj = {v:[] for v in xrange(self.V)}
			for e in xrange(self.E):
				line = f.readline()
				v,w,weight = line.split()
				self.adj[int(v)].append(Edge(v,w,weight))
				self.adj[int(w)].append(Edge(w,v,weight))

	def degree(self,vertex):
		return len(self.adj[vertex])

class PrimMST:
	def __init__(self,G):
		self.edgeTo = [None for v in xrange(G.V)]
		self.distTo = [float('inf') for v in xrange(G.V)]
		self.marked = [False for v in xrange(G.V)]

		self.pq = indexedMinHeap()
		self.pq.push(0,0.0)

		while not self.pq.isEmpty():
			self.visit(G,self.pq.popMin())

	def visit(self,G,v):
		self.marked[v] = True

		for edge in G.adj[v]:
			w = edge.other(v)
			if self.marked[w]:
				continue
			if edge.weight() < self.distTo[w]:
				self.edgeTo[w] = edge
				self.distTo[w] = edge.weight()
				if self.pq.exist(w):
					self.pq.change(w,edge.weight())
				else:
					self.pq.push(w,edge.weight())

	def edges(self):
		return self.edgeTo

######################################################################

