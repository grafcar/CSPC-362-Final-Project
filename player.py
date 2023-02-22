import pieces

class Player(pieces):
    def __init__(self,turn=0, moves=0, piece="black"):
        self.turn = turn
        self.moves = moves
        super().__init__()

    