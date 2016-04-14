from random import randint

class Player():
    def __init__(self, a_name = ""):
        self.player_total_score = 0
        self.player_name = a_name
        self.player_bank_score = 0

    """Decides if to roll or hold"""
    def choose_roll_hold(self):
        pass

    """Set total points for player"""
    def set_total_points(self, value):
        self.player_total_score += value

    """Gets total points from player"""
    def get_total_points(self):
        return self.player_total_score

    """During a turn, set the bank score"""
    def set_bank_score(self, value):
        self.player_bank_score = value

    """Returns the int of the player's in turn score"""
    def get_bank_score(self):
        return self.player_bank_score

    """Returns int for dice"""
    def get_dice_roll(self):
        temp_dice =  randint(1,6)
        print("{} rolled a {}.".format(self.player_name,    temp_dice))
        return temp_dice

    """Prints generic object information"""
    def __str__(self):
        return("I'm {}".format(self.player_name))

    """Manages players action for turn"""
    def decisions_for_each_turn(self):
        player_turn = True
        self.set_bank_score(0)

        while player_turn == True:
            temp_dice = 0
            temp_choice = self.choose_roll_hold()

            if temp_choice == 'roll':
                temp_dice = self.get_dice_roll()
                if temp_dice == 1:
                    self.set_bank_score(0)
                    player_turn = False
                else:
                    self.set_bank_score(temp_dice)
            elif temp_choice == 'hold':
                self.set_total_points(self.get_bank_score())
                player_turn = False




class BasePlayer(Player):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    "Ensures Baseplayer rolls only once"
    def choose_roll_hold(self):
        if self.player_bank_score == 0:
            return "roll"

        else:
            return "hold"



class CautiousPlayer(Player):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def choose_roll_hold(self):
        if self.player_bank_score == 0:
            return "roll"

        else:
            return "hold"
