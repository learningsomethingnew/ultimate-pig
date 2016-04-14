from player import BasePlayer


#####################
# !Make game loop
####################

class Main():
    def __init__(self):
        self.number_of_turns = 7
        self.player1 = BasePlayer(a_name="Player_1")
        self.player2 = BasePlayer(a_name="Player_2")

    """Manages the 7 turns"""

    def main_game_loop(self):
        game_turns = 0
        while game_turns < self.number_of_turns:
            self.player1.decisions_for_each_turn()
            self.player2.decisions_for_each_turn()
            game_turns += 1
        self.win_loose()

    def win_loose(self):
        # Player 1 Wins
        if self.player1.get_total_points() > self.player2.get_total_points():
            print("Player 1 Wins")
            self.print_player_points()
        # Player 2 Wins
        elif self.player1.get_total_points() < self.player2.get_total_points():
            print("Player 2 Wins")
            self.print_player_points()
        else:
            print("It's a tie")

    def print_player_points(self):
        print("Player 1 points = {}".format(self.player1.get_total_points()))
        print("Player 2 points = {}".format(self.player2.get_total_points()))


if __name__ == "__main__":
    f = Main()
    f.main_game_loop()
