import pandas as pd
import time
import datetime as dt
import matplotlib.pyplot as plt
from downloader import sheet_destination


""" ------------------------------------ CONFIG ------------------------------------ """

''' MASTER CONFIG? '''


''' LOTTO CONSTANTS '''
# TODO: standardize dataframes to lessen constants needed
MM_LAST_CHANGE = dt.datetime(2017, 11, 28)


LOTTO_CONST = {
    "MegaMillions":   {
        "FILENAME": "MegaMillions.csv",
        "WINNERS": "Winning Numbers",
        "SORT CRITERIA": dt.datetime(2020, 9, 28),
    },
    'Cash4Life':  {
        "FILENAME": "Cash4Life.csv",
        "WINNERS": "Winning Numbers",
    },
}

''' SORT CRITERIA TYPES '''
DATE = dt.datetime


''' CONTAINERS '''

roll1 = []
roll2 = []
roll3 = []
roll4 = []
roll5 = []
roll_nest = [roll1, roll2, roll3, roll4, roll5]

roll_dict = {key: None for key in LOTTO_CONST}


''' ERRORS '''


def HANDLER(x): return print(x)


ERR_LOTTO_TYPE = 'ERR: INVALID "lotto_type"!!!!!!!!!!!\n-\n000000000---DataFrame unchanged!---000000000'


"""                          ------------ TODO ------------                         """

# USE INPUT TO SET 'lotto_type' THEN USE AS CONDITION FOR ARG VALUES IN MASTER

# e.g.       lotto_type = input() , if lottotype == 'mm':  data_location = MM_LOCATION

# CREATE LOTTO TYPE ERROR HANDLER FUNCTION TO MINIMIZE REPEAT -- see dates_to_dt() else: return


def master(lotto_type, chart=True, **sort_criteria):
    data = collect_data(sheet_destination +
                        LOTTO_CONST[lotto_type]["FILENAME"])
    data = sort_df(data, lotto_type)
    if sort_criteria:
        filtered_data = filter_df(data, lotto_type, sort_criteria)
        main_rolls = get_main_rolls(filtered_data, lotto_type)
    else:
        main_rolls = get_main_rolls(data, lotto_type)
    # populate dict with index: roll(as a list, using .split()) -- MAYBE INEFFICIENT
    append_roll_dict(lotto_type, main_rolls)
    rolls_to_containers(lotto_type, main_rolls)
    if chart:
        if sort_criteria:
            charter(lotto_type, filtered_data)
        else:
            charter(lotto_type, data)
        wipe()
    else:
        return main_rolls


def collect_data(data_location):
    if data_location.endswith('.csv'):
        df = pd.read_csv(data_location)
    else:
        print('ERR: Invalid or Unsupported File Extension')
        manual_data_location = input('YOU MAY MANUALLY ENTER DATA LOCATION(relative or finite)\n'
                                     + 'INPUT /Q TO EXIT(not case sensitive)\n:')
        if manual_data_location.lower() == '/q':
            quit()
        else:
            collect_data(manual_data_location)

    print("\n---ORIGINAL DATAFRAME---\n", df)
    return df


"""
Date Col To dt format
    str(lotto_type):
        'mm' : Mega millions
        'pb' : PowerBall
"""


def dates_to_dt(df, lotto_type):

    print("---Dates To DT---\n")

    if not df['Draw Date'].empty:
        df['Draw Date'] = pd.to_datetime(df["Draw Date"])
        print("---CHECK FOR DATE-TIME TYPE---\n", type(df['Draw Date'][0]))
    else:
        return HANDLER(ERR_LOTTO_TYPE)

    # ADD IF RECUR: FN(DF); ELSE: RETURN DF
    return df


"""Gather Data, Sort Selected Col"""


def sort_df(df, lotto_type):

    # CREATE IF STATEMENT TO HANDLE SORT CRITERIA
    dates_to_dt(df, lotto_type)

    print("\n---SORTING ---\n")
    if not df['Draw Date'].empty:
        df = df.sort_values("Draw Date")
        print("\n---SORTED DATA---\n", df)
    else:
        # MAYBE COPY COLLECT_DATA() FORMAT; OR USE WRAPPER
        return HANDLER(ERR_LOTTO_TYPE)

    # ADD IF RECUR: NEXT_FN(DF); ELSE: RETURN DF
    return df


""""New IDX, Old Moved To Col[0]"""


def reset_index_retain(df):

    # ABSTRACT & NAME IDX_# ++ IF OLD IDX ALREADY EXISTS
    df = df.reset_index().rename(columns={'index': 'idx_orig'})
    print('---ARCHIVING PREV. INDEX---\n', df)
    return df


"""Filter DF, Reset IDX & Retain Previous as: idx_orig"""


def filter_df(df, lotto_type, sort_criteria):  # test is_broken
    # print(type(sort_criteria), type(DATE))
    # get type of value in dict[lotto][sort_criteria]
    print(type(MM_LAST_CHANGE), type(DATE))
    # broken
    # if type(MM_LAST_CHANGE) == DATE:
    #     if lotto_type == "mm":
    #         col_name = "Draw Date"
    #         criteria = sort_criteria
    #         after_change = df[col_name] >= criteria
    #     else:
    #         return HANDLER(ERR_LOTTO_TYPE)
    # else:
    #     print('CRITERIA TYPE UNCHANGED')

    ''' TESTING FOR MASTER FUNCTION while not is_broken: fns '''
    # is_broken = True
    # return is_broken
    print(df)
    col_name = "Draw Date"
    print("DEBUG: 161 ", df[col_name], sort_criteria)
    after_change = df[col_name] >= LOTTO_CONST[lotto_type]["SORT CRITERIA"]
    print('---CRITERIA MET?---\n', after_change)
    df = df.loc[after_change]
    print('---DF AFTER CHANGE---\n', df)
    reset_index_retain(df)
    return df


