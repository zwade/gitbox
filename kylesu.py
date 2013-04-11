class cell(object):
    matrix = None
    
    def __init__(self, val, r, c, matrix):
        self. value = val
        if val != 0:
            self.PossibleValues = [val,]
        else: self.PossibleValues = [1,2,3,4,5,6]
        self.row = r
        self.col = c
        self.block = self.blockNumber(r,c)
        cell.matrix = matrix
        
    def __repr__(self):
        line1 = "M[" + str(self.row) + ", " + str(self.col) + "] = "
        line2 = str(self.value) + "; range = " + str(self.PossibleValues)
        return line1 + line2
    
    def blockNumber(self,row,col):
        if self.row < 2 and self.col < 3: return 0
        if self.row < 2 and self.col > 2: return 1
        if (self.row > 1 and self.row < 4) and self.col < 3: return 2
        if (self.row > 1 and self.row < 4) and self.col > 2: return 3
        if self.row > 3 and self.col < 3: return 4
        if self.row > 3 and self.col > 2: return 5

def setUpCanvas(root):
    root.title("SUDOKU: A Tk/Python Graphics Program")
    canvas = Canvas(root, width = 1270, height = 780, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    return canvas

def solutionIsCorrect(matrix):
    errorFlag = True
    
    rows = [[],[],[],[],[],[]]
    cols = [[],[],[],[],[],[]]
    for r in range(MAX):
        for c in range(MAX):
            rows[r].append(matrix[r][c].value)
            cols[c].append(matrix[r][c].value)
            
    block = [0,0,0,0,0,0]
    block[0] = [matrix[0][0].value,matrix[0][1].value,matrix[0][2].value,matrix[1][0].value,matrix[1][1].value,matrix[1][2].value]
    block[2] = [matrix[2][0].value,matrix[2][1].value,matrix[2][2].value,matrix[3][0].value,matrix[3][1].value,matrix[3][2].value]
    block[4] = [matrix[4][0].value,matrix[4][1].value,matrix[4][2].value,matrix[5][0].value,matrix[5][1].value,matrix[5][2].value]
    block[1] = [matrix[0][3].value,matrix[0][4].value,matrix[0][5].value,matrix[1][3].value,matrix[1][4].value,matrix[1][5].value]
    block[3] = [matrix[2][3].value,matrix[2][4].value,matrix[2][5].value,matrix[3][3].value,matrix[3][4].value,matrix[3][5].value]
    block[5] = [matrix[4][3].value,matrix[4][4].value,matrix[4][5].value,matrix[5][3].value,matrix[5][4].value,matrix[5][5].value]
    
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
            print(matrix[r][c].value, end ='')
        print()
    print(solutionIsCorrect(matrix))
    if solutionIsCorrect(matrix):
        canvas.create_text(490, 460, text = "This sudoku is corrent.", fill = 'WHITE', font = ('Helevetica', 20, 'bold'))
    else:
        canvas.create_text(490, 500, text = "WRONG!", fill = 'RED', font = ('Helevetica', 80, 'bold'))
        
def createMatrix():
    M = [[5,0,0,1,0,0],[0,0,1,0,3,0],[0,0,6,5,0,2],[2,0,5,3,0,0],[0,1,0,2,0,0],[0,0,2,0,0,3]]
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
    canvas.create_rectangle(375, 170, 595, 440, width = 4, outline = 'red', fill = 'blue')
    canvas.create_line(375,262, 595, 262, width = 5, fill = 'red')
    canvas.create_line(375,347, 595, 347, width = 5, fill = 'red')
    canvas.create_line(485,170, 485, 440, width = 5, fill = 'red')
    canvas.create_line(375,220, 595, 220, width = 2, fill = 'red')
    canvas.create_line(375,306, 595, 306, width = 2, fill = 'red')
    canvas.create_line(375,390, 595, 390, width = 2, fill = 'red')
    canvas.create_line(418,170, 418, 440, width = 2, fill = 'red')
    canvas.create_line(453,170, 453, 440, width = 2, fill = 'red')
    canvas.create_line(520,170, 520, 440, width = 2, fill = 'red')
    canvas.create_line(555,170, 555, 440, width = 2, fill = 'red')
    
    for r in range(MAX):
        for c in range(MAX):
            ch = matrix[r][c].value
            if ch == 0: ch = ' '
            canvas.create_text(c*34 + 400, r*42+200, text = ch, fill = 'YElLOW', font = ('Helvetica', 20, 'bold'))
            
def updatePossibleValues(matrix):
    matrix = matrix[:]
    for x in range(MAX):
        for y in range(MAX):
            cell = matrix[x][y]
            for val in returnBlockValues(matrix,cell.block):
                if val in cell.PossibleValues:
                    cell.PossibleValues.remove(val)
            for val in returnRowValues(matrix,cell.row):
                if x == 2 and y==0:
                    print(val)
                if val in cell.PossibleValues:
                    cell.PossibleValues.remove(val)
            for val in returnColumnValues(matrix,cell.col):
                if val in cell.PossibleValues:
                    cell.PossibleValues.remove(val)
            matrix[x][y] = cell
    return matrix

def solveTheSudoku(matrix):
    while not solutionIsCorrect(matrix):
        printMatrixToScreen(matrix)
        print(matrix)
        matrix = updatePossibleValues(matrix)
        matrix = inference(matrix)
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if len(matrix[x][y].PossibleValues) == 1:
                    matrix[x][y].value = matrix[x][y].PossibleValues[0]
    return matrix

def inference(matrix):
    matrix = matrix[:]
 #   for r in range(6):
 #       a = rowInference(matrix,r)
 #       for val in a:
 #           for cell in getRow(matrix,r):
 #               print(val,"###",cell.PossibleValues)
 #               if val in cell.PossibleValues:
 #                   print(cell.row,',',cell.col)
 #                   cell.Value = val

 #   for c in range(6):
 #       a = colInference(matrix,c)
 #       for val in a:
 #           for cell in getCol(matrix,c):
 #               if val in cell.PossibleValues:
 #                   cell.Value = val
                    
 #   for b in range(6):
 #       a = blockInference(matrix,b)
 #       for val in a:
 #           for cell in getBlock(matrix,b):
 #               if val in cell.PossibleValues:
 #                   cell.Value = val

    return matrix
    
def rowInference(matrix,r):
    there = []
    conflict = []
    for i in getRow(matrix,r):
        for val in i.PossibleValues:
            if val in there:
                conflict+=[val]
            if val not in there:
                there += [val]
    for val in conflict:
        if val in there:
            there.remove(val)
    return there

def colInference(matrix,c):
    there = []
    conflict = []
    for i in getCol(matrix,c):
        for val in i.PossibleValues:
            if val in there:
                conflict+=[val]
            if val not in there:
                there += [val]
    for val in conflict:
        if val in there:
            there.remove(val)
    return there

def blockInference(matrix,b):
    there = []
    conflict = []
    for i in getBlock(matrix,b):
        for val in i.PossibleValues:
            if val in there:
                conflict+=[val]
            if val not in there:
                there += [val]
    for val in conflict:
        if val in there:
            there.remove(val)
    return there

def solvetheSudoku2(matrix):
    oldMatrix = deepcopy(matrix)
    for r in range(MAX):
        for c in range(MAX):
            #...
            for number in candidates:
                #...
                matrix = solveTheSudoku2(matrix)
                if solutionIsCorrect(matrix):
                    return matrix
                matrix = restoreValues(matrix, oldMatrix)
            matrix = restoreValues(matrix, oldMatrix)
            return matrix

def returnRowValues(matrix,r):
    for i in getRow(matrix,r):
        yield i.value

def getRow(matrix,r):
    a = []
    for x in range(6):
        a+=[matrix[r][x]]
    return a

def returnColumnValues(matrix,c):
    for i in getCol(matrix,c):
        yield i.value
    
def getCol(matrix, c):    
    a = []
    for x in range(6):
        a+=[matrix[x][c]]
    return a

def returnBlockValues(matrix,b):
    for i in getBlock(matrix,b):
        yield i.value
        
def getBlock(matrix, b):
    block = [0,0,0,0,0,0]
    block[0] = [matrix[0][0],matrix[0][1],matrix[0][2],matrix[1][0],matrix[1][1],matrix[1][2]]
    block[2] = [matrix[2][0],matrix[2][1],matrix[2][2],matrix[3][0],matrix[3][1],matrix[3][2]]
    block[4] = [matrix[4][0],matrix[4][1],matrix[4][2],matrix[5][0],matrix[5][1],matrix[5][2]]
    block[1] = [matrix[0][3],matrix[0][4],matrix[0][5],matrix[1][3],matrix[1][4],matrix[1][5]]
    block[3] = [matrix[2][3],matrix[2][4],matrix[2][5],matrix[3][3],matrix[3][4],matrix[3][5]]
    block[5] = [matrix[4][3],matrix[4][4],matrix[4][5],matrix[5][3],matrix[5][4],matrix[5][5]]
    return block[b]

from tkinter import *
from sys import setrecursionlimit; setrecursionlimit(100)
from copy import deepcopy
root = Tk()
canvas = setUpCanvas(root)
MAX = 6

def main():
    matrix = createMatrix()
    printMatrixToScreen(matrix)
    matrix = solveTheSudoku(matrix)
    printVerification(matrix)
    root.mainloop()
    
if __name__ == '__main__':main()




