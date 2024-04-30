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

