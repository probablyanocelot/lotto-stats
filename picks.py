import datetime as dt
import spin2win
import pandas as pd
import numpy as np
import re
import fuzzymatcher

'''USE TO KEEP UP WITH PERSONAL NUMBERS & WINNING STATUS'''

'''

1.    PERSONAL NUMBER CHECKER
        --> fuzzymatcher? sql?
'''


rolls = spin2win.master('MegaMillions', chart=False, print_on=False,
                        sort_criteria=spin2win.LOTTO_CONST['MegaMillions']['SORT CRITERIA'])

pick_dict = {
    lotto: {
    } for lotto in spin2win.LOTTO_CONST
}


# User Input
def collect_picks(lotto_type, default=False):
    slot_amount = spin2win.roll_counter(
        spin2win.master(lotto_type, chart=False)["Winning Numbers"].loc[0])
    print(slot_amount)
    print([num for num in range(0, slot_amount)])
    if not lotto_type:
        lotto_type = input(
            'input lottery name in CamelCase(no spaces), e.g. Cash4Life\n: ')
    if not default:
        slot1 = input('slot 1\n: ')
        slot2 = input('slot 2\n: ')
        slot3 = input('slot 3\n: ')
        slot4 = input('slot 4\n: ')
        slot5 = input('slot 5\n: ')
        special = input('special\n: ')
        while special <= 0 | special > 99:
            print('special number out of range')
            special = input('special\n: ')
        start_date = input('purchase date\n: ')
        end_date = input('expiration date\n: ')
        picks_to_container(lotto_type, special, start_date, end_date,
                           slot1, slot2, slot3, slot4, slot5)
    else:
        slot1 = 1
        slot2 = 10
        slot3 = 25
        slot4 = 36
        slot5 = 58
        special = 15
        start_date = '2019-01-01'
        end_date = '2021-12-25'
        picks_to_container(lotto_type, special, start_date, end_date,
                           slot1, slot2, slot3, slot4, slot5)


# Input to Containers
def picks_to_container(lotto_type, special, start_date, end_date, *slots):
    roll = [*slots, special]

    new_entry = len(pick_dict[lotto_type])
    pick_dict[lotto_type][new_entry] = dict()

    # make doable for more than just 5 roll lotto
    pick_dict[lotto_type][new_entry]['roll'] = num_group_to_str(
        roll[0:len(roll)-1])
    pick_dict[lotto_type][new_entry]['special ball'] = special
    pick_dict[lotto_type][new_entry]['start,end'] = [start_date, end_date]
    print(pick_dict)


def zero_handler(num):
    num = str(num)
    if len(num) == 1:
        num = '0' + num
    print(num)
    return num


def num_group_to_str(my_group):
    # group can be any iterable
    my_group = [zero_handler(num) for num in my_group]
    my_str = ' '.join(my_group)
    return my_str


collect_picks('MegaMillions', default=True)

print('pick dict:\n', pick_dict)

my_list = [5, 39, 48, 50, 64]


my_dict = {
    0: '05 39 48 50 64',
}

pick_df = pd.DataFrame.from_dict(
    pick_dict['MegaMillions'], orient='index', columns=['roll', 'special ball', 'start,end'])
print(pick_df)

for row in pick_df:
    print(fuzzymatcher.fuzzy_left_join(rolls, pick_df['roll'])


# for row in rolls['Winning Numbers']:
#     print(row)
# print(fuzzymatcher.fuzzy_left_join())


'''



print(re.match(r'\d\d', str(my_list)))

rolls['new_col'] = (rolls['Winning Numbers']
                    # do some re.matching here r'\d\d'
                    .str.findall(f"({'|'.join(str(my_list))})")
                    .str.join(' ')
                    .replace('', np.nan))


rolls['new_col'] = (rolls['Winning Numbers'].isin())
rolls['isin1'] = rolls['Winning Numbers'].isin(my_list)



'''
