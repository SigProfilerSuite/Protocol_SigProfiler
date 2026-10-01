import sigProfilerPlotting as sigPlt

sigPlt.plotSBS("LUAD_res/SBS/LUAD_US.SBS96.all",
			   "LUAD_plots/",
			   "LUAD_US",
			   "96",
			   percentage = False)

sigPlt.plotSBS("LUAD_res/SBS/LUAD_US.SBS288.all",
			   "LUAD_plots/",
			   "LUAD_US",
			   "288",
			   percentage = False)

sigPlt.plotDBS("input_example/matrices/LUAD.DBS78.all",
			   "LUAD_plots/",
			   "LUAD_US",
			   "78",
			   percentage = False)

sigPlt.plotCNV("input_example/matrices/LUAD.CNV48.matrix.tsv",
			   "LUAD_plots/",
			   "LUAD_US",
			   percentage = False)

sigPlt.plotSV("input_example/matrices/LUAD.SV32.matrix.tsv",
			  "LUAD_plots/",
			  "LUAD_US",
			  percentage = False)
