# -*- coding: utf-8 -*-
"""
Created on Sat May 28 22:10:26 2016

@author: victo
"""

import numpy as np
import pandas as pd
import os
import time
import pickle

os.chdir(os.getcwd())   #change directory to current working directory

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
    chunk_size = 2500000

    train = pd.read_csv('train.csv', dtype=dtype_dict, parse_dates= ['date_time', 'srch_ci','srch_co'], chunksize=chunk_size)

    row_count = 0
    chunk_count = 0
    for chunk in train: 
        chunk_count += 1
        row_count += int(chunk.shape[0])
        file_name = "train_chunk_"+str(chunk_count)+".pickle"
        f = open(file_name,'wb')
        pickle.dump(chunk, f)
        f.close()

        
    end_time = time.time()
    duration = (end_time-start_time)   
        
    print "Time to import {0} rows in {2} chunks: {1} seconds".format(row_count, duration, chunk_count)
    return chunk_count, row_count
    
def loadChunk(chunk_num):
    file_name = "train_chunk_"+str(chunk_num)+".pickle"
    f = open(file_name,'rb')
    train = pickle.load(f)
    f.close()
    
    return train
    
def saveChunk(chunk, chunk_num):
    file_name = 'train_chunk_'+str(chunk_num)+".pickle"
    f = open(file_name, 'wb')
    pickle.dump(chunk, file_name)
    f.close()
    
    return
