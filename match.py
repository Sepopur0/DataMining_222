from pyjedai.matching import EntityMatching
from pyjedai.clustering import ConnectedComponentsClustering
from pyjedai.evaluation import Evaluation, write
from networkx import draw, Graph
def data_matcher(blocks,dataset,keys):
    matcher=EntityMatching(metric='levenshtein',attributes=keys,similarity_threshold=0.5)
    cluster=ConnectedComponentsClustering()
    matched=matcher.predict(blocks,dataset,True)
    Evaluation(dataset).report(matched)
    res=cluster.process(matched)
    cluster.report()
    Evaluation(dataset).report(res)
    return res