'''                         !!!!! --- CLEAN FROM HERE --- !!!!!                         '''


# Reset Index & Remove Old
def clean_idx(df):
    df = df.reset_index().drop(columns='index')
    return df


def get_main_rolls(df, lotto_type):
    col_name = LOTTO_CONST[lotto_type]["WINNERS"]
    # RETURN DF : index, col_name
    df = df[str(col_name)]
    df = clean_idx(df)
    df = df.reset_index()
    print(df)
    return df

    # --------- PUT IN SEPARATE FUNCTION
    # ITERATE OVER DF, POPULATE DICT WITH:    idx:cell(.split, if needed)
    counter = 0
    for index, row in df.iterrows():
        # while counter < 0:
        #     roll_dict['mm'].update({'mm':{row['index']: row['c2']}})

        # idx = df.index[df.row]
        # print(df.loc[idx])
        roll = row[col_name].split()
        print(roll)
        roll_dict[lotto_type] += {row['index']: row[col_name]}


def append_roll_dict(lotto_type, main_rolls):
    roll_dict.update({
        lotto_type: {x: None for x in range(0, len(main_rolls.index))}
    })


# CHECKS COMBOS --- NEEDS POLISHING & MODULARIZE --- MOVED FROM LINE 157(END OF FILE)
def num_checker():
    for num1 in range(1, 14):
        for num2 in range(9, 38):
            if num1 < num2:
                for num3 in range(22, 48):
                    if num2 < num3:
                        for num4 in range(39, 62):
                            if num3 < num4:
                                for num5 in range(55, 70):
                                    if num4 < num5:
                                        gen_list = [
                                            num1, num2, num3, num4, num5]
                                        # print(gen_list)
                                        for i in range(0, len(roll_dict['mm'])):
                                            if gen_list[0] == int(roll_dict['mm'][i][0]):
                                                print(
                                                    gen_list, roll_dict['mm'][i][0])
                                                # print([num1,num2,num3,num4,num5], " IS IN DICT: ", roll)


# STORED STATES OF DF
"""
df_by_date_mm = data(MEGA_MILLIONS)
sorted_df = filter_by_date(data(MEGA_MILLIONS), 'Draw Date', MM_LAST_CHANGE)"""


def rolls_to_containers(lotto_type, main_rolls):

    # MODULARIZE & MOVE THIS!!!!!!!!!!!!!!1
    # POPULATE DICT WITH new idx : cell_data(.SPLIT DEFAULT UNTIL MODULARIZED(if x then split))
    # def dict_update():
    for i in range(0, len(main_rolls.index)):
        # print(main_rolls.iloc[i]['index'])
        roll_dict[lotto_type][i] = main_rolls.iloc[i]['Winning Numbers'].split()

    # ITERATE OVER VALUES, CREATE DF: COLS=ROLL PER SLOT, LEAST -> GREATEST NUM
    for group in roll_dict[lotto_type]:
        print(group)
        for i in range(0, len(roll_dict[lotto_type][group])):
            print(roll_dict[lotto_type][group][i])
            roll_nest[i].append(roll_dict[lotto_type][group][i])

    print("\n---ROLL DICT---\n", roll_dict)
    print("\n---ROLL NEST---\n", roll_nest)


# NEEDS ABSTRACTING FOR DIFFERENT LOTTERY 'SPECIAL BALL'
def charter(lotto_type, sorted_df):
    df = pd.DataFrame({'roll1': roll1, 'roll2': roll2,
                      'roll3': roll3, 'roll4': roll4, 'roll5': roll5})
    print("\n---DF : 1 COL PER ROLL---\n", df)
    df = df.astype(float)

    # Initialise the subplot function using number of rows and columns
    figure, axis = plt.subplots(2, 6)

    df.plot.hist(ax=axis[0, 0], stacked=True)
    df['roll1'].plot.hist(ax=axis[0, 1])  # , density=True)
    df['roll2'].plot.hist(ax=axis[0, 2])  # , density=True)
    df['roll3'].plot.hist(ax=axis[0, 3])  # , density=True)
    df['roll4'].plot.hist(ax=axis[0, 4])  # , density=True)
    df['roll5'].plot.hist(ax=axis[0, 5])  # , density=True)
    df = sorted_df
    print('PRINTING SORTED DF \n', df)

    # REPLACE WITH ABSTRACTION (PUT 'AFFIXES(MBALL, ETC)' IN DICT, USE 'FOR ENUM(AFFIXES): )
    col_count = 1
    for col in df.iloc[:, 2: len(df.columns)]:
        df[col].plot.hist(ax=axis[1, col_count], density=True)
        col_count += 1
        # df['Multiplier'].plot.hist(ax=axis[1,2], density=True)
    num_list = []
    print(df)

    # convert df entries from list['string'] to individual integers
    for string in sorted_df[LOTTO_CONST[lotto_type]['WINNERS']]:
        # print(type(string))
        a_list = string.split()
        map_object = map(int, a_list)
        list_of_integers = list(map_object)
        for num in list_of_integers:
            num_list.append(num)
    df = pd.Series(num_list)
    df.plot.hist(ax=axis[1, 0])

    plt.xlabel("Numbers")
    plt.ylabel('Frequency')
    # df = df['Winning Numbers'].astype(float)
    # df['Winning Numbers'].plot.hist(ax=axis[1,0], density=True)

    plt.show()


def wipe():
    for cntnr in roll_nest:
        cntnr.clear()
    roll_dict.clear()


if __name__ == '__main__':
    master('MegaMillions',
           sort_criteria=LOTTO_CONST['MegaMillions']["SORT CRITERIA"])
    # master('c4l')
