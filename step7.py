from SigProfilerClusters import SigProfilerClusters as sigCl

sigCl.analysis(project = "LUAD_US", 
			   genome = "GRCh37", 
			   contexts = "96", 
			   simContext = ["96"], 
			   input_path = "LUAD_res/", 
			   subClassify = True, 
			   max_cpu = 5, 
			   includedVAFs = False)
