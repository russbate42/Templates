#!/bin/zsh

if [[ $# -eq 0 ]]; then
    printf "No arguments passed. See -h.\n\n"
    return 0
fi

FILE=
DPI=300
OUTPUT=

show_help() {
    echo
    echo "RANDOM SCRIPT"
    echo
    echo "Usage: ./shell_with_opts.sh [options] [arguments]"
    echo
    echo "Options:"
    echo "-h, --help        Show this help message and return"
    echo "-f, --file  File containing pdfs to unpack"
    echo "            required argument"
    echo "-d, --dpi  Default DPI setting"
    echo "-o, --output  OUTPUT Name of output file"
    echo "              Will use input filename if not passed."
    echo
    echo "Example:"
    echo "source extract_pngs_from_pdf_files.zsh -h"
    echo 
}

# Parse args
while [[ $# -gt 0 ]]; do
    case ${1} in
        -h|--help) show_help; return 0;;
        -f|--file) FILE=$2; shift; shift;;
        -d|--directory) DPI=$2; shift; shift;;
        -o|--output) OUTPUT=$2; shift; shift;;
        -*|--*) printf "Unknown option ${1}"; return 1;;
    esac
done

if [[ -z "${FILE}" ]]; then
    printf "\n\t-f is a required arg.\n"
    return 0
fi

if [[ ! -f "${FILE}" ]]; then
    printf "\n\t${FILE} is not a valid file.\n"
    return 0
fi

# Load file list into array
local -a pdf_files
pdf_files=("${(@f)$(cat ${FILE})}")

# Iterate and print
for pdf in "${pdf_files[@]}"; do
    printf "\n\nFound: %s\n" "${pdf}"
    if [[ ! -f "${pdf}" ]]; then
        printf "\nWARNING: %s in %s DOESN\'T EXIST!!!\n" "${pdf}" "${FILE}"
    fi
    # Replace display loop body:
    cmd=(gs -dNOPAUSE -dBATCH -sDEVICE=png16m -r${DPI})
    cmd+=("-sOutputFile=${pdf:t:r}_%03d.png" "${pdf}")
    printf "Running: %s\n" "${cmd[*]}"
    # loc_command="gs -dNOPAUSE -dBATCH -sDEVICE=png16m -r${DPI}"
    # loc_command+=" -sOutputFile=${pdf:t:r}_\%03d.png ${pdf}"
    # printf "Running: %s${loc_command}"
    sleep .1
done

# Ask user
printf "\nProceed? [y/N]: "
read -r confirm
[[ "${confirm}" == "y" || "${confirm}" == "Y" ]] || return 0

printf -- '\n-----------------------------\n'
printf -- '-- CONVERTING PDFS TO PNGS --\n'
printf -- '-----------------------------\n\n'

# Main run loop
for pdf in "${pdf_files[@]}"; do
    cmd=(gs -dNOPAUSE -dBATCH -sDEVICE=png16m -r${DPI})
    cmd+=("-sOutputFile=${pdf:t:r}_%03d.png" "${pdf}")
    "${cmd[@]}"
    sleep .1
done

printf '\nFinished!\n'

