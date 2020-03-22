import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer

# to read in the data

# to read csv
# other readable format might which requires another library/dependency
# for excel (.xls) use pd.read_excel()
# useful parameters
# names = ['col1', 'col2'] for beffer performance
# dtype to specify dtype will improve performance eg. df object takes longest time to load, or use int32 whenever possible instead of default int64 etc


df = pd.read_csv('your_csv_file.csv')

# some basic explanatory data analysis

# df.describe() will be always useful and tend to works well with pivot table
df.describe()
df.head()
df.tail('some integers')
# head and tail returns dataframe thus can follow up with some operations
# sort_values is not inplace...
df.head(10).sort_values(by='Height', ascending=False)
# or
df.sort_values(by="Revenue (Millions)", ascending=False).head(10)
# view unique values
df['Genre'].unique()
# for list eg. [['Action, Sci-fi, Adventure'],['Drama, Comedy']](take note the ''), no better solution currently
gen_lst = []
for i in range(len(df)):
    sub_lst = df['Genre'][i].split(',')
    for j in sub_lst:
        if j not in gen_lst:
            gen_lst.append(j)
print(gen_lst, '\n', len(gen_lst))

# to make string within list into list of strings within list, ikr...
# imdb dataset
gen = [each.split(',') for each in df['Genre']]
mlb_genre = pd.DataFrame(gen)
mlb = MultiLabelBinarizer()
res = pd.DataFrame(mlb.fit_transform(mlb_genre), columns=mlb.classes_)
genre_onehot = pd.DataFrame(res, columns=mlb.classes_)
new_df = pd.merge(df['Title'], genre_onehot, left_index=True, right_index=True)
print(new_df)

# plot horizontal bar for each class
gen = [each.split(',') for each in df['Genre']]
x = [new_df[each].sum() for each in gen_lst]
new_dict = {gen: cnt for gen, cnt in zip(gen_lst, x)}
n = [[k, v] for k, v in sorted(new_dict.items(), key=lambda k: k[1])]
genre = [each[0] for each in n]
count = [each[1] for each in n]
plt.barh(genre, count)
plt.title('Genre list')
plt.xlabel('cumulative list')
plt.tight_layout()
plt.show()


# quick function to enable printing entire dataframe


def display_all(df):
    with pd.option_context('display.max_rows', 1000):
        # max rows will show first 5 and last 5 in this case
        with pd.option_context('display.max_columns', 1000):
            print(df)


# pin point certain value
df.loc['row_index', 'col_index']

# resetting index
df.reset_index(drop=True)
# or manual reindex
df.reindex(range(100), method='ffill')
df.reindex(column=list())

# dropping columns and rows
df.drop(['col_name', 'col_name'], axis=1)
df.drop(['index', 'index'])

# replacing some value to nan
# always remember to put inplace to true
df['Alcohol'].replace(['*'], np.nan, inplace=True)

# dealing with NA values
# often requires to replace value to np.nan and drop or deal with it through various approaches
# one of the easiest approach it to  directly replace to mean/median etc.
df.dropna()
df.fillna(value=df['Age'].median(), inplace=True)

# list df is a way to get all columns
col = list(df)
for item in col:
    print(item, df[item].isna().sum())
# print out each column and sum of na values
index_ = df.index[df['col_name'].isna()]
df['Title'].loc[index_]

# filtering
df[df['Gender'] == 'Male'].head(30)
df[df['Alcohol'] > 14]
df[df['Genre'].str.contains('Comedy')]
df.index[df['animal'].str.contains('ro') == True].tolist()
# or for same result
df[df['animal'].str.contains('ro')].index

# groupby
# important to note groupby returns a dataframegroupby object
# requires to apply some function to enable
df.groupby(['col1']).sum()

# difference between below two examples
# sum only Count column
df.groupby('Director')['Count'].sum()
# sum all possible columns, eg rank year, runtime, rating...
df.groupby('Director').sum()
