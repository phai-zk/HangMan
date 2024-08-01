from hangman_state import HangmanState as State;
from game_rule import GameRule as Rule;
import os

def reDisplay():
    os.system("clear")
    print("========= Welcome To Hangman =========")

def reAnswerDisplay(state, wrong=False):
    reDisplay()
    if (wrong): print("** Your answer is not in the chios **")
    state.show()
    print("======================================")

def gamePlay(state, rule):
    win = False
    wrongANS = False
    while(state.getState() < 6 and not(win) ):
        while(True):
            reAnswerDisplay(state, wrongANS)
            print(f"Chios : {(' ').join(rule.chios)}")
            print(f"Answer : {(' ').join(rule.answer)}")
            ans = input("your answer : ").strip()
            if (ans.upper() in rule.chios) :
                if not(rule.check(ans)):
                    print("Wrong Ur Noop LoL :(")
                    state.nextState()
                reDisplay()
                wrongANS = False
                break
            else:
                wrongANS = True

        if (rule.endGame()):
            win = True
            break

    return (win)

def Game():
    while(True):
        state = State()
        rule = Rule()
        reDisplay()
        if (gamePlay(state, rule)):
            state.show()
            print("================ YOU WIN ================")
            print(f"The answer is {('').join(rule.answer)}")
        else:
            state.show()
            print("=============== GAME OVER ===============")
            print(f"Answer is : {rule.word}")
        
        out = None
        while (True):
            out = input("Do you wanna play again? (Y/n) : ").upper()
            if (out == "Y" or out == "N"):
                break
        if (out == "Y"):
            reDisplay()
            pass
        else:
            break


def main():
    while(True):
        play = input("Do you wanna play Hangman? (Y/n) : ").upper()
        if (play == "Y"):
            Game()
            break
        elif (play == "N"):
            break

main()