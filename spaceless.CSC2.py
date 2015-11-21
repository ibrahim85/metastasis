print """Cancer Stem Cell with driver support Simulation
Spaceless Model
"""

from spaceless.Toys import build_CSC_reg, regular_processor
from spaceless import Post
from spaceless.Model import pDivisionFunction
import time
import matplotlib.pyplot as plt
import numpy as np
import csv

sim = build_CSC_reg(mean_mutations=1, update_mean_mutations=25, p_division_function=pDivisionFunction.sigmoid(), post_steps=1500)

# from cc3dtools.Genome import save_genomes2, get2_to_dict
# from cc3dtools.GenomeCompare import GenomeCompare


file_name = './spaceless_data/CSC_MD.'+time.ctime()

# # # genomes =  sim.get_genomes()
# # types = sim.get_types()
# # sim.sort_genomes()
# # genomes = sim.sorted_genomes
print sim.cell_stats()

vals = regular_processor(sim, subsample=100)

print vals

with open(file_name+'stats.csv', 'w') as f:
	writer = csv.writer(f)
	for val in vals:
		writer.writerow(val)


# for testing purposes
# this should show that any cell with max division of 4
# should not have the middle element larger than 4
# from collections import Counter
# print Counter(map(lambda cell: (cell.max_divisions, cell.number_of_divisions, cell.cell_type), sim.cells.values()))