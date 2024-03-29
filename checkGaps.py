
import os
import numpy as np
import pandas as pd
from datetime import datetime

"""The function checkGaps() look for gaps in the times series and fills them with the missing dates"""

def checkGaps(File, timestep):

    # Read the file
    fileName, fileExtension = os.path.splitext(File)

    if timestep == '15 min':
        dateParser = lambda x: datetime.strptime(x, '%d-%m-%Y %H:%M:%S') # It is 4 times faster with the parser
        df = pd.read_csv(f'data/{fileName}.csv', delimiter=';', parse_dates=['Date'], date_parser=dateParser, index_col=['Date'])
        frequency = '15min'

    elif timestep == '1 day':
        dateParser = lambda x: datetime.strptime(x, '%d-%m-%Y') # It is 4 times faster with the parser
        df = pd.read_csv(f'data/{fileName}.csv', delimiter=';', parse_dates=['Date'], date_parser=dateParser, index_col=['Date'])
        frequency = 'D'

    # Remove the index duplication
    df = df.loc[~df.index.duplicated(), :]

    # Check for missing dates
    df.index = pd.to_datetime(df.index)
    missingDates = pd.date_range(start=str(df.index[0]), end=str(df.index[-1]), freq=frequency).difference(df.index)

    # Get all the whole date range
    allDates = pd.date_range(start=str(df.index[0]), end=str(df.index[-1]), freq=frequency)

    #  Insert all dates in the db
    df = df.reindex(allDates, fill_value=np.nan)
    df.index.name = 'date'
    
    # Save the db to csv
    df.to_csv(f'data/{fileName}_full.csv', sep=';', encoding='utf-8', index=True, header=[f'{fileName}'])

