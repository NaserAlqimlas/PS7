## I worked on this assignment with help from a friend who had previously taken this class,
## as well as a student in CSEL.

import random

class Matrix(object):
    def __init__(self, i, k):
        self.mtrx = []
        x = 0
        y = 0
        while (x < i):
            y = 0
            nRow = []
            while (y < k):
                nRow.append(0)
                y = y + 1
            self.mtrx.append(nRow)
            x = x + 1

    def __repr__(self):
        return str(self.mtrx)

    def printMtrx(self):
        rStr = ""
        for r in self.mtrx:
            rStr = ""
            for entry in r:
                rStr += '{:{align}{width}}'.format(str(entry), align='^', width='3')
            print rStr

    def lenCol(self):
        return len(self.mtrx)

    def lenRow(self):
        return len(self.mtrx[0])

    def getE(self, r, c):
        return self.mtrx[r][c]

    def editE(self, r, c, new):
        self.mtrx[r][c] = new




def detOptOperation(S, i, j, x, y):
    if ((S.getE(i,j) - S.getE(i-1, j-1)) < 10):
        cheapests = []
        if (S.getE(i,j) == S.getE(i-1, j-1)):
            cheapest = min(S.getE(i, j), \
                           S.getE(i-1, j), \
                           S.getE(i, j-1))
            if (S.getE(i-1, j) == cheapest):
                cheapests.append("Delete " + x[i-1] + " from x")
            if (S.getE(i, j-1) == cheapest):
                cheapests.append("Insert " + y[j-1] + " into x")
            if (S.getE(i-1, j-1) == cheapest):
                cheapests.append("no-op")

        else:
            cheapest = min(S.getE(i-1, j), S.getE(i, j-1))
            if (S.getE(i-1, j) == cheapest):
                cheapests.append("Delete " + x[i-1] + " from x")
            if (S.getE(i, j-1) == cheapest):
                cheapests.append("Insert " + y[j-1] + " into x")
        if (len(cheapests) == 3):
            return "no-op"
        else:
            rndm = random.randint(0, len(cheapests)-1)
            return cheapests[rndm]

    else:
        return "Sub " + x[i-1] + " with " + y[j-1]


def alignStrings(x, y):     #Worked on this function with a student in CSEL,
                            #One of them told me his name was daniel but I can't remember his last name.
    S = Matrix(len(x) + 1, len(y) + 1)
    i = 1
    while (i < S.lenRow()):
        S.editE(0, i, i)
        i = i + 1
    i = 1
    while (i < S.lenCol()):
        S.editE(i, 0, i)
        i = i + 1
    i = 1
    j = 1
    while (i < S.lenCol()):
        j = 1
        while (j < S.lenRow()):
            if (x[i-1] == y[j-1]):
                S.editE(i, j, min(S.getE(i-1, j), \
                                      S.getE(i, j-1), \
                                      S.getE(i-1, j-1)))
            else:
                if (i >= 2 and j >= 2):
                    S.editE(i, j, min(S.getE(i-2, j-2) + 30, \
                                          S.getE(i-1, j) + 1, \
                                          S.getE(i, j-1) + 1, \
                                          S.getE(i-1, j-1) + 10))
                else:
                    S.editE(i, j, min(S.getE(i-1, j) + 1, \
                                          S.getE(i, j-1) + 1, \
                                          S.getE(i-1, j-1) + 10))
            j = j + 1
        i = i + 1
    return S

def extractAlignment(S, x, y):
    arr = []
    xLen = len(x)
    yLen = len(y)
    while (xLen > 0 or yLen > 0):
        arr.insert(0, detOptOperation(S, xLen, yLen, x, y))
        if (arr[0][:6] == "Insert"):
            yLen = yLen - 1
        elif (arr[0][:6] == "Delete"):
            xLen = xLen - 1
        else:
            xLen = xLen - 1
            yLen = yLen - 1
    return arr

def commonSubstrings(x, L, a):
    subStrs = []
    subStr = ""
    i = 0
    for l in a:
        if (l[:6] != "Insert"):
            if (l == "no-op"):
                subStr = subStr + x[i]
                i = i + 1
            else:
                if (len(subStr) >= L):
                    subStrs.append(subStr)
                subStr = ""
                i = i + 1
        else:
            if (len(subStr) >= L):
                subStrs.append(subStr)
            subStr = ""
    if (subStr != ""):
        subStrs.append(subStr)
    return subStrs



file1 = open("csci3104_PS7_data_string_x.txt", "r")
file2 = open("csci3104_PS7_data_string_y.txt", "r")
file1lines = file1.readlines()
file2lines = file2.readlines()
x = "".join(file1lines)
y = "".join(file2lines)
S = alignStrings(x, y)
a = extractAlignment(S, x, y)
m = commonSubstrings(x, 10, a)
print m
