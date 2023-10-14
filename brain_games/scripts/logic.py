from brain_games_1 import cli
import prompt


def logic_game(game):
    cli.welcome_user()
    play = game.RULES
    print(play)
    for _ in range(3):
        correct_answer, question = game.get_game()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f'Let\'s try again, {cli.name}!')
            return
    print(f'Congratulations, {cli.name}!')