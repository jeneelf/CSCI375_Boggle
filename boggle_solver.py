"""
NAME: Jeneel Farrell
SID: @03023942
"""

class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.row = len(grid)
        self.col = len(grid[0])
        self.dictionary = set(word.upper() for word in dictionary)
        self.solutions = set()
        self.directions = [(1, -1), (-1, 0), (-1, -1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        self.visited = [[False for _ in range(self.col)] for _ in range(self.row)]

    def setGrid(self, grid):
        """Setting Grid"""
        self.grid = grid
        self.row = len(grid)
        self.col = len(grid[0])

    def setDictionary(self, dictionary):
        """Setting Dictionary"""
        self.dictionary = set(word.upper() for word in dictionary)

    def getSolution(self):
        """Finds all words in the grid that are in the dictionary"""
        self.solutions = set()
        self.visited = [[False for _ in range(self.col)] for _ in range(self.row)]

        for r in range(self.row):
            for c in range(self.col):
                self.dfs(r, c, "")

        return list(self.solutions)

    def dfs(self, row, col, currWord):
        if row < 0 or row >= self.row or col < 0 or col >= self.col:
            return
        
        if self.visited[row][col]:
            return

        # Handle special tiles
        tile = self.grid[row][col]
        if tile == "Qu":
            tile = "QU"
        elif tile == "St":
            tile = "ST"
        else:
            tile = tile.upper()

        currWord += tile

        if len(currWord) >= 3 and currWord in self.dictionary and currWord not in self.solutions:
            self.solutions.add(currWord)

        # Check if the current prefix can lead to any word in the dictionary
        if not any(word.startswith(currWord) for word in self.dictionary):
            return

        self.visited[row][col] = True

        for dr, dc in self.directions:
            new_row, new_col = row + dr, col + dc
            self.dfs(new_row, new_col, currWord)

        # Unmark the current cell (backtrack)
        self.visited[row][col] = False

def main():
    grid = [
        ["T", "W", "Y", "R"],
        ["E", "N", "P", "H"],
        ["G", "St", "Qu", "R"],
        ["O", "N", "T", "A"]
    ]
    dictionary = [
        "art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"
    ]
    
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

if __name__ == "__main__":
    main()
