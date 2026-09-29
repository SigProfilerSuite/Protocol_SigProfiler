#!/usr/bin/env bash

set -euo pipefail

conda create --name sigprofiler -y python=3.10 pip
conda run --name sigprofiler --no-capture-output pip install SigProfilerMatrixGenerator==1.3.6 SigProfilerSimulator==1.2.2 SigProfilerClusters==1.2.2 SigProfilerExtractor==1.4.1 SigProfilerAssignment==1.1.5 SigProfilerTopography==1.0.113 SigProfilerPlotting==1.4.3
