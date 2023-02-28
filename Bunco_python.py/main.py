import bunco


def main():
    # Your program code should start here
    bunco.play_game()
    play_again = input("Play again? (y/n)")
    if play_again == 'y' or play_again == 'Y':
        main()



if __name__ == '__main__':
    main()