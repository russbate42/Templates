import subprocess

''' Collection of useful functions for imports '''

def ps(str):
    if not Silent:
        print(str)
    return None

def pv(str):
    if Verbose:
        print(str)
    return None

def pd(str):
    if Debug:
        print(str)
    return None

def run_subprocess(cmd, echo_command=True, print_output=False,
                    capture_output=False, check=False):
    ''' launches a subprocess with different options.
    echo command: prints the command to terminal
    print_output: prints the output to terminal if possile
    capture_output: will capture stderr and stdout
    check: will throw an error if something fails.'''
    _shell=True
    if type(cmd) == str:
        pass
    elif type(cmd) == list:
        _shell=False
    else:
        raise ValueError('Invalid input to run_subprocess. '\
                +'Must be list or string.')
    if echo_command:
        print(f'\n>>> {cmd}')
    
    if capture_output == False:
        subprocess_out = subprocess.run(cmd,
            stdout=subprocess.PIPE, shell=_shell, check=check)
    else:
        subprocess_out = subprocess.run(cmd,
            capture_output=True, shell=_shell, check=check)

    if not subprocess_out is None:
        _output = subprocess_out.stdout.decode('utf-8')
    else:
        _output = None
    
    if print_output:
        print(_output)

    return _output

