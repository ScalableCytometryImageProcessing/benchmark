# SCIP benchmarking

Repo containing code for benchmarking SCIP performance on a PBS-TORQUE cluster.

# Usage

The benchmarking is executed using [atools](https://github.com/gjbex/atools), a library for easily running parameter sweep on an HPC cluster.

1. Generate configurations to run with benchmark_setup.py -a [size|n_workers]: Test scaling with respect to increasing dataset size or number of workers. This creates a directory containing a results folder and data.csv file containing the configurations.
2. Run configurations with an array job.
3. Gather all runtimes in a timing-results.csv file using benchmark_post.py.

## Snakemake
An attempt was made to run the configurations with Snakemake as it also allows to dynamiccaly request resources based on what configuration is run (for example, setting ppn based on the number of workers). It almost works, but still sometimes the execution fails due to a missing vsc-mympirun implementation.

