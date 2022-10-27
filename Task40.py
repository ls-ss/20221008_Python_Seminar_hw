''' Task40. Создайте программу для игры в ""Крестики-нолики"". '''

from tkinter import *
import random
root = Tk()                     # Создаем окно
root.title('Крестики-нолики')   # Название окна
game_run = True                 # Переменная для завершения игры
pole = []                       # Сюда будут записываться координаты фигур
kolvo_figur = 0                 # Кол-во фигур

# Поле с игрой 3 х 3
def new_game():
    for row in range(3):
        for col in range(3):
            pole[row][col]['text'] = ' '    # Начальный текст на поле
            pole[row][col]['background'] = 'lavender'   # Цвет плитки
    global game_run
    game_run = True
    global kolvo_figur
    kolvo_figur = 0

# Ф-ция проверки клика
def click(row, col):
    if game_run and pole[row][col]['text'] == ' ': # При нажатии на плитку ставим Х
        pole[row][col]['text'] = 'X'
        global kolvo_figur
        kolvo_figur += 1 # Пополняем список фигур
        check_win('X')
        if game_run and kolvo_figur < 5: # После добавления фигуры передаем ход боту
            computer_move()
            check_win('O')

# Проверка выигрышных вариантов
def check_win(smb):
    for n in range(3):
        check_line(pole[n][0], pole[n][1], pole[n][2], smb)
        check_line(pole[0][n], pole[1][n], pole[2][n], smb)
    check_line(pole[0][0], pole[1][1], pole[2][2], smb)
    check_line(pole[2][0], pole[1][1], pole[0][2], smb)

# Если собрана линия фигур, меняем цвет на розовый
def check_line(a1,a2,a3,smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'pink'
        global game_run
        game_run = False # Конец игры

# Ход бота. Ищет выигрышные варианты
def can_win(a1,a2,a3,smb):
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res

# Проверка возможной победы противника за следующий ход.
# Если игрок выставил два крестика в ряд, бот пытается разрушить выигрыш.
def computer_move():
    for n in range(3):
        if can_win(pole[n][0], pole[n][1], pole[n][2], 'O'):
            return
        if can_win(pole[0][n], pole[1][n], pole[2][n], 'O'):
            return

    if can_win(pole[0][0], pole[1][1], pole[2][2], 'O'):
        return
    if can_win(pole[2][0], pole[1][1], pole[0][2], 'O'):
        return

    for n in range(3):
        if can_win(pole[n][0], pole[n][1], pole[n][2], 'X'):
            return

        if can_win(pole[0][n], pole[1][n], pole[2][n], 'X'):
            return

    if can_win(pole[0][0], pole[1][1], pole[2][2], 'X'):
        return
    if can_win(pole[2][0], pole[1][1], pole[0][2], 'X'):
        return

# Случайный ход. Т.к. нельзя победить и проиграть
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if pole[row][col]['text'] == ' ':
            pole[row][col]['text'] = 'O'
            break

# Графический интерфейс
for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text=' ', width=4, height=2,
            font=('Verdana', 20, 'bold'),
            background='lavender',
            command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    pole.append(line)

new_button = Button(root, text='Новая игра', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
root.mainloop()