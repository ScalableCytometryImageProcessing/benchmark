from snakemake.utils import Paramspace
import pandas
import os

# declare a dataframe to be a paramspace
paramspace = Paramspace(pandas.read_csv(config["path"] + "/data_snake.csv"), filename_params="*")
vo = os.environ["VSC_DATA_VO_USER"]

rule all:
    input:
        expand("results/{params}", params=paramspace.instance_patterns)

rule run:
    output:
        f"results/{paramspace.wildcard_pattern}"
    params:
        props=paramspace.instance,
	config=f"{vo}/datasets/wbc/scip_zarr_small.yml",
	data=f"{vo}/datasets/wbc/images/sample0/*.zarr",
	pattern=paramspace.wildcard_pattern,
	scratch=os.environ["VSC_SCRATCH_NODE"],
	vscdata=os.environ["VSC_DATA"],
	cluster=os.environ["VSC_INSTITUTE_CLUSTER"],
	pythonpath=os.environ["PYTHONPATH"]
    shell:
        """
        mympirun --hybrid {params.props[np]} {params.vscdata}/python_lib_{params.cluster}/bin/scip \
           -d9104 --timing {config[path]}/{params.pattern}.json -t1 --headless --mode mpi \
           -l {params.scratch} -j {params.props[n_workers]} -s {params.props[partition_size]} \
           -m {params.props[memory]} {config[path]}/{params.pattern} {params.config} {params.data}
	"""

