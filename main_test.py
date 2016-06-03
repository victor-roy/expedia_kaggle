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
    
    
    dtype_dict = {'date_time':str, 
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
                   'srch_ci':str, 
                   'srch_co':str, 
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
    
    end_time = time.time()
    
    duration = end_time-start_time
    
    print "Time to import {0} rows in {1} seconds".format(n_rows, duration)
    
    return train
    
    
def featureEngineering(train):
     
     
    # Calc # nights
    num_nights = train['srch_co']-train['srch_ci']
    num_nights = (num_nights/np.timedelta64(1,'D')).astype(float)
    train['num_nights'] = num_nights
    
    # Calc # days searching in advance
    days_advance = (train['srch_ci']-train['date_time'])/np.timedelta64(1,'D')
    train['days_advance'] = days_advance
    
# unfinished
def calcPopular(train):
    train.groupby(('srch_destination_id','is_booking'))    
    
    

def main():
    
    train = importData()
    
    train = featureEngineering(train)

    #most_popular = calcPopular(train)     
    
    
    
    
   
        
