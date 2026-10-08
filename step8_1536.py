from SigProfilerExtractor import sigpro as sig

if __name__ == "__main__":
	sig.sigProfilerExtractor(input_type = "matrix", 
							 output = "LUAD_US_extraction_1536", 
							 input_data = "LUAD_res/SBS/LUAD_US.SBS1536.all", 
							 reference_genome = "GRCh37", 
							 minimum_signatures = 1, 
							 maximum_signatures = 10, 
							 nmf_replicates = 100, 
							 cpu = 30, 
							 gpu = False)
