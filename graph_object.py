from igraph import *
import numpy as np

class graph_object:
    def __init__(self, c_boxes):
        try:
            # Create fully connected undirected graph without loops
            self.g = Graph.Full(c_boxes.shape[0], False, False)
        except AttributeError:
            print "Argument c_boxes should be a 2-D numpy array with " \
                  "shape as an attribute."

    def edge_features(self, v1, v2):
        return 0

    def edge_labels(self, model):
        edges = self.g.es
        vertices = self.g.vs
        features = []

        for e in edges:
            v1 = vertices[e.source]
            v2 = vertices[e.target]
            features.append(self.edge_features(v1, v2))
        edges["label"] = model.predict(features)

        delete_index = []
        for i in xrange(0, len(edges)):
            if (not edges["label"][i]):
                delete_index.append(i)

        # delete edges that are marked for deletion
        self.g.delete_edges(delete_index)

        # print len(edges), len(vertices)
        # for e in edges:
        #     print e.tuple
        #
        # for v in vertices:
        #     print v.index
        return 0

def main():
    print "yay"

if __name__ == "__main__":
    a = np.ones((3,1))
    x = graph_object(a)
    x.edge_labels(a)