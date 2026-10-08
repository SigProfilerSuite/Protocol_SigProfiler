######### Box 1: Multimodal SBS+ID de novo signature extraction
import pandas as pd

sbs = pd.read_csv("LUAD_res/SBS/LUAD_US.SBS96.all", sep = "\t", index_col = 0)
ids = pd.read_csv("input_example/matrices/LUAD.ID83.all", sep = "\t", index_col = 0)

sbs.columns = sbs.columns.str.replace(r"_\d+$", "", regex = True)

multimodal = pd.concat([sbs, ids[sbs.columns]])
multimodal.to_csv("LUAD_res/LUAD_US.SBS96_ID83.all", sep = "\t")

from SigProfilerExtractor import sigpro as sig

if __name__ == "__main__":
	sig.sigProfilerExtractor(input_type = "matrix",
							 output = "LUAD_US_extraction_multimodal",
							 input_data = "LUAD_res/LUAD_US.SBS96_ID83.all",
							 reference_genome = "GRCh37",
							 minimum_signatures = 1,
							 maximum_signatures = 10,
							 nmf_replicates = 100,
							 cpu = 30,
							 gpu = False)

	denovo = pd.read_csv("LUAD_US_extraction_multimodal/CH179/Suggested_Solution/CH179_De-Novo_Solution/Signatures/CH179_De-Novo_Signatures.txt",
						 sep = "\t", index_col = 0)

	sbs_sigs = denovo.iloc[:96]
	id_sigs = denovo.iloc[96:]

	(sbs_sigs / sbs_sigs.sum()).to_csv("multimodal_SBS96_signatures.txt", sep = "\t")
	(id_sigs / id_sigs.sum()).to_csv("multimodal_ID83_signatures.txt", sep = "\t")
