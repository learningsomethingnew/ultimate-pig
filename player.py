from random import randint


class Player():
    def __init__(self, a_name=""):
        self.player_total_score = 0
        self.player_name = a_name
        self.player_bank_score = 0
        # tracks how many times a player rolls
        self.player_dice_rolls = 0
        # tracking stats
        self.wins = 0
        self.game_count = 0
        self.dice_value_per_roll = []
        self.bank_score_list = []
        self.total_score_list = []

    """Returns player name"""

    def get_name(self):
        return self.player_name

    """Decides if to roll or hold"""

    def choose_roll_hold(self):
        pass

    """Set total points from bucket turn"""

    def set_total_score(self, a_value):
        self.player_total_score += a_value

    """Gets total points from player"""

    def get_total_score(self):
        return self.player_total_score

    """Resets player score"""

    def reset_total_score(self):
        self.player_total_score = 0

    """During a turn, set the bank score"""

    def set_bank_score(self, value):
        self.player_bank_score = value

    """Returns the int of the player's in turn score"""

    def get_bank_score(self):
        return self.player_bank_score

    """Returns int for dice"""

    def get_dice_roll(self):
        self.player_dice_rolls += 1
        temp_dice = randint(1, 6)
        # STATS: tracks the dice roll
        self.dice_value_per_roll.append(temp_dice)
        return temp_dice

    """Prints generic object information"""

    def __str__(self):
        return "I'm {}".format(self.player_name)

    """Manages players action for turn"""

    def decisions_for_each_turn(self):
        player_turn = True
        self.set_bank_score(0)
        self.player_dice_rolls = 0

        while player_turn:
            temp_dice = 0
            temp_choice = self.choose_roll_hold()
            # player chooses to roll
            if temp_choice == 'roll':
                # tracking stats
                # getting the roll information
                temp_dice = self.get_dice_roll()
                # testing if it ends turn
                if temp_dice == 1:
                    self.set_bank_score(0)
                    # break the loop
                    player_turn = False
                # if not, it adds the score to the bank
                else:
                    self.set_bank_score(temp_dice)
            # player chooses hold
            elif temp_choice == 'hold':
                # adds bank to the total
                self.set_total_score(self.get_bank_score())
                # break loop
                player_turn = False

    """takes in the win state and tracks the data"""

    def track_game_stats(self, a_win=0):
        self.game_count += 1
        self.wins += a_win
        # STATS: passes the number of dice rolls
        self.set_total_score_list(self.get_total_score())

    """Returns game count and wins"""

    def get_game_stats(self):
        return (self.game_count, self.wins)

    """Returns list of dice values per role"""

    def get_dice_values_per_role(self):
        return self.dice_value_per_roll

    """Appends an int to the bank score list"""

    def set_bank_score_list(self, a_value):
        self.bank_score_list.append(a_value)

    """Returns list of bank score per turn"""

    def get_bank_score_list(self):
        return self.bank_score_list

    """Appends an int to the total points"""

    def set_total_score_list(self, a_value):
        self.total_score_list.append(a_value)

    """Returns list of the total points list"""

    def get_total_score_list(self):
        return self.total_score_list


class BasePlayer(Player):
    """Ensures Baseplayer rolls only once"""

    def choose_roll_hold(self):
        if self.player_bank_score == 0:
            return "roll"
        else:
            return "hold"

class RandomThrow(Player):
    def choose_roll_hold(self):
        if randint(1,6) < 5:
            return 'roll'
        else:
            return 'hold'

class RollSixThenHold(Player):
    def choose_roll_hold(self):
        if self.player_dice_rolls < 7:
            return 'roll'
        else:
            return 'hold'

class RollFiveThenHold(Player):
    def choose_roll_hold(self):
        if self.player_dice_rolls < 6:
            return 'roll'
        else:
            return 'hold'

class RollFourThenHold(Player):
    def choose_roll_hold(self):
        if self.player_dice_rolls < 5:
            return 'roll'
        else:
            return 'hold'

class RollThreeThenHold(Player):
    def choose_roll_hold(self):
        if self.player_dice_rolls < 4:
            return 'roll'
        else:
            return 'hold'

class RollTwoThenHold(Player):
    def choose_roll_hold(self):
        if self.player_dice_rolls < 3:
            return 'roll'
        else:
            return 'hold'