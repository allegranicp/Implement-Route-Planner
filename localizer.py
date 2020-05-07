# import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    normalized_new_belief = []
    row_non_normalized = []
    row_normalized = []
    total_probability = 0.0
    
    
    for i in range(len(grid)):
        for j in range(len(grid)):
            hit = (grid[i][j] == color)
            non_normalized_belief = beliefs[i][j] * (hit * p_hit + (1-hit) * p_miss)
            total_probability = total_probability + non_normalized_belief
            row_non_normalized.append(non_normalized_belief)
        new_beliefs.append(row_non_normalized) 
        row_non_normalized = []
      
    
    for k in range(len(new_beliefs)):
        for l in range(len(new_beliefs[0])):
            row_normalized.append(new_beliefs[k][l]/total_probability)
        normalized_new_belief.append(row_normalized)
        row_normalized = []
             

    return normalized_new_belief

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % width
            new_j = (j + dx ) % height
            # pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)