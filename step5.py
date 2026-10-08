######### Genome version installation
from SigProfilerMatrixGenerator import install as genInstall
genInstall.install(genome = 'GRCh37')

######### Matrix generation
from SigProfilerMatrixGenerator.scripts import SigProfilerMatrixGeneratorFunc as matGen
matGen.SigProfilerMatrixGeneratorFunc(project = "LUAD_US", 
									  reference_genome = "GRCh37", 
									  path_to_input_files = "input_example/somatic_mutation", 
									  output_directory = "LUAD_res")
