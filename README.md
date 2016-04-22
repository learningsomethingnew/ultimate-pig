#Ultimate Pig
![ultimate spiderman pig ](http://i107.photobucket.com/albums/m294/Armitage72/Executioner.jpg)

##Goal
----------
Simulate multiple games of pig solitaire with different playing styles to identify winning strategies.

##Pig Solitaire
----------
###Goal of the game
Get the highest score in 7 turns and understand inheritance better.

###Rules
Each turn, you have two choices:
 - Roll a six-sided die
 - Hold

####Rolling
- Roll 1 
	- Turn is over 
	- Add nothing to player score. 
- Roll 2-6 
	 - Add that number to turn total
 - Choose
	 - Roll
	 - Hold

####Hold 
-  Add the turn total to your score.


##How to View Results
----------
Open the ["Ultimate-Pig"]() file and view results.



##Classes
----------
####Players

 - Base player
	 - rolls once per turn 
	 - Hold
		 - If able to hold, will hold
 - Random player
	 - based on random, determine
 - Rolls (6-2 times) and then holds


####Game
Manages the turns and who is currently rolling.

