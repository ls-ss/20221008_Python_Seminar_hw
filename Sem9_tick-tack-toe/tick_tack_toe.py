from os import system

cls = lambda: system('cls||clear')

class TicTacToeBoard():
    mark = ["X", "O"]
    n = 0
    def __init__(self):
        self.field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.active = TicTacToeBoard.mark[0]
        self.in_progress = True


    def new_game():
        cls()
        return TicTacToeBoard()

    def get_field(self):
        return self.field

    def check_field(self):
            TicTacToeBoard.n += 1

            if self.field[0][0] == self.field[0][1] == self.field[0][2] and self.field[0][0] != ' ': # Проверка по горизонтали
                return self.field[0][0]
            elif self.field[1][0] == self.field[1][1] == self.field[1][2] and self.field[1][0] != ' ':
                return self.field[1][0]
            elif self.field[2][0] == self.field[2][1] == self.field[2][2] and self.field[2][0] != ' ':
                return self.field[2][0]
            elif self.field[0][0] == self.field[1][0] == self.field[2][0] and self.field[0][0] != ' ': # Проверка по вертикали
                return self.field[0][0]
            elif self.field[0][1] == self.field[1][1] == self.field[2][1] and self.field[0][1] != ' ':
                return self.field[0][1]
            elif self.field[0][2] == self.field[1][2] == self.field[2][2] and self.field[0][2] != ' ':
                return self.field[0][2]
            elif self.field[0][0] == self.field[1][1] == self.field[2][2] and self.field[0][0] != ' ': # Проверка по Диагонали
                return self.field[0][0]
            elif self.field[0][2] == self.field[1][1] == self.field[2][0] and self.field[0][2] != ' ': # Проверка по Диагонали
                return self.field[0][2]
            elif TicTacToeBoard.n == 9 : # Если ничья
                return "D"


    def make_move(self, row, col):
        if self.in_progress == True:
            if 0 <= row < 3 and 0 <= col < 3:
                if self.field[row][col] != ' ':
                    cls()
                    print(f"Клетка {row + 1}:{col + 1} уже занята")
                    return 1
                else:
                    self.field[row][col] = self.active
                    self.active = TicTacToeBoard.mark[0] if self.active == TicTacToeBoard.mark[1] else \
                    TicTacToeBoard.mark[1]
                    result = self.check_field()
                    if result == None:
                        cls()
                        print("Продолжаем играть")
                        return 1
                    elif (result in 'XO'):
                        cls()
                        print(f"Победил игрок {result}")
                        print("Игра уже завершена")
                        self.in_progress = False
                        return 0
                    elif result == "D":
                        cls()
                        print("Ничья")
                        self.in_progress = False
                        return 0
                    return 1
            else:
                cls()
                print('Повторите ход')
                return 1
