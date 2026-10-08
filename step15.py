# This script can only be run with real data; it cannot be run with the synthetic
# example data provided in this repository, which is a simulated null background.

from SigProfilerTopography import Topography as topography

topography.install_nucleosome(genome = "GRCh37")
topography.install_atac_seq(genome = "GRCh37")
topography.install_repli_seq(genome = "GRCh37")
