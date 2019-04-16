import numpy as np
import random
from graph_tool.all import *

'''
  0 new_black_nodes, 1 black_nodes_excluding_block, 2 cumulative_black_nodes, 3 len(total_number_nodes), 4 black_node_length, 5 number_clean_tx_in_block,
  6 number_black_tx_in_block, 7 number_tx_in_block, 8 volume_clean_tx_block, 9 volume_black_tx_in_block, 10 volume_tx_in_block, 11 number_nodes_clean,
  12 len(all_black_nodes), 13 len(all_nodes), 14 volume_total, 15volume_black
'''

data=np.load('/Users/macbook/Desktop/FYP/heur1-V4400000.npy')

print(int(float(data[400000][3])))

g = Graph()
v=[g.add_vertex() for i in range(0,int(float(data[400000][3])))]

print(len(v))

paint_black = random.sample([i for i in range(0, int(float(data[400000][3])))], int(float(data[400000][4])))

e_prop = g.new_vertex_property("vector<float>")
for i in paint_black:
    e_prop[v[i]]= [0,0,0,0]


graph_draw(g, vertex_font_size=10, vertex_fill_color = e_prop, fit_view=1, output_size=(6000, 6000), output="/Users/macbook/Desktop/FYP/charts/paint_nodes_black.png")
