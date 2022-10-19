import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

# Statistical summary
print(df.describe())

# Replace All NAN values with Mean
df = df.fillna(df.mean())

# aggregating
grouped_multiple = df.groupby(['Pulse', 'Maxpulse']).agg({'Calories': ['mean', 'min', 'max','count']})
grouped_multiple.columns = ['Mean', 'Min', 'Max','Count']
grouped_multiple = grouped_multiple.reset_index()
print(grouped_multiple)

#Filter between 500 and 1000
result=df.loc[(df['Calories'] > 500) & (df['Calories'] < 1000 )]
t_result=df.loc[(df['Calories'] > 500) & (df['Pulse'] < 100)]

# create  modified dataframe with no Maxpulse column
df_modified =df.loc[:, df.columns != "Maxpulse"]
print(df_modified)

# delete a column MaxPulse
del df['Maxpulse']
print(df)

# change datatype columns to_numeric   Calories
df['Calories'] = pd.to_numeric(df['Calories'])

# Draw a scatter plot
plt.scatter(df['Duration'], df['Calories'], s=0.5,c='blue')
plt.xlabel('Duration')
plt.ylabel('Calories')
plt.show()