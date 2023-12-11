class Tile:
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.s = symbol
        self.visited = False

    def is_connected(self, other):
        return True if (self.x, self.y) in other.connected_tiles else False
    
    def has_visited(self):
        self.visited = True

    def find_options(self, maze):
        options = []
        for tile in [(self.x, self.y - 1), (self.x - 1, self.y - 1), (self.x - 1, self.y), (self.x - 1, self.y + 1), (self.x, self.y + 1), (self.x + 1, self.y + 1), (self.x + 1, self.y), (self.x + 1, self.y - 1)]:
            if self.is_connected(maze[tile[0][1]]):
                options.append(maze[tile[0][1]])
        return options
                

class Ground(Tile):
    def __init__(self, x, y, symbol):
        super().__init__(x, y, symbol)
    
    @property
    def connected_tiles(self):
        return ()

class Vertical(Tile):
    def __init__(self, x, y, symbol):
        super().__init__(x, y, symbol)

    def __repr__(self):
        return f'{self.s} at {self.x}, {self.y}'
    
    @property
    def connected_tiles(self):
        return ((self.x + 1, self.y), (self.x - 1, self.y))

class Horizontal(Tile):
    def __init__(self, x, y, symbol):
        super().__init__(x, y, symbol)
    
    def __repr__(self):
        return f'{self.s} at {self.x}, {self.y}'

    @property
    def connected_tiles(self):
        return ((self.x, self.y + 1), (self.x, self.y - 1))
    
class North_East(Tile):
    def __init__(self, x, y, symbol):
        super().__init__(x, y, symbol)
    
    def __repr__(self):
        return f'{self.s} at {self.x}, {self.y}'

    @property
    def connected_tiles(self):
        return ((self.x - 1, self.y), (self.x, self.y + 1))

class North_West(Tile):
    def __init__(self, x, y, symbol):
        super().__init__(x, y, symbol)
    
    def __repr__(self):
        return f'{self.s} at {self.x}, {self.y}'

    @property
    def connected_tiles(self):
        return ((self.x - 1, self.y), (self.x, self.y - 1))
    
class South_West(Tile):
    def __init__(self, x, y, symbol):
        super().__init__(x, y, symbol)
    
    def __repr__(self):
        return f'{self.s} at {self.x}, {self.y}'

    @property
    def connected_tiles(self):
        return ((self.x + 1, self.y), (self.x, self.y - 1))

class South_East(Tile):
    def __init__(self, x, y, symbol):
        super().__init__(x, y, symbol)
    
    def __repr__(self):
        return f'{self.s} at {self.x}, {self.y}'

    @property
    def connected_tiles(self):
        return ((self.x + 1, self.y), (self.x, self.y + 1))
    
class Start(Tile):
    def __init__(self, x, y, symbol):
        super().__init__(x, y, symbol)
    
    def __repr__(self):
        return f'{self.s} at {self.x}, {self.y}'

    @property
    def connected_tiles(self):
        return ()