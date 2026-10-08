# This script can only be run with real data; it cannot be run with the synthetic
# example data provided in this repository, which is a simulated null background.

from SigProfilerTopography import Topography as topography

topography.runAnalyses(genome = "GRCh37", 
	inputDir = "LUAD_res", 
	outputDir = "LUAD_topography", 
	jobname = "LUAD_US", 
	numofSimulations = 100, 
	sbs_probabilities = "LUAD_US_optimized_decomposition/Decompose_Solution/Activities/Decomposed_MutationType_Probabilities.txt", 
	epigenomics = True, 
	nucleosome = True, 
	replication_time = True, 
	strand_bias = True, 
	replication_strand_bias = True, 
	transcription_strand_bias = True, 
	processivity = True, 
	step2_gen_sim_data = False, 
	mutation_types = ["SBS"])
