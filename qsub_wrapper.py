#!/apps/gent/RHEL8/zen2-ib/software/Python/3.9.6-GCCcore-11.2.0/bin/python

import os
import sys
from snakemake.utils import read_job_properties

jobscript = sys.argv[1]
job_properties = read_job_properties(jobscript)

# do something useful with the threads
params = job_properties["wildcards"]

os.system("qsub -l walltime=12:00:00 -l nodes=1:ppn={np} -l mem=96gb {script}".format(np=params["np"], script=jobscript))
