from player import BasePlayer, RollFiveThenHold


#####################
# Main class. Manages the number of turns and
# the number of sims of the app.
####################

class Main():
    def __init__(self, num_of_sims, a_player1, a_player2):
        self.number_of_turns = 7
        self.player1 = a_player1
        self.player2 = a_player2

        self.num_of_sims = num_of_sims

    """Runs the game for the # of sims needed"""

    def main(self):
        for _ in range(self.num_of_sims):
            self.game_loop()

    """Manages the 7 turns"""

    def game_loop(self):
        self.player1.reset_total_score()
        self.player2.reset_total_score()
        game_turns = 0
        while game_turns < self.number_of_turns:
            self.player1.decisions_for_each_turn()
            self.player2.decisions_for_each_turn()
            game_turns += 1
        self.win_lose()

    def win_lose(self):
        # Player 1 Wins
        if self.player1.get_total_score() > \
                self.player2.get_total_score():
            #print("Player 1 Wins")
            #self.game_results()
            # track stats of player 1
            self.player1.track_game_stats(1)
            self.player2.track_game_stats()
        # Player 2 Wins
        elif self.player1.get_total_score() < \
                self.player2.get_total_score():
            #print("Player 2 Wins")
            #self.game_results()
            # track stats of player 2
            self.player1.track_game_stats()
            self.player2.track_game_stats(1)
        else:
            # print("It's a tie")
            pass

    def game_results(self):
        print("Player 1 points = {}".format(self.player1.get_total_score()))
        print("Player 2 points = {}".format(self.player2.get_total_score()))
        self.player2.track_game_stats()


if __name__ == "__main__":

    # Base vs Base
    b_player1 = BasePlayer("Player1")
    b_player2 = BasePlayer("Player2")
    f = Main(1000, b_player1, b_player2)
    f.main()


    # Roll 5 Player vs Roll 5
    r5_player1 = BasePlayer("Player1")
    r5_player2 = BasePlayer("Player2")
    g = Main(1000, r5_player1, r5_player2)

    print(b_player1.get_total_score_list())
