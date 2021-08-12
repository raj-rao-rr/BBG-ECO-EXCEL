#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 16:39:02 2021

@author: Rajesh Rao

This script works to format economic release data from Bloomberg, as stored
in an excel file. Note, API users need not worry about this. 
"""

##########################################################################
# PACKAGE IMPORTS
##########################################################################

import time
import numpy as np
import pandas as pd 


# %% Economic Data Numeric Conversion

print('\nParsing Bloomberg Economic Data file...\n')
start = time.time()

# create excel object to determine number of excel sheets and read sequentially
xl = pd.ExcelFile('Input/ECO_RELEASES.xlsx')
res = xl.sheet_names

# initialize memory for variable storage
concat_list = []

# iterate through each of the excel sheets, concat dataframes
for pg in range(len(res)):
    
    # read dataframe from economic release sheet
    df = pd.read_excel('ECO_RELEASES.xlsx', sheet_name=pg)
    
    # construct proper database from each sheet
    export_df = df.iloc[5:]
    export_df.columns = df.iloc[4]
    
    # remove all NaNs present within the Release Date
    export_df = export_df[~np.isnat(pd.to_datetime(export_df.RELEASE_DATE))]
    
    # add names and corresponding TICKERS
    n = export_df.shape[0]
    export_df['TICKER'] = [res[pg]] * n
    export_df['NAME'] = [df.iloc[0].iloc[1]] * n
    
    concat_list.append(export_df)

# concat all of the dataframes (all macroeconomic event)
concat_pd = pd.concat(concat_list)

# back-propagate the bloomberg relevancy indicator (measure on follow activity)
concat_pd['RELEVANCE_VALUE'] = concat_pd['RELEVANCE_VALUE'].fillna(method='bfill')

concat_pd = concat_pd.sort_values(by='RELEASE_DATE')
concat_pd = concat_pd[['RELEASE_DATE', 'TICKER', 'NAME', 'ACTUAL_RELEASE', 'ECO_RELEASE_DT', 
                       'BN_SURVEY_MEDIAN', 'BN_SURVEY_AVERAGE', 'BN_SURVEY_HIGH','BN_SURVEY_LOW',
                       'FORECAST_STANDARD_DEVIATION', 'BN_SURVEY_NUMBER_OBSERVATIONS', 
                       'RELEVANCE_VALUE']]

# replace values where the forecast standard deviation is zero with NaNto avoid zero division error 
concat_pd['FORECAST_STANDARD_DEVIATION'] = concat_pd['FORECAST_STANDARD_DEVIATION'].replace({
        0:np.nan})

# construct economic forecast surprises and z-score measures
concat_pd['SURPRISES'] = concat_pd['ACTUAL_RELEASE'] - concat_pd['BN_SURVEY_MEDIAN']
concat_pd['ZSCORE'] = concat_pd['SURPRISES'] / concat_pd['FORECAST_STANDARD_DEVIATION']

# ----------------------------------------------------------------------
# remove duplicates that exist for specific releases (data-release lag) 
# e.g.
#    12/04/13 | New Home Sales | Sep | 425k
#    12/04/13 | New Home Sales | Oct | 429k
# ----------------------------------------------------------------------
# we do not preserve any duplicates instead drop all duplicate rows
concat_pd = concat_pd.drop_duplicates(subset=['RELEASE_DATE', 'TICKER'], keep=False)


# %% Export Files locally to folder

print('\Cleaned Bloomberg Economic Data completed\n')
print('\t\tTime Taken: %.2f minutes' % ((time.time() - start) / 60))
concat_pd.to_csv('Output/bloomberg_economic_releases.csv', index=False)

