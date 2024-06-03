'''
Author: russbate42
'''

from concurrent.futures import ProcessPoolExecutor

parser = argparse.ArgumentParser(description=
"""Pull args for the multiprocess.
""")
main_group = parser.add_argument_group('Main')
main_group.add_argument('--cpus', dest='cpus', action='store',
    type=int, default=9, choices=[1,2,3,4,5,6,7,8,9,10],
    help='Number of cpus. Default is 10.')
args = parser.parse_intermixed_args()
CPUs = args.cpus

A = '1'
B = '2'

def myfunction(arg_1, arg_2, optarg=2):
    return 'results'

results_dict_raw = dict()
list_containing_processes = ['process_1', 'process_2', 'process_3']
with ProcessPoolExecutor(max_workers=CPUs) as executor:
    for thing_to_iterate in list_containing_processes:
    
        results_dict_raw[thing_to_iterate] = executor.submit(myfunction,
                            A, B, optarg=3)

    prints('\n\n#===============================#')
    prints('# Waiting on ProcessPoolExecutor ..')
    prints('#===============================#\n\n')

## Results must be serializeable (pickleable)
## Same pickle file
with open('{}.pickle'.format(PickleFileName), 'wb') as handle:
    pickle.dump(results_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

