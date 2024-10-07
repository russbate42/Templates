#!/bin/bash
# -f and -d are here for historic reasons. COuld be combined into one.
# Define arguments
if [[ $# -eq 0 ]]; then
    printf "No arguments passed. See -h.\n\n"
    exit 0
fi

show_help() {
    echo
    echo "RANDOM SCRIPT"
    echo
    echo "Usage: ./shell_with_opts.sh [options] [arguments]"
    echo
    echo "Options:"
    echo "-h, --help        Show this help message and exit"
    echo "-f, --file FILE Name of DAOD file"
    echo "-d, --directory DIRECTORY This is where the daod is located"
    echo "-o, --output OUTPUT Name of output file"
    echo "-r, --run-dir RUN_DIR Directory to run ntupler from"
    echo
    echo "Example:"
    echo "  ./shell_with_opts.sh -h"
    echo 
}

# Parse args
while [[ $# -gt 0 ]]; do
    case ${1} in
        -h|--help)
            show_help
            exit 0
            ;;
        -f|--file)
            FILE=$2
            shift
            shift
            ;;
        -d|--directory) # This is where the daod is located
            DIRECTORY=$2
            shift
            shift
            ;;
        -o|--output)
            OUTPUT=$2
            shift
            shift
            ;;
        -r|--run-dir) # directory to run from
            RUN_DIR=$2
            shift
            shift
            ;;
        -*|--*)
            echo "Unknown option ${1}"
            exit 1
            ;;
    esac
done

printf -- '\n----------------------\n'
printf -- '--RUNNING TEST SCRIPT \n'
printf -- '------------------------\n\n'

# ECHO ALL IMPORTANT VARIABLES
printf "\nCurrent working directory $(pwd)\n"
echo "FILE ${FILE}"
echo "DIRECTORY ${DIRECTORY}"
echo "OUTPUT ${OUTPUT}"
echo "RUN_DIR ${RUN_DIR}"
echo

printf '\nFinished!\n'

