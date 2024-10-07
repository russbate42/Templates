'''
Author: Russell Bate
    russell.bate@cern.ch, russellbate@phas.ubc.ca
'''

import argparse, subprocess, os, sys, pickle, copy
sys.path.append('../utils/')
from functions import run_subprocess
mass_points = [300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,
               1600,1800,2000,2250,2500,2750,3000,3500,4000,4500,5000,5500,
               6000]
jo_subFolder = [522557, 522558, 522559, 522560, 522561, 522562, 522563, 522564,
    522565, 522566, 522567, 522568, 522569, 522570, 522571, 522572, 522573,
    522574, 522575, 522576, 522577, 522578, 522579, 522580, 522581, 522582]

jobOptionRepo = '/cvmfs/atlas.cern.ch/repo/sw/Generators/MCJobOptions'
#local_jo_folder = '514xxx' 
local_jo_folder = '522xxx'
jo_dict = dict(zip(jo_subFolder,mass_points))
CWD = os.getcwd()

## argparsing
parser = argparse.ArgumentParser(description=
"""Modify lines in the madgraph control script.
""",
    epilog='\n')

## Main config of the program ------------------------------------------------
parser.add_argument('--dry-run', dest='dry_run', action='store_true',
    help='Recommended before launching script.',
    default=False)
parser.add_argument('--directory', dest='directory',
    action='store', type=str,
    help='Base directory to save output event gen files.',
    default=None)
parser.add_argument('--file-grep', dest='file_grep',
    action='store', type=str,
    help='String which filename contains to grep for.',
    default=None)
parser.add_argument('--old-string', dest='old_string',
    action='store', type=str,
    help='String to search for in lines in file.',
    required=True)
parser.add_argument('--new-string', dest='new_string',
    action='store', type=str,
    help='String to replace the old string with in the file.',
    required=True)
parser.add_argument('--silent', dest='silent',
    action='store_true',
    help='Run without any information in the terminal.',
    default=False)

## Complete parsing
args = parser.parse_intermixed_args()
DryRun = args.dry_run
Silent = args.silent
Directory = args.directory
FileGrep = args.file_grep
OldString = args.old_string
NewString = args.new_string
#-------------------------------------------------------------------------------

file_names = []
for subfolder in jo_subFolder:
    _dir = local_jo_folder + '/' + str(subfolder)
    print(f'Working on folder {_dir}')
    try:
        if FileGrep is None:
            grepped_filename = run_subprocess(f'ls -l {_dir}',
                        echo_command=False,
                        check=True, print_output=False, capture_output=True)
            grepped_filename = grepped_filename.split()[-1]
            print(grepped_filename)
        else:
            grepped_filename = run_subprocess(f'ls -l {_dir} | grep {FileGrep}',
                echo_command=False, check=True, print_output=False,
                                              capture_output=True)
            grepped_filename = grepped_filename.split()[-1]
            print(grepped_filename)
        if not '_tmp' in grepped_filename:
            file_names.append(f'{_dir}/{grepped_filename}')
        else:
            run_subprocess(f'rm {_dir}/{grepped_filename}')

    except CalledProcessError as cpe:
        print(f'\nCould not find file ')

for file_name in file_names:
    print(f'\nWorking on {file_name}')

    with open(file_name, 'r') as file:
        file_name_split = file_name.split('.')
        extension = f'.{file_name_split[-1]}'
        file_name_tmp = file_name.replace(f'{extension}', f'_tmp{extension}')
        print(f'\tOpening file {file_name_tmp}')
    
        with open(file_name_tmp, 'w') as tmp_file:
            lines = file.readlines()
            
            FoundOldString = False
            for i, line in enumerate(lines):
                if OldString in line:
                    FoundOldString = True
                    print(f'\t\tFound {OldString} in line {i+1}.')
                    print(f'\t\tReplacing this with {NewString}.')
                    line = line.replace(OldString, NewString)
                
                tmp_file.write(line)

            if FoundOldString == False:
                print(f'\t\tWarning: did not find {OldString} in file!')

    print(f'\tFinished copying lines to {file_name_tmp}')
    if DryRun:
        print(f'\tDry run, removing {file_name_tmp}')
        run_subprocess(f'rm {file_name_tmp}')
    else:
        print(f'\tMoving tmp file {file_name_tmp}')
        print(f'\tTo original file {file_name}')
        run_subprocess(f'rm {file_name}', echo_command=False)
        run_subprocess(f'mv {file_name_tmp} {file_name}' echo_command=False)
        print(f'\t .. done!')
