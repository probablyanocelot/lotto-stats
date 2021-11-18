# MULTIPLE SPREADSHEET/LOTTERY FORMATS
import spin2win
import pandas as pd
import re
import os
import glob


# for dir_df_dict fn
data = {}


def dir_df_dict():
    for filename in glob.glob('./sheets/*.csv'):
        data[filename[:-4]] = pd.read_csv(filename, sep=",")
    print(data)
    print(data.keys())


winn = 'WINN'

winning_patterns = [
    'winn',
]
special_patterns = [
    'ball',
]
multiplier_patterns = [
    'multi',
]

special_ball = 'Special Ball'


def match_category(df, pattern):
    for category in df:
        if type(pattern) == str:
            if re.match(winn.lower(), str(category).lower()):
                return category
        elif type(pattern) == list:
            for p in pattern:
                if re.match(p.lower(), str(category).lower()):
                    return category


def parse_roll_amount(df, target_col, new_column):
    '''
    Objective: return the number of rolls in a column.
    if special ball is in wrong column,
    will move it to the correct column
    '''
    wnums = (re.findall(r'\d+', (df[target_col][0])))
    length = len(wnums)
    print(length)
    if wnums[-1] <= wnums[-2]:
        length = length - 1
        special_ball_roll = wnums[-1]
        total_columns = len([col for col in df])
        if not new_column in [col for col in df]:
            if 'Filename' in [col for col in df]:
                df.insert(
                    total_columns-1, special_ball, '')
            else:
                df.insert(total_columns, special_ball, '')
        separator(df, target_col, new_column)
        df.to_csv('./sheets/' + df['Filename'][0], index=False)

        # return df with winning numbers and special ball separated
        return length
    else:
        return length


def separator(df, column_name, new_column):
    '''
    If special ball is in wrong column, 
    this function will move it to the correct column
    '''
    count = 0
    last_col = len(df.columns) - 1
    for idx, row in enumerate(df[column_name]):
        if re.match(r'\d+', str(row)):
            num_list = re.findall(r'\d+', row)
            df.at[idx, new_column] = num_list[-1]
            df.at[idx, column_name] = df.at[idx,
                                            column_name].replace(num_list[-1], '')
    print(df)


if __name__ == '__main__':
    df = spin2win.collect_data('./sheets/Powerball.csv')
    winner_column = match_category(df, winn)
    new_column = special_ball
    match_category(df, multiplier_patterns)
    parse_roll_amount(df, winner_column, special_ball)
