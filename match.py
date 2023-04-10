from pyjedai.matching import EntityMatching
from pyjedai.clustering import ConnectedComponentsClustering
from pyjedai.evaluation import Evaluation, write
import networkx
from networkx import draw, Graph
def data_matcher(blocks,dataset,keys):
    matcher=EntityMatching(attributes=keys,similarity_threshold=0.5)
    cluster=ConnectedComponentsClustering()
    res=cluster.process(matcher.predict(blocks,dataset,True))
    # cluster.report()
    # Evaluation(dataset).report(res)
    return res