import random


def rand_graph(x,y):
	a = []
	b = []
	for i in range(x):
		a.append(i)	
		b.append([])
	graph = dict(zip(a,b))
	for i in range (x):
		j = i+1
		while j < x:
			if random.random() <= y:
				graph[i].append(j)
				graph[j].append(i)
			j += 1
	return graph


