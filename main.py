from data_structure.graph import Graph as GRAPH
from web_parsers.href_parser import HrefParserThreadBoosted
from pyvis.network import Network

link = 'https://facebook.com'

graph = GRAPH()
network = Network(height='100%', width='100%', bgcolor='#000000', font_color='white')

threaded_parser = HrefParserThreadBoosted(threads=5, max_links=100)
threaded_parser.driver(link)

graph.add_nodes(threaded_parser.links)
graph.add_edges(threaded_parser.edges)

network.barnes_hut()
network.add_nodes(graph.get_all_nodes)
network.add_edges(graph.get_all_edges)

network.show(f'foo.html')
