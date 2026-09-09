class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        boxDict = {
            (0,0) : {1,2,3,4,5,6,7,8,9},
            (0,1) : {1,2,3,4,5,6,7,8,9},
            (0,2) : {1,2,3,4,5,6,7,8,9},
            (1,0) : {1,2,3,4,5,6,7,8,9},
            (1,1) : {1,2,3,4,5,6,7,8,9},
            (1,2) : {1,2,3,4,5,6,7,8,9},
            (2,0) : {1,2,3,4,5,6,7,8,9},
            (2,1) : {1,2,3,4,5,6,7,8,9},
            (2,2) : {1,2,3,4,5,6,7,8,9}
        }

        columnList = [{1,2,3,4,5,6,7,8,9},
                      {1,2,3,4,5,6,7,8,9},
                      {1,2,3,4,5,6,7,8,9},
                      {1,2,3,4,5,6,7,8,9},
                      {1,2,3,4,5,6,7,8,9},
                      {1,2,3,4,5,6,7,8,9},
                      {1,2,3,4,5,6,7,8,9},
                      {1,2,3,4,5,6,7,8,9},
                      {1,2,3,4,5,6,7,8,9}]

        for rowIndex, row in enumerate(board):
            rowSet = {1,2,3,4,5,6,7,8,9}
            for columnIndex, cell in enumerate(row):
                if cell == ".":
                    continue
                

                rangeTuple = (rowIndex // 3, columnIndex // 3)

                if int(cell) not in columnList[columnIndex] or int(cell) not in rowSet or int(cell) not in boxDict[rangeTuple]:
                    return False

                rowSet.remove(int(cell))
                columnList[columnIndex].remove(int(cell))
                boxDict[rangeTuple].remove(int(cell))
        

        return True

        