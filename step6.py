from SigProfilerSimulator import SigProfilerSimulator as sigSim

sigSim.SigProfilerSimulator(project = "LUAD_US", 
							project_path = "LUAD_res", 
							genome = "GRCh37", 
							contexts = ["96"], 
							simulations = 100, 
							chrom_based = True,
							exome = False)
