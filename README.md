# Protocol_SigProfiler

Runnable example for **"Profiling signatures of mutational processes using the SigProfiler suite"**
(Nature Protocols).

The protocol is demonstrated in the paper on 37 lung adenocarcinomas from the PCAWG cohort. Those
mutation calls are not public, so this repository ships a **synthetic dataset** derived from them,
together with the scripts for every step of the protocol and the output they produce. The point is to
let you run the workflow end to end, check that your installation behaves, and compare your output
with ours — without applying for data access first.

## The synthetic dataset

`input_example/somatic_mutation/LUAD_sim_data.maf` holds 1,338,192 single-base substitutions across
37 samples.

It was produced with SigProfilerSimulator from the original tumours, simulating in the SBS-6144
context. **The simulator randomises the genomic position of every mutation** while preserving its
mutational profile. Two consequences, and they matter:

- **The mutational matrices are preserved.** The SBS-96 and SBS-1536 matrices derived from this
  dataset are identical to those of the original tumours; SBS-288 differs by 6 mutations out of
  1,338,192. Signature extraction, decomposition and assignment therefore reproduce the published
  results.
- **The spatial distribution is destroyed.** The dataset *is* a simulated null background, so it
  cannot demonstrate any method that looks at where mutations fall in the genome. That rules out
  clustered-mutation detection (SigProfilerClusters) and topographical analysis
  (SigProfilerTopography).

The MAF contains substitutions only. The ID-83, DBS-78, CNV-48 and SV-32 matrices used for plotting
are supplied ready-made in `input_example/matrices/`, and `input_example/refitting/` holds a small
SBS-96 matrix for two samples used by the refitting step.

## Requirements

- Linux or macOS, with [Conda](https://conda.io) or Mamba
- ~30 CPU cores. The extraction steps are the reason this is not a laptop workload
- ~15 GB of free disk: the GRCh37 reference installed by `step5.py` takes ~6 GB inside the
  environment, and the outputs take a few GB more
- Network access on the first run, to download the reference genome and the COSMIC catalogue

## Installing the environment

```bash
./setup.sh
```

That creates a Conda environment named `sigprofiler` with Python 3.10 and installs the seven
SigProfiler packages at the versions the paper was written against:

| Package | Version |
|---|---|
| SigProfilerMatrixGenerator | 1.3.6 |
| SigProfilerSimulator | 1.2.2 |
| SigProfilerClusters | 1.2.2 |
| SigProfilerExtractor | 1.4.1 |
| SigProfilerAssignment | 1.1.5 |
| SigProfilerTopography | 1.0.113 |
| SigProfilerPlotting | 1.4.3 |

## Running the example

```bash
./run_example.sh
```

Run it from anywhere: the script changes into the repository root itself. It executes every step
through `conda run`, so the environment does not need to be activated and it works from a batch job
on a cluster. It stops at the first error.

These are the steps it runs — the ones the synthetic data support:

| Step | Script | What it does |
|---|---|---|
| 5 | `step5.py` | install GRCh37 and generate the mutational matrices |
| 8 | `step8_288.py`, `step8_1536.py` | de novo extraction, SBS-288 and SBS-1536 |
| 10 | `step10.py` | decomposition into COSMIC reference signatures |
| 11 | `step11.py` | decomposition excluding signature subgroups |
| 12 | `step12.py` | assignment of the de novo signatures to samples |
| 13 | `step13.py` | refitting the full COSMIC catalogue to two samples |
| 14 | `step14.py` | assignment of signatures to individual mutations |
| 17 | `step17.py` | SBS, ID, DBS, CN and SV profile plots |

To run a single step instead:

```bash
conda run --name sigprofiler --no-capture-output python step5.py
```

Scripts use paths relative to the repository root, so run them from there.

`Box1.py` is an optional extra: the multimodal SBS+ID extraction described in Box 1 of the paper. It
needs `step5.py` to have run first, and it is not part of `run_example.sh` because it adds a second
full extraction.

### Steps that are not run

`step6.py`, `step7.py`, `step15.py` and `step16.py` are included for reference and `run_example.sh`
does not call them. SigProfilerClusters and SigProfilerTopography both compare the observed genomic
distribution of mutations against a simulated null background, and this dataset *is* that background:
there is no clustering to detect and no departure from the background to measure. These branches need
real somatic mutation data that retains its native spatial distribution.

## What the run produces

Every directory below is created by the run and is excluded from version control.

```
LUAD_res/                                   step5   mutational matrices + GRCh37 install
LUAD_US_extraction_288/                     step8   de novo extraction, SBS-288
LUAD_US_extraction_1536/                    step8   de novo extraction, SBS-1536
LUAD_US_decomposition/                      step10  decomposition into COSMIC signatures
LUAD_US_optimized_decomposition/            step11  decomposition excluding subgroups
LUAD_de_novo_decomposition/                 step12  de novo signatures assigned to samples
LUAD_cosmic_refitting/                      step13  COSMIC catalogue refitted to 2 samples
LUAD_decomposed_assignment_to_mutations/    step14  per-mutation signature probabilities
LUAD_plots/                                 step17  mutational profile plots
```

`step14.py` also creates `input_example/somatic_mutation/input/` and
`input_example/somatic_mutation/output/`. These are intermediate files, not results.

Reference results are archived in `expected_output.zip`.

## Comparing your results with the archived output

De novo extraction uses stochastic NMF optimisation, so exact values will not reproduce. Signature
counts, extracted profiles and assigned exposures should be very close; signature labels, their
order, per-signature stability scores and the last decimal places of the activities will differ
between runs. Treat a different *number* of selected signatures as a result worth investigating, and
small numerical differences as expected.

## Troubleshooting

**`conda: command not found`** — Conda is not on `PATH`. Install Miniconda, or load the module that
provides it on your cluster.

**A step cannot find its input** — the scripts use relative paths. Run them from the repository root,
or use `run_example.sh`, which changes into it.

**Results differ from `expected_output.zip`** — see *Comparing your results with the archived
output*. Check the package versions first: different SigProfiler releases default to different
COSMIC catalogue versions.

**A rerun behaves differently from the first run** — delete the generated directories listed under
*What the run produces*, including `input_example/somatic_mutation/input/` and
`input_example/somatic_mutation/output/`.
