# My partner is Lutfiyah Mohammed


import heifer_generator

import sys


# this is the main function
def main():
    # this generates the cow
    cows = heifer_generator.get_cows()

    # this displays the right type of cow and we know its gonna either be a cow or cat because of the use -n
    if sys.argv[1] == '-n':
        if sys.argv[2] == 'heifer':
            message = sys.argv[3:]
            message_joined = ' '.join(message)
            print(message_joined)
            print(cows[0].get_image())
        elif sys.argv[2] == 'kitteh':
            message = sys.argv[3:]
            message_joined = ' '.join(message)
            print(message_joined)
            print(cows[1].get_image())
        else:
            print(f'Could not find {sys.argv[2]} cow!')
    # this prints out all cow types
    elif sys.argv[1] == '-l':
        print("Cows available: ", end="")
        print(cows[0].get_name() + " " + cows[1].get_name())



    # this is the default cow with any message
    else:
        message = sys.argv[1:]
        message_joined = ' '.join(message)
        print(message_joined)
        print(cows[0].get_image())


# this calls the main function
if __name__ == "__main__":
    main()

