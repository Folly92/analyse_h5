import os, sys, argparse, re, glob
from utils import *

parser = argparse.ArgumentParser()
parser.add_argument('--numRuns', type=int, default=1, help='Define number of runs to be analysed.')
parser.add_argument('--hepd', action='store_true', help='Analyse HEPD data.')
parser.add_argument('--leos', action='store_true', help='Analyse LEOS data.')
args,_=parser.parse_known_args()

runs = args.numRuns
os.system('source /opt/exp_software/limadou/set_env_standalone.sh')

datapath = ''
if args.hepd:
    datapath = '/storage/gpfs_data/limadou/data/flight_data/L3h5/'
elif args.leos:
    datapath = '/storage/gpfs_data/limadou/data/cses_data/HEPP_LEOS/*HEP_1*'
    
for irun,run in enumerate(glob.glob(datapath+'*.h5')):
    if irun>runs:
        break
    outfile = home()+"/root/"+(os.path.split(run)[1]).replace("h5","root")
    print("Test if output exists: ", outfile)
    if os.path.isfile(outfile):
        print("Output root file already exists... \n run analysis on the next run. ")
        runs=runs+1
    else:        
        cmd='python3 python/readH5.py --inputFile '+str(run)
        if args.hepd:
            cmd+=' --data hepd'
        elif args.leos:
            cmd+=' --data leos'
        print(cmd)
        os.system(cmd)
 
