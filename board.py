
class SnakeLadderBoard:
    def __init__(self):
        self.snakeLadderCells = [[None, None]]*101
        self.playersNumbers = 0
        self.playerNames = list()

    def insertSnake(self, head, tail):
        self.snakeLadderCells[head] = ['S', tail]

    def insertLadder(self, head, tail):
        self.snakeLadderCells[tail] = ['L', head]

    def displayBoard(self):
        # os.system("cls")
        arro = list()
        # print(self.snakeLadderCells)
        for j in range(90, -10, -10):
            k = j//10
            if k % 2 == 0:
                for i in range(1, 11):
                    if self.snakeLadderCells[i+j] == [None, None]:
                        arro.append(str(i+j)+"       ")
                    else:
                        arro.append(str(self.snakeLadderCells[i+j]) + " ")
            else:
                for i in range(10, 0, -1):
                    if self.snakeLadderCells[i+j] == [None, None]:
                        arro.append(str(i+j)+"       ")
                    else:
                        arro.append(str(self.snakeLadderCells[i+j]) + " ")
            arro.append("\n")
        string = "".join(arro)
        return string
