import sigProfilerPlotting as sigPlt

sigPlt.plotSBS(matrix_path = "LUAD_res/SBS/LUAD_US.SBS288.all",
			   output_path = "LUAD_plots/",
			   project = "LUAD_US",
			   plot_type = "288",
			   percentage = False)

sigPlt.plotID(matrix_path = "input_example/matrices/LUAD.ID83.all",
			  output_path = "LUAD_plots/",
			  project = "LUAD_US",
			  plot_type = "83",
			  percentage = False)

sigPlt.plotDBS(matrix_path = "input_example/matrices/LUAD.DBS78.all",
			   output_path = "LUAD_plots/",
			   project = "LUAD_US",
			   plot_type = "78",
			   percentage = False)

sigPlt.plotCNV(matrix_path = "input_example/matrices/LUAD.CNV48.matrix.tsv",
			   output_path = "LUAD_plots/",
			   project = "LUAD_US",
			   percentage = False)

sigPlt.plotSV(matrix_path = "input_example/matrices/LUAD.SV32.matrix.tsv",
			  output_path = "LUAD_plots/",
			  project = "LUAD_US",
			  percentage = False)
