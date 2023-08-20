class Grid:
    def __init__(self, fname):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        self.candidates = [[[i for i in range(9)] for _ in range(9)] for _ in range(9)]
        with open(fname, "r") as f:
            content = [r.strip() for r in f.readlines()]
            for i in range(9):
                for j in range(9):
                    item = content[i][j]
                    self.grid[i][j] = " " if item == '-' else int(item)

    def __str__(self):
        def str_builder(boundary_str, content_fn):
            bboundary_str = f"\033[1m{boundary_str}\033[0m"
            ret = ""
            for i in range(9):
                ret += bboundary_str if i % 3 == 0 else boundary_str
                ret += content_fn(i)
            ret += bboundary_str
            return ret

        bound = "+---+---+---+---+---+---+---+---+---+"
        bbound = f"\033[1m{bound}\033[0m"
        bound = str_builder("+", lambda _: "---")

        grid_str = ""
        for i in range(9):
            grid_str += bbound if i % 3 == 0 else bound
            grid_str += "\n"
            row = self.grid[i]
            grid_str += str_builder("|", lambda j: f" {row[j]} ")
            grid_str += "\n"
        grid_str += bbound
        return grid_str

    def _symbols_in_box(self, i, j):
        box_i = i // 3
        box_j = j // 3
        symbols = []
        for i in range(box_i * 3, box_i * 4):
            for j in range(box_j * 3, box_j * 4):
                if self.grid[i][j]:
                    symbols.append(self.grid[i][j])
        return symbols
    
    def _symbols_in_col(self, j):
        return self.grid(col)

    def get_next_brute_force(self):
        # When I am ruling out numbers in the grid, my brain chunks things
        # as much as possible. The correct representation might therefore not
        # be individual items in a grid laid out completely linearly, but instead
        # views must be provided that simplify how much brainpower a human must
        # use to track candidates and exclude candidates.
        for i in range(9):
            for j in range(9):
                cs = self.candidates[i][j]
        for symbol in range(1, 10):
            pass

    def ideas(self):
        # 1. Brute force. Each item in the grid has a candidate list of symbols.
        #    See how far one can get with "rol,col" saturation rule applied at a single
        #    depth level, then similar for exclusion techniques.
        # 2. Introduce another level of reasoning. See how far a solve can get.
        # 3. Additionally introduce more and more levels of reasoning.
        # 4. Do machines exhibit different strategies from humans? Can they arise independently?
        #    What insights can we gain?
        pass


g = Grid("00.grid")
print(g)
