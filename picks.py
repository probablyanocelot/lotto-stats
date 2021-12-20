import datetime as dt
import spin2win

'''USE TO KEEP UP WITH PERSONAL NUMBERS & WINNING STATUS'''

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


collect_rolls('MegaMillions')
print(pick_dict)
mm = {
    "lotto type": 'MegaMillions',
    0: {
        "roll": [3, 7, 37, 40, 69],
        "special_ball": 8,
        "start,end": [dt.datetime(2021, 9, 28), dt.datetime(2021, 10, 12)]
    },
    1: {
        "roll": [2, 16, 35, 47, 65],
        "special_ball": 17,
        "start,end": [dt.datetime(2021, 9, 21), dt.datetime(2021, 10, 22)]
    }
}


def check(lotto_type, data):
    for ctnr in ctnrs:
        print(ctnr)
        if lotto_type == ctnr['l_type']:
            for i in ctnr:
                nums = ctnr[lotto_type][i]["roll"]
                special = ctnr[lotto_type][i]['special_ball']
                start = ctnr[lotto_type][i]['start,end'][0]
                end = ctnr[lotto_type][i]['start,end'][1]


# check('mm', spin2win.collect_data)
