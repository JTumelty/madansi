import networkx as nx
from madansi.JoiningContigComponents import JoiningContigComponents

class IterateJoiningContigComponents(object):
    
    def __init__(self, unrefined_graph):
        self.temp_graph = nx.Graph()
        self.unrefined_graph = unrefined_graph
        
    
    def iterate_joining(self, ordered_contig_graph):
        join_components         = JoiningContigComponents(ordered_contig_graph, self.unrefined_graph)
        ordered_contig_graph    = join_components.add_edges()
        while not nx.is_isomorphic(self.temp_graph, ordered_contig_graph):
            self.temp_graph         = ordered_contig_graph
            join_components         = JoiningContigComponents(ordered_contig_graph, self.unrefined_graph)
            ordered_contig_graph    = join_components.add_edges()
        return ordered_contig_graph
    

        