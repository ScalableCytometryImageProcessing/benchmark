#!/bin/bash
# properties = {properties}

module load SciPy-bundle/2021.10-foss-2021b
module load vsc-mympirun
export PYTHONPATH="${{VSC_DATA}}/python_lib_${{VSC_INSTITUTE_CLUSTER}}/lib/python3.9/site-packages/:${{PYTHONPATH}}"

{exec_job}
