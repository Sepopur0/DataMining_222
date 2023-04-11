from readfile import *
from create_data import create_data
from block_process import data_process
from match import data_matcher

DATA_SETS={#'Restaurants':['restaurant1Profiles','restaurant2Profiles','restaurantsIdDuplicates'],
           'Abt-Buy':['abtProfiles','buyProfiles','abtBuyIdDuplicates'],
           'Amazon-Google Products':['amazonProfiles','gpProfiles','amazonGpIdDuplicates'],
           'DBLP-ACM':['dblpProfiles','acmProfiles','dblpAcmIdDuplicates'],
           'IMDB-TMDB':['imdbProfilesNEW','tmdbProfiles','imdbTmdbIdDuplicates'],
           'IMDB-TVDB':['imdbProfilesNEW','tvdbProfiles','imdbTvdbIdDuplicates'],
           'TMDB-TVDB':['tmdbProfiles','tvdbProfiles','tmdbTvdbIdDuplicates'],
           'Amazon-Walmart':['amazonProfiles2','walmartProfiles','amazonWalmartIdDuplicates'],
           'DBLP-Scholar':['dblpProfiles2','scholarProfiles','dblpScholarIdDuplicates']}

def inform():
    print("""The following datasets are chosen to test:""")
    count=1
    for i in list(DATA_SETS.keys()):
        filesstr=DATA_SETS[i][0]+ ', ' + DATA_SETS[i][1] + '. Groundtruth file: ' + DATA_SETS[i][2]
        print(str(count)+' '+ i + filesstr)
        count+=1
        
    print("Type the dataset id to begin test:")
    res=-1
    while True:
        try:
            inp=input()
            res=int(inp)
            if not(res in range(1,9)):
                print("Error in input. PLease try again.")
                print("Type the dataset id to begin test:")
            else:
                break
        except:
            print("Error in input. PLease try again.")
            print("Type the dataset id to begin test:")
    idx=list(DATA_SETS.keys())[res-1]
    return  'datafiles\\'+DATA_SETS[idx][0],'datafiles\\'+DATA_SETS[idx][1],'datafiles\\'+DATA_SETS[idx][2]
        
def choosekey(most1,most2):
    set1=set(most1)
    set2=set(most2)   
    return list(set1.intersection(set2))


def main():
    filePath1,filePath2,filePathgt=inform()
    #create data
    # filePath1='walmartProfiles'
    dataset1=Readfile(filePath1)
    dataframe1,most1=Dictionary_file(dataset1)
    # filePath2='amazonProfiles2'
    dataset2=Readfile(filePath2)
    dataframe2,most2=Dictionary_file(dataset2)
    
    # filePathgt='amazonWalmartIdDuplicates'
    groundtruth=ReadGtfile(filePathgt)
    gtframe=Dictionary_Gt_file(groundtruth)
    
    dataset=create_data(dataframe1,dataframe2,gtframe)
    keylst=choosekey(most1,most2)
    #process data
    processed_data=data_process(dataset)
    
    #match data
    matched_data=data_matcher(processed_data,dataset,keylst)
    # print(matched_data)
    
    
    

    
    
if __name__=="__main__":
    main()
    