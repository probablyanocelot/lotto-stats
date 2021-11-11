# MEGAMILLIONS - https://data.ny.gov/api/views/5xaw-6ayf/rows.csv?accessType=DOWNLOAD
import urllib.request
import os

sheet_destination = './sheets/'

mm_url = "https://data.ny.gov/api/views/5xaw-6ayf/rows.csv?accessType=DOWNLOAD"
mm_file_name = "MegaMillions.csv"

c4l_url = "https://data.ny.gov/api/views/kwxv-fwze/rows.csv?accessType=DOWNLOAD&sorting=true"
c4l_file_name = "Cash4Life.csv"


def master():
    '''MAKE MORE MODULAR & USE PICKLES OF USER INPUT FROM add_lotto()'''
    dl(mm_url, mm_file_name)
    dl(c4l_url, c4l_file_name)


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
