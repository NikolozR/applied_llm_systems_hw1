
class Solution:

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        self.rows = len(mat)
        self.cols = len(mat[0])
        self.diagonalRowsCrawler(mat)
        return mat

    def diagonalRowsCrawler(self, mat: List[List[int]]) -> None:
        col = self.cols
        for row in range(self.rows):
            # iterate through diagonals on first row
            while col:
                col -= 1
                self.diagonalValueSort(mat, row, col)
            # iterate through diagonals on other rows
            self.diagonalValueSort(mat, row, col)

    def diagonalValueSort(self, mat: List[List[int]], row: int, col: int) -> None:
        diagonal_values = []
        # gather values
        while row < self.rows and col < self.cols:
            diagonal_values.append(mat[row][col])
            row += 1
            col += 1
        # sort values
        diagonal_values.sort()
        # replace current values with sorted
        while row > 0 and col > 0:
            row -= 1
            col -= 1
            mat[row][col] = diagonal_values.pop()