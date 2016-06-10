    # -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:24:59 2016

@author: victo
"""
import numpy as np
import pandas as pd
import os
import time

os.chdir(os.getcwd())

def importData():
    
    start_time = time.time()        
    
    print "Importing data from train.csv..."    
    
    
    dtype_dict = {'date_time':np.datetime64, 
                   'site_name': np.int32, 
                   'posa_continent':np.int32, 
                   'user_location_country':np.int32, 
                   'user_location_region':np.int32, 
                   'user_location_city':np.int32, 
                   'orig_destination_distance':np.float64, 
                   'user_id':np.int32, 
                   'is_mobile':np.bool_, 
                   'is_package':np.bool_, 
                   'channel':np.int32, 
                   'srch_ci':np.datetime64, 
                   'srch_co':np.datetime64, 
                   'srch_adults_cnt':np.int32, 
                   'srch_children_cnt':np.int32, 
                   'srch_rm_cnt':np.int32, 
                   'srch_destination_id':np.int32,
                   'srch_destination_type_id':np.int32,
                   'hotel_continent':np.int32, 
                   'hotel_country':np.int32, 
                   'hotel_market':np.int32, 
                   'is_booking':np.bool_, 
                   'cnt':np.int64, 
                   'hotel_cluster':np.int32}
                    
    # Import csv with chunk_size = 5,000,000   
    # TODO: move chunk_size to config
    n_rows = 2500000

    train = pd.read_csv('train.csv', dtype=dtype_dict, parse_dates= ['date_time', 'srch_ci','srch_co'], nrows=n_rows)
    
    cat_vars = ['site_name','posa_continent','user_location_country', 'user_location_region', 'user_location_city', 'is_mobile', 'is_package', 'channel', 'srch_destination_type_id', 'hotel_continent', 'hotel_country', 'hotel_market', 'hotel_cluster']
    ordered_cat_vars = ['srch_adults_cnt', 'srch_children_cnt', 'srch_rm_cnt', 'is_booking']
    
    for i in cat_vars:
        train[i] = train[i].astype("category", ordered=False)
    for i in ordered_cat_vars:
        train[i] = train[i].astype("category", ordered=True)
    
    
    end_time = time.time()
    
    duration = end_time-start_time
    
    print "Time to import {0} rows in {1} seconds".format(n_rows, duration)
    
    return train
    
    
def featureEngineering(train):
    # Number of days searching in advance of check-in
    train['days_advance'] = pd.to_datetime(train['srch_ci'], errors='coerce') - pd.to_datetime(train['date_time'],errors='coerce')
    
    # Number of nights of stay searched for, round to day.
    train['num_nights'] = pd.to_datetime(train['srch_co'], errors = 'coerce')-pd.to_datetime(train['srch_ci'], errors = 'coerce')
    train['num_nights'] = train['num_nights'].astype('category',ordered = False)
    
    # Day of week; 0=Monday, 6=Sunday
    train['day_of_week'] = pd.to_datetime(train['date_time'], errors='coerce').dt.dayofweek
    train['day_of_week'] = train['day_of_week'].astype('category', ordered = False)

    # Month in which search-check-in day resides; 0 for January, 11 for December
    train['srch_ci_month'] = pd.to_datetime(train['srch_ci'], errors='coerce').dt.month
    train['serch_ci_month'] = train['srch_ci_month'].astype('category', ordered = False)

    # True for winter/summer; False for autumn/spring    
    # Winter/Summer counts as [1,2,12,11,6,7,8,9], where 1 = Jan; 12 = Dec
    train['season'] = train['srch_ci_month'].map(lambda x: x in [1,2,12,11,6,7,8])
    
    
    return train
    

def main():
    
    # Store a quick pickle for ease of testing in console
    #train = importData()
    train = pd.read_pickle('train.pickle')
    
    train = featureEngineering(train)
    
    train.to_pickle('train.pickle')
   

main()
    
    
    
   
        
