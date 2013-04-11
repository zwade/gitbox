class cell(object):
	matrix = None

	def __init__(self, val, r, c,  matrix):
		self.value = val
		if val!=0:
			self.PossibleValues = [val,]
		else: self.PossibleValues = [1,2,3,4,5,6]
		self.row = r
		self.col = c
		self.block = self.blockNumber(r,c)
		cell.matrix = matrix
	def __repr__(self):
		line1 = "M{"+str(self.row)+", "+str(self.col)+"] = "
		line2 = str(self.value)+"; range = "+str(self.PossibleValues)
		return line1+line2
	def __eq__(self,other):
		return self.value==other.value
	def clone(self):
		return cell(self.value,self.row,self.col,cell.matrix)	
	def blockNumber(self,row,col):
		if self.row < 2 and self.col < 3:return 0
		if self.row < 2 and self.col > 2:return 1
		if (self.row > 1 and self.col < 4) and self.col < 3:return 2
		if (self.row > 1 and self.col < 4) and self.col > 2:return 3
		if self.row > 3 and self.col < 3:return 4
		if self.row > 3 and self.col > 2:return 5

def setUpCanvas(root):
	root.title("SUDOKU")
	canvas = Canvas(root, width = 1270, height = 780, bg = 'black')
	canvas.pack(expand = YES, fill = BOTH)
	return canvas

def compareSudokus(mat1,mat2):
	for i in range(len(mat1)):
		for a in range(len(mat1[i])):
			if not(mat1[i][a]==mat2[i][a]):
				return False
	return True
def solutionIsCorrect(matrix):
	errorFlag = True

	rows = [[],[],[],[],[],[]]
	cols = [[],[],[],[],[],[]]

	for r in range(MAX):
		for c in range(MAX):
			rows[r].append(matrix[r][c].value)
			cols[c].append(matrix[r][c].value)
	block = [0,0,0,0,0,0]

	block[0] = [matrix[0][0].value,matrix[0][1].value,matrix[0][2].value,
		    matrix[1][0].value,matrix[1][1].value,matrix[1][2].value]
	block[1] = [matrix[2][0].value,matrix[2][1].value,matrix[2][2].value,
		    matrix[3][0].value,matrix[3][1].value,matrix[3][2].value]
	block[2] = [matrix[4][0].value,matrix[4][1].value,matrix[4][2].value,
		    matrix[5][0].value,matrix[5][1].value,matrix[5][2].value]
	block[3] = [matrix[0][3].value,matrix[0][4].value,matrix[0][5].value,
		    matrix[1][3].value,matrix[1][4].value,matrix[1][5].value]
	block[4] = [matrix[2][3].value,matrix[2][4].value,matrix[2][5].value,
		    matrix[3][3].value,matrix[3][4].value,matrix[3][5].value]
	block[5] = [matrix[4][3].value,matrix[4][4].value,matrix[4][5].value,
		    matrix[5][3].value,matrix[5][4].value,matrix[5][5].value]

	for r in rows:
		for n in range(1, MAX+1):
			if n not in r:
				return False

	for c in cols:
		for n in range(1, MAX+1):
			if n not in c:
				return False
	
	for b in block:
		for n in range(1,MAX+1):
			if n not in b:
				return False

	return True

def printVerification(matrix):
	for r in range(MAX):
		for c in range(MAX):
			print(matrix[r][c].value, end='')
		print()
	print(solutionIsCorrect(matrix))
	if solutionIsCorrect(matrix):
		canvas.create_text(490,460,text = 'This solution is correct', fill = 'WHITE', font = ('Helvetica', 20, 'bold'))
	else:
		canvas.create_text(490,460,text = 'WRONG!', fill = 'WHITE', font = ('Helvetica', 20, 'bold'))
	
def createMatrix():
	#M = [[5,0,3,1,2,4],[0,0,1,0,3,0,],[0,0,6,5,0,2],[2,0,5,3,0,0],[0,1,0,2,0,0],[0,0,2,0,0,3],]
	M = [[5,0,0,1,0,0],[0,0,1,0,3,0,],[0,0,6,5,0,2],[2,0,5,3,0,0],[0,1,0,2,0,0],[0,0,2,0,0,3],]
	#M = [[0,0,0,0,0,0],[0,0,0,0,0,0,],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],]
	#M = [[2,0,1,6,0,0],[0,5,0,0,0,0,],[3,0,0,0,2,0],[0,1,0,0,0,4],[0,0,0,0,3,0],[0,0,0,0,0,1],]
	matrix = []
	for r in range(MAX):
		row = []
		for c in range(MAX):
			row.append(cell(M[r][c],r,c,matrix))
		matrix.append(row)
	return matrix

