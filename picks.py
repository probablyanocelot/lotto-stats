import datetime as dt
import spin2win

'''USE TO KEEP UP WITH PERSONAL NUMBERS & WINNING STATUS'''

pick_dict = {
    "lotto_type": {
        lotto for lotto in spin2win.LOTTO_CONST
    }
}


def collect_rolls():
    slot1 = input(1)
    slot2 = input(2)
    slot3 = input(3)
    slot4 = input(4)
    slot5 = input(5)
    special = input('special')
    roll = [slot1, slot2, slot3, slot4, slot5, special]


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


c4l = {
    "lotto type": 'Cash4Life',
    0: {
        "roll": [5, 19, 30, 40, 54],
        "special_ball": 2,
        "start,end": [dt.datetime(2021, 9, 28), dt.datetime(2021, 10, 2)]
    }
}

personal_num_dict = {
    "l_type": {
    }
}

ctnrs = [mm, c4l]
print(ctnrs)


def check(lotto_type, data):
    for ctnr in ctnrs:
        print(ctnr)
        if lotto_type == ctnr['l_type']:
            for i in ctnr:
                nums = ctnr[i]["roll"]
                special = ctnr[i]['special_ball']
                start = ctnr[i]['start,end'][0]
                end = ctnr[i]['start,end'][1]


# check('mm', spin2win.collect_data)
