from pandas import DataFrame
from pyjedai.datamodel import Data
def create_data(profiles1:dict,profiles2:dict,gt=None):
    dataset1=DataFrame(profiles1)
    dataset2=DataFrame(profiles2)
    if gt is None:
        return Data(dataset_1=dataset1,attributes_1=profiles1.keys(),id_column_name_1='id',dataset_2=dataset2,attributes_2=profiles2.keys(),id_column_name_2='id')
        
    else:
        gt=DataFrame(gt)
        data= Data(dataset_1=dataset1,attributes_1=profiles1.keys(),id_column_name_1='id',dataset_2=dataset2,attributes_2=profiles2.keys(),id_column_name_2='id',ground_truth=gt)
        data.process()
        return data
