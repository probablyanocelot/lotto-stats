import downloader
import spin2win

print('\n\n-------------SPIN-2-WIN USER INTERFACE-------------\n')
print('ENTER "e" WITHOUT QUOTATIONS TO EXIT!!!!\n')

options = []
option_main = ["Personal Picks", "Update Files", "Data & Charts"]
option_lotto_type = ['mm', 'c4l']


option_dict = {
    v: k for v, k in enumerate(options)
}

wipe_containers = [options, option_dict]


def master(option_list):
    wipe()
    pop_list(options, option_list)
    pop_dict(options, option_dict)
    options_interface(option_dict)


def pop_list(options, option_list):
    for option in option_list:
        options.append(option)


def pop_dict(options, option_dict):
    option_dict.update({
        v: k for v, k in enumerate(options)
    })


def options_interface(option_dict):
    print("\nOPTIONS : ")
    for i, x in enumerate(option_dict):
        print(" " + str(i) + " : " + str(option_dict[i]))
    user_input = choice(option_dict)
    choice_handler(user_input)


def choice(option_dict):

    user_choice = input('\n\nENTER CHOICE(digits only!) : ')
    if user_choice.lower() == 'e':
        quit()
    elif user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice in range(0, len(option_dict)):
            user_choice = option_dict[user_choice]
            return user_choice
        else:
            print('\n\nCHOICE OUT OF RANGE\n\n')
            options_interface(option_dict)
    else:
        print('CHOICE MUST BE DIGIT')


def choice_handler(choice):
    if choice == "Update Files":
        downloader.master()
    elif choice == "Data & Charts":
        master(option_lotto_type)
    elif choice == 'mm':
        spin2win.master(choice, sort_criteria=spin2win.MM_LAST_CHANGE)
    elif choice == 'c4l':
        spin2win.master(choice)
    master(option_main)


def wipe():
    for cntnr in wipe_containers:
        cntnr.clear()


if __name__ == '__main__':
    master(option_main)
