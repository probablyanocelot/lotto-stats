import pandas as pd
import matplotlib.pyplot as plt
import organizer
from organizer import LOTTO_CONST
from organizer import key_data


mm = key_data('mm', sort_criteria=LOTTO_CONST['mm']['SORT CRITERIA'])


'''NEEDS ABSTRACTING FOR DIFFERENT LOTTERY SPECIAL BALL'''

# rpc = roll per col


def chart(lotto_type, data, rpc):

    df = data.astype(float)

    # Initialise the subplot function using number of rows and columns
    figure, axis = plt.subplots(2, 6)

    df.plot.hist(ax=axis[0, 0], stacked=True)
    df['roll1'].plot.hist(ax=axis[0, 1])  # , density=True)
    df['roll2'].plot.hist(ax=axis[0, 2])  # , density=True)
    df['roll3'].plot.hist(ax=axis[0, 3])  # , density=True)
    df['roll4'].plot.hist(ax=axis[0, 4])  # , density=True)
    df['roll5'].plot.hist(ax=axis[0, 5])  # , density=True)
    # df = sorted_df
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


chart('mm', mm)
