from pyjedai.block_building import QGramsBlocking
from pyjedai.block_cleaning import BlockFiltering
from pyjedai.block_cleaning import BlockPurging
from pyjedai.comparison_cleaning import CardinalityEdgePruning

def buildblock(dataset,k):
    block_builder=QGramsBlocking(qgrams=3)
    return block_builder.build_blocks(dataset)

def cleanblock(builtblock,dataset):
    block_cleaner_1=BlockFiltering(ratio=0.8)
    block_cleaner_2=BlockPurging()
    cleaned_block_p=block_cleaner_1.process(builtblock,dataset)
    return block_cleaner_2.process(cleaned_block_p,dataset)

def clean_comp(cleanedblock,dataset):
    comp_cleaner=CardinalityEdgePruning('X2')
    cleaned_comp=comp_cleaner.process(cleanedblock,dataset)
    return cleaned_comp

def data_process(dataset,keylst):
    built_block=buildblock(dataset,keylst)
    cleaned_block=cleanblock(built_block,dataset)
    return clean_comp(cleaned_block,dataset)
    
    


    