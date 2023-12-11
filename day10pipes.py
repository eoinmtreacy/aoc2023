class Tile:
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.s = symbol
        self.visited = False

    def is_connected(self, other):
        return True if (self.x, self.y) in other.connected_tiles else False
    
    def __repr__(self):
        return f'{self.s} at {self.x}, {self.y}'
    
    def has_visited(self):
        self.visited = True

    def find_options(self, maze):
        options = []
        for tile in [(self.x - 1, self.y - 1), (self.x, self.y - 1), (self.x + 1, self.y - 1), (self.x + 1, self.y), (self.x + 1, self.y + 1), (self.x , self.y + 1), (self.x -1, self.y + 1), (self.x - 1, self.y)]:
            check = maze[tile[1]][tile[0]]
            if self.is_connected(check):
                options.append(check)
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

    @property
    def connected_tiles(self):
        return ((self.x, self.y + 1), (self.x, self.y - 1))

class Horizontal(Tile):
    def __init__(self, x, y, symbol):
        super().__init__(x, y, symbol)
    
    @property
    def connected_tiles(self):
        return ((self.x + 1, self.y), (self.x - 1, self.y))
    
class North_East(Tile):
    def __init__(self, x, y, symbol):
        super().__init__(x, y, symbol)

    @property
    def connected_tiles(self):
        return ((self.x - 1, self.y), (self.x, self.y + 1))

class North_West(Tile):
    def __init__(self, x, y, symbol):
        super().__init__(x, y, symbol)

    @property
    def connected_tiles(self):
        return ((self.x - 1, self.y), (self.x, self.y - 1))
    
class South_West(Tile):
    def __init__(self, x, y, symbol):
        super().__init__(x, y, symbol)
    
    @property
    def connected_tiles(self):
        return ((self.x + 1, self.y), (self.x, self.y - 1))

class South_East(Tile):
    def __init__(self, x, y, symbol):
        super().__init__(x, y, symbol)

    @property
    def connected_tiles(self):
        return ((self.x + 1, self.y), (self.x, self.y + 1))
    
class Start(Tile):
    def __init__(self, x, y, symbol):
        super().__init__(x, y, symbol)

    @property
    def connected_tiles(self):
        return ()