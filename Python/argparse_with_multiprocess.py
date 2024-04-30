import argparse, subprocess, os, sys, pickle, copy
from concurrent.futures import ProcessPoolExecutor
from time import sleep

WD = os.getcwd()

## argparsing
parser = argparse.ArgumentParser(description=
"""Template argparse program.
""")

main_group = parser.add_argument_group('Main')
first_group = parser.add_argument_group('First Group')
second_group = parser.add_argument_group('Second Group')

## Main config of the program ------------------------------------------------
main_group.add_argument('--integers', dest='integers', action='store',
    type=int, default=9, choices=[1,2,3,4,5,6,7,8,9,10],
    help='Argument with set choices.')
main_group.add_argument('--silent', dest='silent', action='store_true',
    help='Toggle for boolean',
    default=True)
main_group.add_argument('--second-integers', dest='second_integers', action='store',
    help='Accepts list like arguments.', nargs='+', type=int,
    default=None)
main_group.add_argument('--optional-argument', dest='optional_arg', action='store',
    help='Optional argument.', nargs='?', type=int,
    default=None)
main_group.add_argument('--pickle-filename', dest='pickle_filename',
    action='store', type=str,
    help='Name for the pickled dictionary of results.',
    default='submit-output')
main_group.add_argument('--print-results', dest='print_results',
    action='store_true',
    help='Print the last lines of the results from the execution.',
    default=False)

## For local jobs -----------------------------------------------------------
first_group.add_argument('--input-dir', dest='input_dir',
    action='store', type=str,
    help='Standard usage.',
    default=None)

## For grid jobs ------------------------------------------------------------
second_group.add_argument('--output-dir', dest='output_dir', action='store_true',
    help='Standard usage for output file',
    default=False)

## Complete parsing
args = parser.parse_intermixed_args() # this mixed positional with non positional
print(dir(args))
sys.exit()

Integers = args.integers
Local = args.local
InputDir = args.input_dir
OutputDir = args.output_dir


## Use multithreading to speed this up! ---------------------------------------
#=============================================================================#
results_dict_raw = dict()
results_dict = dict()

if Test:
    print('Running in test mode')
    for jo_folder, mp in jo_dict.items():
        _output = run_subprocess2(Generation_script_dict[mp], echo_command=True,
                        print_output=True, capture_output=True)
        break
    sys.exit()

with ProcessPoolExecutor(max_workers=CPUs) as executor:
    for jo_folder, mp in jo_dict.items():
        print('Submitting run script in {}'.format(mp))
    
        results_dict_raw[mp] = executor.submit(run_subprocess2,
                            Generation_script_dict[mp], echo_command=False,
                            print_output=False, capture_output=True)

for key, val in results_dict_raw.items():
    results_dict[key] = val.result()

if PrintResults:
    for mp, value in results_dict.items():
        print('\n\n\t=== Mass Point: {} ===\n'.format(mp))
        print(value)

## Same pickle file
with open('{}.pickle'.format(PickleFileName), 'wb') as handle:
    pickle.dump(results_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

