data = {
    'shoes':['red', 'purple', 'red', 'purple', 'red', 'red', 'red'],
    'hats': ['blue', 'blue', 'blue', 'white', 'white', 'blue', 'blue']
}

data

import pandas as pd

store = pd.DataFrame (data)
store

store = pd.DataFrame (data, index=['Jay', 'Mary', 'Bill', 'Chris', 'Martha', 'Karen', 'Rob'])
store

myDF = pd.read_csv("/anvil/projects/tdm/data/death_records/DeathRecords.csv")

myDF.head()

pd.options.display.max_columns = None
myDF.head()

myDF.iloc[10,]

myDF.tail()

myDF.shape

# There are 2631171 rows, 38 columns in the entire dataframe


myDF.columns

[print(x) for x in myDF.columns ]

len(myDF['Age'][myDF['Age']>52])

# 2325365 people over age 52 are represented in the death record

myDF['Sex'].value_counts()

# M    1331461
# F    1299710
# Name: Sex, dtype: int64


myDF['Age'].value_counts()

len(myDF['Age'][(myDF['Age']>52) & (myDF['Sex'] == 'F')])

len(myDF['Age'][(myDF['Age']>70) & (myDF['Sex'] == 'F')])

len(myDF['Age'][(myDF['Age']>70) & (myDF['Sex'] == 'M')])

len(myDF['Age'][myDF['Age']>70])


915750 + 738600

import matplotlib.pyplot as plt

myDF['Sex'].value_counts()

mygender = myDF['Sex'].value_counts()

plt.bar(mygender.index, mygender)

myDF['Age'].value_counts()

mydata = myDF['Age'].value_counts()

plt.bar(mydata.index, mydata)


max(myDF['Age'])

mydata = myDF['Age'][myDF['Age']<999].value_counts()

max(myDF['Age'][myDF['Age']<999])

plt.bar(mydata.index, mydata)

myDF['MaritalStatus'].value_counts()

mydata = myDF['MaritalStatus'].value_counts()

plt.bar(mydata.index, mydata)

myDF['Autopsy'].value_counts()

mydata = myDF['Autopsy'].value_counts()

plt.bar(mydata.index, mydata)

myDF['MethodOfDisposition'].value_counts()

mydata = myDF['MethodOfDisposition'].value_counts()

plt.bar(mydata.index, mydata)