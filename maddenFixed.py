#Veeru Senthil
import pandas as pd
import numpy


madden= pd.read_csv('madden22.csv')

df = pd.DataFrame(madden)

user = input('Enter a column from the dataset: ')

#print(df[user])
counts = df['Team'].value_counts()
#print(counts)

# function to output freq table
def frequency_tables(df, col):
    """
    input: dataframe, categorical column;
    output: freq table
    """

    # check that col is categorical


    freq = df[col].value_counts()

    return freq

print()
if (pd.api.types.is_numeric_dtype(df[user].dtype) ):
    print("You picked a numeric column")
    print('Time to find a 5 number summary of the column')
    print()

    mean = numpy.mean(df[user])
    Minimum =  numpy.min(df[user])
    Q1 = numpy.quantile(0.25)(df[user])
    Q2 = numpy.quantile(0.50)(df[user])
    Q3 = numpy.quantile(0.75)(df[user])
    Max = numpy.max(df[user])


    print('Mean: ' + str(mean) )
    print('Minimum ' +  str(Minimum))
    print('Q1: ' + str(Q1))
    print('Median (Q2):' + str(Q2))
    print('Q3: ' + str(Q3))
    print('Maximum ' +  str((Max)))
else: 
    print("You picked a categorical column")
    print('Time to create a frequency table for the data')
    frequency_tables(df, df[user])



    