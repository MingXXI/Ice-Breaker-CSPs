from a2_q1 import *


def check_teams(graph, csp_sol):
	for i in range (len(graph)):
		for j in range (len(graph[i])):
			cur_member = graph[i][j]
			if (csp_sol[i] == csp_sol[cur_member] ):
				print('yo')
				return False
	return True