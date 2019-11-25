

import networkx as nx
from graphs_parser import loadGXL
from grec_cost_functions import *
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Graph Edit Distance')
    parser.add_argument('--g1', type=str, help='source graph')
    parser.add_argument('--g2', type=str, help='target graph')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    if(args.g1 is None or args.g2 is None):
        print("g1 or g2 is not initialized")
    else:
        GREC = GRECCostFunctions()
        g1 = loadGXL(args.g1)
        g2 = loadGXL(args.g2)

        # if you want to only output the distance, you can use the graph_edit_distance as follows:

        distance  = nx.graph_edit_distance(g1, g2, node_subst_cost=GREC.node_substitution_cost,
                               node_del_cost=GREC.node_deletion_cost,
                               node_ins_cost=GREC.node_insertion_cost
                               , edge_subst_cost=GREC.edge_substitution_cost,
                               edge_del_cost=GREC.edge_deletion_cost,
                               edge_ins_cost=GREC.node_insertion_cost)

        print("optimal distance :::", distance)

        # if you want to output the distance and all the possible optimal pathz, you can use the optimal_edit_paths function

        paths, cost = nx.optimal_edit_paths(g1, g2, node_subst_cost=GREC.node_substitution_cost,
                               node_del_cost=GREC.node_deletion_cost,
                               node_ins_cost=GREC.node_insertion_cost
                               , edge_subst_cost=GREC.edge_substitution_cost,
                               edge_del_cost=GREC.edge_deletion_cost,
                               edge_ins_cost=GREC.node_insertion_cost)

        print("the possible paths are: ", paths)
        print("distance: ", distance)

