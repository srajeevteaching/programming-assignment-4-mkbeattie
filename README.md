Programming Assignment 4
Due: Wed Nov 10, 11:59 pm

Note: For this assignment you must work in a group of two or three members.

Problem
Create a program that lets the user play a simplified game of Blackjack, which is played between the user and an automated dealer as follows.

The dealer shuffles a standard deck of 52 cards, draws two cards, and gives them to the user. The user can then choose to request another card from the dealer, adding it to their hand. The user can continue to request cards or choose to stop at any time. After each time the user requests a card, the program should output the cards in the player's updated hand and their total point value (see the function decomposition section below for how to calculate points). If, when receiving a new card, the total number of points in the hand goes over 21, the user loses. In this case, the dealer does not play.

Once the user chooses to not draw any more cards, it is the dealer's turn to play, which is automated as follows. The dealer begins by drawing two cards. As long as the point value of the dealer's hand is less than 17, the dealer draws another card. When the point value of the hand is between 17 and 21 (inclusive), the dealer stops and the two hands (user's and dealer's) are compared. The player with the highest point value wins. If the point value of the dealer's hand goes over 21, the dealer has lost.

When the game ends, the program should output the outcome along with both player's hands.

Instructions
Create a new Python file and place intro comments using the template below.
Use comments to write the algorithm your program will follow, including functions. Use the function decomposition described in the section below.
Write the Python code corresponding to each of your algorithm's steps.
Note: This assignment does not require a flowchart or test cases in a spreadsheet. Test your program by playing through a game several times, ensuring that you try all possible scenarios.

Commit and push changes and check your repository on github.com to confirm your updates before the deadline.

Intro comments template
    # Programmers: [your name]
    # Course: CS151, Dr. Rajeev  
    # Programming Assignment: 4
    # Program Inputs: [What information do you request from the user?]
    # Program Outputs: [What information do you display for the user?]
Function decomposition
Your program should have a function for at least each of the following tasks. You may have additional helper functions.

A function that generates a shuffled deck of cards represented as a list. There are 52 cards in a deck: 13 clubs, 13 diamonds, 13 hearts, and 13 spades. A card is represented as a string made up of a number between 1 and 13 and one character identifying the suit. For example, the string '8c' represents the 8 of clubs and '12d' represents the queen of diamonds. Use loops to generate the deck list in order and then use the random.shuffle function to randomly shuffle it. No user input or output should occur inside this function.

A function which, given a string parameter representing a card (as described above), generates and returns a string with the card's name. For example, if the function receives '13h', the function should return 'King of Hearts'; if it receives '1s', the function should return 'Ace of Spades'; if it receives '3d' it should return '3 of Diamonds'. Use string indexing/slicing as needed to extract the number and suit. No user input or output should occur inside this function.

A function which, given a list parameter representing a hand of cards, outputs the hand to the console, printing each card's name (as described above).

A function which, given a list parameter representing a hand of cards, returns its total point value. A hand's point value is computed as the sum of point values of its cards. Each card's value is independent of its suit. An ace is worth 11 points. A face card (jack, queen, or king) is worth 10 points. All other cards are worth their value (for example, the 8 of clubs is worth 8 points). Use string indexing/slicing as needed to extract the number and suit. No user input or output should occur inside this function.

A main function to drive the program and enable play.

Submission
GitHub: Completed .py file (including comments).