def printMatrixToScreen(matrix):
	canvas.update()
	canvas.delete('all')
	canvas.create_rectangle(375,170,595,440,width=4,outline = 'gold', fill = 'blue')

	canvas.create_line(375,262,595,262,width=5, fill='gold')
	canvas.create_line(375,347,595,347,width=5, fill='gold')
	canvas.create_line(485,170,485,440,width=5, fill='gold')
	canvas.create_line(375,220,595,220,width=5, fill='gold')
	canvas.create_line(375,306,595,306,width=5, fill='gold')
	canvas.create_line(375,390,595,390,width=5, fill='gold')
	canvas.create_line(418,170,418,440,width=5, fill='gold')
	canvas.create_line(453,170,453,440,width=5, fill='gold')
	canvas.create_line(520,170,520,440,width=5, fill='gold')
	canvas.create_line(555,170,555,440,width=5, fill='gold')

	for r in range(MAX):
		for c in range(MAX):
			ch = matrix[r][c].value
			if ch == 0: ch = ''
			canvas.create_text(c*34+400,r*42+200, text = ch, fill = 'YELLOW', font = ('Helvetica',20,'bold'))

def solveTheSudoku(matrix):
	cont = True
	while cont:
		matrix,cont = solveIterative(matrix)
	matrix,cont = solveRecurse(matrix)
	return matrix

def solveRecurse(matrix):
	print("Recursed")
	cont = True
	while cont:
		matrix,cont = solveIterative(matrix)
	if solutionIsCorrect(matrix):
		return (matrix,True)
	if isFull(matrix):
		return (matrix,False)
	for a in matrix:
		for i in a:
			if i.value!=0: continue
			for p in i.PossibleValues:
				i.value = p
				matrix,true = solveRecurse(matrix)
				if true:
					return (matrix,True)
	print('Fallback')
	return (matrix,False)

def solveIterative(matrix):
	omatrix = [[i.clone() for i in a] for a in matrix]
	unfin = 0
	cont = True
	for a in range(MAX):
		for i in range(MAX):
			if matrix[a][i].value==0:
				#poss.append((a,i,findAllPoss(matrix,a,i)))
				vals = findAllPoss(matrix,a,i)
				if len(vals)==1:
					matrix[a][i].value = vals[0]
				else:
					unfin+=1
				matrix[a][i].PossibleValues = vals
			else:
				pass

	for a in range(MAX):
		for i in range(MAX):
			if (matrix[a][i].value==0):
				matrix[a][i].PossibleValues = findAllPoss(matrix,a,i)
	for a in range(MAX):
		for i in range(MAX):
			if (matrix[a][i].value==0):
				tmp = elim(matrix,a,i)
				if (tmp):
					matrix[a][i].value = tmp
					matrix[a][i].PossibleValues = [tmp]
	
	if unfin==0 or compareSudokus(matrix,omatrix):
		cont = False

	return (matrix,cont)

def findAllPoss(matrix,r,c):
	ret = [i for i in range(MAX+1)]
	for i in matrix[r]:
		if i.value in ret:ret.remove(i.value)
	for i in matrix:
		if i[c].value in ret:ret.remove(i[c].value)
	for i in getCell2x3(matrix,r,c):
		i = i.value
		if i in ret: ret.remove(i)
	return ret

def elim(matrix,r,c):
	block = getCell2x3(matrix,r,c)
	nr = r%2
	nc = c%3
	poss = [i for i in range(1,MAX+1)]
	block = block[:nr*3+nc]+block[nr*3+nc+1:]
	for i in range(len(block)):
		for a in block[i].PossibleValues:
			if a in poss: poss.remove(a)

	if len(poss)==1:
		return poss[0]
	return False

def isFull(matrix):
	for i in matrix:
		for a in i:
			if a.value==0:
				return False

	return True

def getCell2x3(matrix,r,c):
	r = r//2*2
	c = c//3*3
	ret = []
	ret.append(matrix[r][c] )
	ret.append(matrix[r+0][c+1] )
	ret.append(matrix[r+0][c+2] )
	ret.append(matrix[r+1][c+0] )
	ret.append(matrix[r+1][c+1] )
	ret.append(matrix[r+1][c+2] )
	return ret

from tkinter import *
from sys import setrecursionlimit; setrecursionlimit(100)
from copy import deepcopy
root = Tk()
canvas = setUpCanvas(root)
MAX = 6

def main():
	matrix = createMatrix()
	matrix = solveTheSudoku(matrix)
	printMatrixToScreen(matrix)
	printVerification(matrix)
	root.mainloop()

if __name__ == '__main__' : main()
