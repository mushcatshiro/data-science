import os
import pandas as pd
import matplotlib.pyplot as plt


lst = ['sof19.csv', 'sof18.csv', 'sof18.csv', 'sof17.csv', 'sof16.csv', 'sof15.csv', 'sof14.csv', 'sof13.csv', 'sof12.csv', 'sof11.csv']
for item in lst:
    print(item)
    for root, dirs, files in os.walk('D:\\USERNAME\\project1'):
        for file in files:
            if file.endswith(item):
                df = pd.read_csv(os.path.join(root, file))
                if not df.empty:
                    print(df.describe())
                    print()
                    # or we can merge to a larger dataframe, write into a file/database(required normalization later tho) for further use

dir = "D:\\stock analysis"


def plot_DATE_(dir):
    for filename in os.listdir(dir):
        print(filename)
        if (filename.endswith(".csv")):
            fn = pd.read_csv(os.path.join(dir, filename), parse_dates=True)
            fn['Date'] = pd.to_datetime(fn['Date'])
            fn.sort_values(by=['Date'], inplace=True)
            price_date = fn['Date']
            price_close = fn['Close']
            plt.xlabel('Date')
            plt.xticks(ticks=None)

            plt.plot_date(price_date, price_close, linestyle='solid', label=filename[:-4])
            plt.legend()
            plt.show()
# problem with this is if the dates is not synchronized the xticks will be a mess
# solutions?


plot_DATE_(dir)