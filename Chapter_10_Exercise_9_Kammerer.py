class Question:

    def __init__(self, question, possible_1, possible_2, possible_3, possible_4, correct_choice):
        self.__question = question
        self.__possible_1 = possible_1
        self.__possible_2 = possible_2
        self.__possible_3 = possible_3
        self.__possible_4 = possible_4
        self.__correct_choice = correct_choice

    def print_question(self):
        print(self.__question, '\n')
        print("1.)", self.__possible_1)
        print("2.)", self.__possible_2)
        print("3.)", self.__possible_3)
        print("4.)", self.__possible_3, '\n')

    def player_1_input(self):

        player_input = int(input("Please Enter Your Guess Player 1 >>> "))

        if player_input == self.__correct_choice:

            print("Correct")
            correct = True

            return correct

        else:
            print("Wrong Answer")

    def player_2_input(self):

        player_input = int(input("Please Enter Your Guess Player 2 >>> "))

        if player_input == self.__correct_choice:

            print("Correct")
            correct = True

            return correct
        else:
            print("Wrong Answer")


def main():
    correct = False

    player_1_score = 0
    player_2_score = 0
    question_number = 0

    question_1 = Question("What is 5 + 5", "7", "10", "11", "13", 2)
    question_2 = Question("What is 5 + 5", "7", "10", "11", "13", 2)
    question_3 = Question("What is 5 + 5", "7", "10", "11", "13", 2)
    question_4 = Question("What is 5 + 5", "7", "10", "11", "13", 2)
    question_5 = Question("What is 5 + 5", "7", "10", "11", "13", 2)
    question_6 = Question("What is 5 + 5", "7", "10", "11", "13", 2)
    question_7 = Question("What is 5 + 5", "7", "10", "11", "13", 2)
    question_8 = Question("What is 5 + 5", "7", "10", "11", "13", 2)
    question_9 = Question("What is 5 + 5", "7", "10", "11", "13", 2)
    question_10 = Question("What is 5 + 5", "7", "10", "11", "13", 2)



    questions = [question_1, question_2, question_3, question_4, question_5, question_6, question_7, question_8, question_9, question_10]

    print('\n')

    while question_number <= 9:

        questions[question_number].print_question()

        if not correct:
            if Question.player_1_input(question_1):
                player_1_score = player_1_score + 1
                correct = True

        if not correct:
            if Question.player_2_input(question_1):
                player_2_score = player_2_score + 1
                correct = True

        if correct:
            question_number = question_number + 1
            correct = False

    print()
    print("Player 1 has", player_1_score, "points")
    print("Player 2 has", player_2_score, "points")

    if player_1_score > player_2_score:
        print('\n', "Player 1  Wins!")
    elif player_2_score > player_1_score:
        print('\n', "Player 2 Wins!")
    else:
        print("Draw")


main()
