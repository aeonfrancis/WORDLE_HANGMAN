import random
import sys
import time
from termcolor import colored


def print_menu():
    w = colored("W ", "green", attrs=["bold"])
    o = colored("O ", "white", attrs=["bold"])
    r = colored("R ", "cyan", attrs=["bold"])
    d = colored("D ", "yellow", attrs=["bold"])
    l = colored("L ", "magenta", attrs=["bold"])
    e = colored("E ", "red", attrs=["bold"])
    f = colored("𝟝", "yellow", attrs=["bold"])
    ent = colored("ENTER!", "green", attrs=["bold"])
    print(
        f"""\nLet's play {w}{o}{r}{d}{l}{e} together with 🅷 🅰  🅽 🅶 🅼 🅰  🅽 ❗""")
    time.sleep(2)
    print(f"""\nType a {f}letter word and hit {ent}

    If the letter is NOT in the word, the letter is colored \33[30m'WHITE',\33[37m
    If the letter is in the word but NOT in the right position, the letter is colored \33[33m'YELLOW',\33[37m
    If the letter is in the word and in the right position, the letter is colored \33[32m'GREEN'.\33[37m
    Only the first five letters will be considered.\n""")


n = 0
x_anc = ""
x_anc1 = ""
x_anc0 = ""
x_anc00 = ""


def process_guess(the_answer, the_guess):
    position = 0
    clue = ""

    for letter in the_guess:
        if letter == the_answer[position]:
            clue += colored(letter, "green")
        elif letter in the_answer:
            clue += colored(letter, "yellow")
        else:
            clue += letter
        position += 1

    global n, x_anc, x_anc0, x_anc00, x_anc1
    a = colored("   0   ", "red", attrs=["bold"])
    a1 = "  /|\ "
    a1r = colored("|", "red", attrs=["bold"])
    a2 = colored("  /|\  ", "red", attrs=["bold"])
    a3 = colored("  /", "red", attrs=["bold"])
    a20 = colored("  |||  ", "red", attrs=["bold"])
    a40 = colored("  | | ", "red", attrs=["bold"])
    a4 = colored("  / \ ", "red", attrs=["bold"])
    a5 = "    "
    a6 = "     "
    a50 = "  / \ "
    x = colored("_____", "green", "on_green")
    z = x_anc0+"   |"

    if n == 0:
        if guess == answer:
            print(clue)
        else:
            print(clue + a + "\n\n\n"+x+"   ")
            x_anc0 = clue
            n += 1
    elif n == 1:
        if guess == answer:
            print(clue)
        else:
            x_anc = clue
            print(x_anc + a1.replace("|", a1r)+"\n\n\n"+x+"   ")
            n += 1
    elif n == 2:
        if guess == answer:
            print(clue)
        else:
            sys.stdout.write("\033[F")
            print(x_anc + a2)
            print(clue + a50+"\n"+x+"    ")
            x_anc00 = clue
            n += 1
    elif n == 3:
        if guess == answer:
            print(clue)
        else:
            sys.stdout.write("\033[F")
            print(x_anc00 + a3)
            print(clue + a5+"\n"+x+"    ")
            x_anc1 = clue
            n += 1
    elif n == 4:
        if guess == answer:
            print(clue)
        else:
            sys.stdout.write("\033[4F")
            print(z)
            print(x_anc + a)
            print(x_anc00 + a20)
            print(x_anc1 + a40)
            print(clue + a6)


word_list = []
word_file = ["apple", "ghost", "balls", "toads", "sales", "maids",
            "lakes", "cakes", "glass", "troll", "print", "users", "loser"]

for word in word_file:
    word_list.append(word.strip())

answer = random.choice(word_list)


def t1():
    timer = 5
    t0 = timer
    if timer <= 10:
        t0 = colored(timer, "red", attrs=["bold"])
    T = f"Timer: {timer}"
    while timer != 0:
        t = colored("The Game will start in ", "cyan", attrs=["bold"])
        print(t, '{:2d}'.format(timer))
        sys.stdout.write("\033[F")
        time.sleep(1)
        timer -= 1


play_again = ""
while play_again != "n":
    print_menu()
    time.sleep(2)
    t1()

    b = "   0   |"
    c = "  /|\  |"
    d = "  / \  |"
    e = colored("░░░", "blue", attrs=["underline"])
    x = colored("_", "green", "on_green")
    print(f"""        +---+              
{x}{x}{x}{x}{x}{b}
{x}{x}{x}{x}{x}{c}
{x}{x}{x}{x}{x}{d}
{x}{x}{x}{x}{x}  {e}  |
{x}{x}{x}{x}{x}  {e}╔═══╗""")

    guess_count = 1
    while guess_count != 6:
        if guess_count == 1:
            sys.stdout.write("\033[5F")
        elif guess_count == 2 or guess_count == 3:
            sys.stdout.write("\033[3F")
        elif guess_count == 4 or guess_count == 5:
            sys.stdout.write("\033[F")

        guess = input().lower()
        sys.stdout.write("\033[F")

        if len(guess) > 5:
            guess = guess[:5]
        elif len(guess) < 5:
            guess = guess + ((5 - (len(guess))) * " ")

        guess_count += 1
        right_guess = process_guess(answer, guess)
        if guess == answer:
            answer = colored(answer, "yellow", attrs=["bold"])
            y = colored("as the right answer!\n               ", "blue")
            x = f"Congratulations for guessing {answer} {y}"
            if guess_count == 2:
                sys.stdout.write("\033[4E")
                print(colored(x, "blue"))
            elif guess_count == 3:
                sys.stdout.write("\033[3E")
                print(colored(x, "blue"))
            elif guess_count == 4:
                sys.stdout.write("\033[2E")
                print(colored(x, "blue"))
            elif guess_count == 5:
                sys.stdout.write("\033[1E")
                print(colored(x, "blue"))
            else:
                print(colored(x, "blue"))
            guess_count = 6

        elif guess_count == 6:
            m0 = colored("Out of turn,", "red")
            answer = colored(answer, "blue", attrs=["bold"])
            print(f"{m0}\nThe answer is {answer}...")

    n1 = colored("Play again?", "magenta", attrs=["bold"])
    n2 = colored("If yes, press ENTER,", "green", attrs=["bold"])
    n3 = colored("if no, press", "grey", attrs=["bold"])
    n4 = colored("'n'", "red", attrs=["bold"])
    print(f"{n1} {n2} {n3} {n4}.")
    play_again = input().lower()
    sys.stdout.write("\033[F")
    if play_again != "n":
        guess_count = 1
        n = 0
        answer = random.choice(word_list)
    else:
        closing = colored("     \nThank you for playing!",
                          "yellow", attrs=["bold"])
        closing0 = colored("\nHave a nice day....\n", "cyan", attrs=["bold"])
        print(f"{closing}{closing0}")
        break
    print("   ")
