# MEGAMILLIONS - https://data.ny.gov/api/views/5xaw-6ayf/rows.csv?accessType=DOWNLOAD
import urllib.request
import pickle
import os
from os.path import exists

ext = ['.csv', '.xlsx', '.json']

sheet_destination = './sheets/'


mm_url = "https://data.ny.gov/api/views/5xaw-6ayf/rows.csv?accessType=DOWNLOAD"
mm_file_name = "MegaMillions.csv"

c4l_url = "https://data.ny.gov/api/views/kwxv-fwze/rows.csv?accessType=DOWNLOAD&sorting=true"
c4l_file_name = "Cash4Life.csv"

if exists('./sheet_pickle.p'):
    sheet_dict = pickle.load(open('sheet_pickle.p', 'rb'))
else:
    sheet_dict = {
        'MegaMillions': {'url': mm_url,
                         'filename': mm_file_name},
        'Cash4Life': {'url': c4l_url,
                      'filename': c4l_file_name},
    }


def master():
    '''MAKE MORE MODULAR & USE PICKLES OF USER INPUT FROM add_lotto()'''
    for lotto in sheet_dict:
        dl(sheet_dict[lotto]['url'], sheet_dict[lotto]['filename'])
    # dl(mm_url, mm_file_name)
    # dl(c4l_url, c4l_file_name)


def dl(url, filename):
    print("Beginning download...")
    urllib.request.urlretrieve(url, filename=sheet_destination + filename)


def create_sheetdir():
    if not os.path.exists(sheet_destination):
        os.mkdir(sheet_destination)


def add_lotto(url, filename):
    dl(url, filename)


create_sheetdir()


if __name__ == '__main__':
    master()
