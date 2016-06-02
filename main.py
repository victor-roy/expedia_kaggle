# -*- coding: utf-8 -*-
"""
Created on Sun May 29 01:33:22 2016

@author: victo
"""
from DataLoader import importData, loadChunk
import os


# Change directory
os.chdir(os.getcwd())



def main():
    # importData needs to only be run once. 
    # TODO: add check to see if importData has been run, retrieve chunk_count
    chunk_count, row_count = importData()
    
    print "chunk_count = {0}".format(chunk_count)
    print "row_count = {0}".format(row_count)

        
    
    
main()