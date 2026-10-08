# This script can only be run with real data; it cannot be run with the synthetic
# example data provided in this repository, which is a simulated null background.

from SigProfilerSimulator import SigProfilerSimulator as sigSim

sigSim.SigProfilerSimulator(project = "LUAD_US", 
							project_path = "LUAD_res", 
							genome = "GRCh37", 
							contexts = ["96"], 
							simulations = 100, 
							chrom_based = True)
