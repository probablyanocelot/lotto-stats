import datetime as dt
import organizer

'''USE TO KEEP UP WITH PERSONAL NUMBERS & WINNING STATUS'''


mm = {
    "l_type": 'mm',
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
    "l_type": 'c4l',
    0: {
        "roll": [5, 19, 30, 40, 54],
        "special_ball": 2,
        "start,end": [dt.datetime(2021, 9, 28), dt.datetime(2021, 10, 2)]
    }
}

ctnrs = [mm, c4l]


def check(lotto_type, data):
    '''
    FIX
    '''
    for ctnr in ctnrs:
        print(ctnr)
        if lotto_type == ctnr['l_type']:
            for i in ctnr:
                nums = ctnr[i]["roll"]
                special = ctnr[i]['special_ball']
                start = ctnr[i]['start,end'][0]
                end = ctnr[i]['start,end'][1]


check('mm', organizer.master('mm'))
