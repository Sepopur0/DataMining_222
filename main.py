from readfile import *
from create_data import create_data
from block_process import data_process
from match import data_matcher
def main():
    #create data
    filePath1='walmartProfiles'
    dataset1=Readfile(filePath1)
    dataframe1=Dictionary_file(dataset1)
    
    filePath2='amazonProfiles2'
    dataset2=Readfile(filePath2)
    dataframe2=Dictionary_file(dataset2)
    
    filePathgt='amazonWalmartIdDuplicates'
    groundtruth=ReadGtfile(filePathgt)
    gtframe=Dictionary_Gt_file(groundtruth)
    
    dataset=create_data(dataframe1,dataframe2,gtframe)
    
    #process data
    processed_data=data_process(dataset)
    
    #match data
    matched_data=data_matcher(processed_data,dataset,list(dataframe1.keys()).remove('id'))
    
    
    

    
    
if __name__=="__main__":
    main()
    