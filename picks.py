import datetime as dt
import spin2win
import pandas as pd
import numpy as np
import re

'''USE TO KEEP UP WITH PERSONAL NUMBERS & WINNING STATUS'''

rolls = spin2win.master('MegaMillions', chart=False,
                        sort_criteria=spin2win.LOTTO_CONST['MegaMillions']['SORT CRITERIA'])

print(rolls)

pick_dict = {
    lotto: {
    } for lotto in spin2win.LOTTO_CONST
}

print(pick_dict)


def collect_rolls(lotto_type):
    if not lotto_type:
        lotto_type = input(
            'input lottery name in CamelCase(no spaces), e.g. Cash4Life\n: ')
    slot1 = input('slot 1\n: ')
    slot2 = input('slot 2\n: ')
    slot3 = input('slot 3\n: ')
    slot4 = input('slot 4\n: ')
    slot5 = input('slot 5\n: ')
    special = input('special\n: ')
    if special <= 0 | special > 99:
        print('special number out of range')
        special = input('special\n: ')
    purchase_date = input('purchase date\n: ')
    expiry_date = input('expiration date\n: ')
    roll = [slot1, slot2, slot3, slot4, slot5, special]

    # make doable for more than just 5 roll lotto
    pick_dict[lotto_type]['roll'] = roll[0:5]
    pick_dict[lotto_type]['special ball'] = special
    pick_dict[lotto_type]['start,end'] = [purchase_date, expiry_date]


my_list = [5, 39, 48, 50, 64]


def zero_handler(num_list):
    for num in num_list:
        if len(str(num)) == 1:
            num = int('0' + str(num))
        print(num)


print(my_list)
zero_handler(my_list)
print(my_list)

# print(re.match(r'\d\d', str(my_list)))

rolls['new_col'] = (rolls['Winning Numbers']
                    # do some re.matching here r'\d\d'
                    .str.findall(f"({'|'.join(str(my_list))})")
                    .str.join(' ')
                    .replace('', np.nan))


# rolls['new_col'] = (rolls['Winning Numbers'].isin())
print(rolls)


rolls['isin1'] = rolls['Winning Numbers'].isin(my_list)
print(rolls)
# print('you won')


for num in my_list:
    print(num)

    # for num in my_list:
