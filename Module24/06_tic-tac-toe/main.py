class Board:
    def __init__(self):
        self.board = {
            '1': "1", '2': "2", '3': "3",
            '4': "4", '5': "5", '6': "6",
            '7': "7", '8': "8", '9': "9"}

    def print_board(self):

        print(self.board['1'] + "|" + self.board['2'] \
            + "|" + self.board['3'] + "|")
        print("--" * 3)
        print(self.board['4'] + "|" + self.board['5'] \
            + "|" + self.board['6'] + "|")
        print("--" * 3)
        print(self.board['7'] + "|" + self.board['8'] \
            + "|" + self.board['9'] + "|")

    def _is_valid_move(self, position):
        if self.board[position] == " ":
            return True
        return False

    def change_board(self, position, type):
       if self._is_valid_move(position):
          self.board[position] = type
          return self.board
       return None

    def victory_comb(self, player):
        """Returns True if the player won and False otherwise."""
        if self.board['1'] == player.type and self.board['2'] == player.type and self.board['3'] == player.type or \
        self.board['4'] == player.type and self.board['5'] == player.type and self.board['6'] == player.type or \
        self.board['7'] == player.type and self.board['8'] == player.type and self.board['9'] == player.type or \
        self.board['1'] == player.type and self.board['4'] == player.type and self.board['7'] == player.type or \
        self.board['2'] == player.type and self.board['5'] == player.type and self.board['8'] == player.type or \
        self.board['3'] == player.type and self.board['6'] == player.type and self.board['9'] == player.type or \
        self.board['1'] == player.type and self.board['5'] == player.type and self.board['9'] == player.type or \
        self.board['7'] == player.type and self.board['5'] == player.type and self.board['3'] == player.type:
            return True
        return False


class Player:

    def __init__(self, type):
        self.type = type

    def __str__(self):
        return "Player {}".format(self.type)


class Game:
    def __init__(self):
        self.player1 = Player("X")
        self.player2 = Player("O")
        self.board = Board()


    def printing_board(self):
        self.board.print_board()

    def change_turn(self, player):
        if player is self.player1:
            return self.player2
        else:
            return self.player1

    def won_game(self, player):
        return self.board.victory_comb(player)

    def modify_board(self, position, type):
        if self.board.change_board(position, type) is not None:
            return self.board.change_board(position, type)
        else:
            position = input("Нет доступных ходов, попробуйте еще раз ")
            return self.board.change_board(position, type)


def play():
    game = Game()
    player = game.player1
    num = 9
    while num > 0:
        num -= 1
        game.printing_board()
        position = input("{} ходит, куда хотите сходить ".format(player))
        game.modify_board(position, player.type)
        if game.won_game(player):
            print("{} Победитель!".format(player))
            break
        else:
            player = game.change_turn(player)
    if num == 0:
        print("Игра окончена!")


if __name__ == "__main__":
    play()
