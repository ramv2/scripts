from igraph import *
import numpy as np

class graph_thingy:
    def __init__(self, c_boxes):
        # Create fully connected graph
        self.g = Graph.Full(c_boxes.shape[0], True, False)

    def edge_features(self, v1, v2):
        return 0

    def edge_labels(self, model):
        edge_list = self.g.es
        vertex_list = self.g.vs
        features = []

        for e in edge_list:
            v1 = vertex_list[e.source]
            v2 = vertex_list[e.target]
            features.append(self.edge_features(v1, v2))
        edge_list["label"] = model.predict(features)

        delete_list = []
        for i in xrange(0, len(edge_list)):
            if (not edge_list["label"][i]):
                delete_list.append(edge_list[i])

        # delete edges that are marked for deletion
        self.g.delete_edges(delete_list)

        # print len(edge_list), len(vertex_list)
        # for e in edge_list:
        #     print e.tuple
        #
        # for v in vertex_list:
        #     print v.index
        return 0

def main():
    print "yay"

if __name__ == "__main__":
    a = np.ones((3,1))
    x = graph_thingy(a)
    x.edge_labels(a)