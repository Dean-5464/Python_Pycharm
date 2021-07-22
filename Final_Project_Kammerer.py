class Question:

    # Init Method for the Question Class
    def __init__(self, question, correct_answer, hint, player_score):
        self.__question = question
        self.__correct_answer = correct_answer
        self.__hint = hint
        self.__player_score = player_score

    # Prints the current question and displays it for the player
    def print_question(self):
        print('\n' + self.__question)

    # Update scoring variable to correctly display the current score
    def update_player_score(self, player_score):
        self.__player_score = player_score

    # Player input method that retrieves the player input and then decides if the answer is either correct or incorrect
    def get_player_input(self):
        player_input = input("Please enter your answer to the question >>> ")

        # Correct answer
        if player_input.lower() == self.__correct_answer:
            self.__player_score = self.__player_score + 1
            print("Your answer of", player_input, "is correct!", '\n')
            print('\n' + "Your Current Score is", self.__player_score, "points", '\n')
            return "correct"

        # Hint Text
        elif player_input.lower() == "hint":
            print("Hint:", self.__hint, '\n')
            return "hint_text"

        # All other answers (incorrect)
        else:
            print("Your answer of", player_input, "is not correct", '\n')
            print("Your Current Score is", self.__player_score, "points", '\n')
            return "incorrect"


class Final_Question:

    # Init Method for the Final Question Class
    def __init__(self, question, correct_answer, hint):
        self.__question = question
        self.__correct_answer = correct_answer
        self.__hint = hint

    # Prints the final question and displays it for the player
    def print_question(self):
        print('\n' + self.__question)

    # Player input method that retrieves the player input and then decides if the answer is either correct or incorrect
    def get_player_input(self):
        player_input = input("Please enter your answer to the question >>> ")

        # Correct answer
        if player_input.lower() == self.__correct_answer:
            print("Your answer of", player_input, "is correct!", '\n')
            return "correct"

        # Hint Text
        elif player_input.lower() == "hint":
            print("Hint:", self.__hint, '\n')
            return "hint_text"

        # All other answers (incorrect)
        else:
            print("Your answer of", player_input, "is not correct", '\n')
            return "incorrect"


class top_scores:
    
    def __init__(self):
        self.__high_score = 0
        self.__name = "AAA"
        
    def get_high_score(self):
        return self.__high_score

    def set_high_score(self, player_score):
        self.__name = input("Please enter the name for your high score! >>> ")
        self.__high_score = player_score

    def display_high_score(self):
        print(self.__name, "with a total of", self.__high_score, "points")


def main():

    # Constants
    first_option = "1.) Play Quiz"
    second_option = "2.) Show High Scores"
    third_option = "3.) Quit Program"

    # Variable initialization to be used at a later time
    question_number = 0
    player_score = 0
    new_place_number = -1

    terminate_program = False
    new_high_score = False

    # Question object creation

    # Question(Question that you want answered, Correct answer to question,
    #           Hint to the question, Player score variable)

    question_1 = Question("What is the capital of Minnesota?", "st. paul",
                          "it is one of the \"twin cities\" ", player_score)

    question_2 = Question("What color is the sky on a sunny day (test question)", "blue",
                          "hint text", player_score)

    question_3 = Question("Filler Question Number 3", "correct",
                          "hint text", player_score)

    question_4 = Question("Filler Question Number 4", "correct",
                          "hint text", player_score)

    question_5 = Question("Filler Question Number 5", "correct",
                          "hint text", player_score)

    question_6 = Question("Filler Question Number 6", "correct",
                          "hint text", player_score)

    question_7 = Question("Filler Question Number 7", "correct",
                          "hint text", player_score)

    question_8 = Question("Filler Question Number 8", "correct",
                          "hint text", player_score)

    question_9 = Question("Filler Question Number 9", "correct",
                          "hint text", player_score)

    # Final_Question class (Special class to not display the current score at the end and just state the final score)
    question_10 = Final_Question("Filler Question Number 10", "correct", "hint text")

    # Question array that is used to call on the questions while the loop is active
    questions_array = [question_1, question_2, question_3, question_4, question_5,
                       question_6, question_7, question_8, question_9, question_10]

    # Top scores object creation (top scores class)
    first_place = top_scores()
    second_place = top_scores()
    third_place = top_scores()
    fourth_place = top_scores()
    fifth_place = top_scores()
    sixth_place = top_scores()
    seventh_place = top_scores()
    eighth_place = top_scores()
    ninth_place = top_scores()
    tenth_place = top_scores()

    # Top scores array (used to write to the top scores correctly)
    top_scores_array = [first_place, second_place, third_place, fourth_place, fifth_place,
                        sixth_place, seventh_place, eighth_place, ninth_place, tenth_place]

    while terminate_program == False:

        # Constants listed above
        print('\n' + "Options")
        print(first_option)
        print(second_option)
        print(third_option)
        print()

        initial_input = input("Please Select an option from the list >>> ")

        if initial_input == "1":

            while question_number < 10:

                # Check to see if the question number is the final question
                # (Note: the 9th entry in the array is question 10)
                if isinstance(questions_array[question_number], Question):

                    # Update scoring of the current question before it is prompted
                    # to correctly display the current score
                    questions_array[question_number].update_player_score(player_score)

                # Display the current question
                questions_array[question_number].print_question()

                # Returns the current state of the question (hint, correct, or incorrect)
                question_state = questions_array[question_number].get_player_input()

                # Displays the hint text then proceeds to go back a question to counteract the default question increase
                if question_state == "hint_text":
                    question_number = question_number - 1

                # Increases the player score if the current state of the question is correct
                elif question_state == "correct":
                    player_score = player_score + 1

                # Default question increment
                question_number = question_number + 1

            # After the loop is broken, display the final score and terminate the code
            print('\n' + "Your final score is", str(player_score) + "!", '\n' + "Congratulations!")

            # Check for a new high score
            for place_number in range(9, -1, -1):
                if player_score > top_scores_array[place_number].get_high_score():
                    new_place_number = place_number
                    new_high_score = True

            if new_high_score == True:

                if new_place_number is not 9:
                    for update_top_scores_table in range(9, new_place_number - 1, -1):
                        top_scores_array[update_top_scores_table] = top_scores_array[update_top_scores_table - 1]

                    top_scores_array[new_place_number].set_high_score(player_score)

            new_place_number = -1
            new_high_score = False

        elif initial_input == "2":

            print()
            for place_number in range(0, 10, 1):
                top_scores_array[place_number].display_high_score()
            print()

        else:
            terminate_program = True


main()
