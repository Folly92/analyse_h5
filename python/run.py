import os, sys, argparse, re, glob
from utils import *

parser = argparse.ArgumentParser()
parser.add_argument('--numRuns', type=int, default=1, help='Define number of runs to be analysed.')
args,_=parser.parse_known_args()

runs = args.numRuns
os.system('source /opt/exp_software/limadou/set_env_standalone.sh')

for irun,run in enumerate(glob.glob('/storage/gpfs_data/limadou/data/flight_data/L3h5/*.h5')):
    if irun>runs:
        break
    outfile = home()+"/root/"+(os.path.split(run)[1]).replace("h5","root")
    print("Test if output exists: ", outfile)
    if os.path.isfile(outfile):
        print("Output root file already exists... \n run analysis on the next run. ")
        runs=runs+1
    else:        
        cmd='python3 python/readH5.py --inputFile '+str(run)
        print(cmd)
        os.system(cmd)
 
