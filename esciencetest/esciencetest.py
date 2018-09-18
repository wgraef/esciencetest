# -*- coding: utf-8 -*-
"""Documentation about the eScienceTest module."""
def hithere():
    print('hi')

def dovoro(dim_x, dim_y, cells):
#    import matplotlib
#    import matplotlib.pyplot as plt
    import pyvoro
    import numpy as np

    dots_num = cells
    vol = dim_x * dim_y
    colors = np.random.rand(dots_num, 3) # or predefined 
  
    dots = np.random.rand(dots_num, 2)
    # make color map (unnecessary for just random colorization)
    color_map = {tuple(coords):color for coords, color in zip(dots, colors)}

    cells = pyvoro.compute_2d_voronoi(
        dots, # point positions, 2D vectors this time.
        [[0.0, dim_x], [0.0, dim_y]], # box size
        2.0 # block size
    )
    
    # colorize

    vol_sum = 0.0
    cell_count = 0
    for i, cell in enumerate(cells):
        vol_sum += cell['volume']
        cell_count += 1
        print(i, cell['volume'])
#        polygon = cell['vertices']
#        plt.fill(*zip(*polygon), color = color_map[tuple(cell['original'])], alpha=0.5)
    
#    plt.plot(dots[:,0], dots[:,1], 'ko')
#    plt.xlim(-0.1, 1.1)
#    plt.ylim(-0.1, 1.1)
#    
#    plt.show()
    return (cell_count, vol_sum)
