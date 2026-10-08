import sigProfilerPlotting as sigPlt

sigPlt.plotSBS("LUAD_res/SBS/LUAD_US.SBS288.all",
			   "LUAD_plots/",
			   "LUAD_US",
			   "288",
			   percentage = False)

sigPlt.plotID("input_example/matrices/LUAD.ID83.all",
			  "LUAD_plots/",
			  "LUAD_US",
			  "83",
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
