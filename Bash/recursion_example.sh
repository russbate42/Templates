#!/bin/zsh

# value=4
# while [[ $value -gt 0 ]]; do
#     printf "value: ${value}\n"
#     value=$((value - 1))
# done
# return 0

function get_parent_directory {
    local num_parent=1
    local full_filepath=
    
    while [[ $# -gt 0 ]]; do
        full_filepath=$1; shift 1;
        case "$1" in
            -n); num_parent=$2; shift 2;;
            *); printf "Uknown argument"; exit 0;
        esac
    done
    
    return_file=$(basename $full_filepath)
    full_filepath=$(dirname $full_filepath)
    while [[ $num_parent -gt 0 ]]; do
        base_name=$(basename $full_filepath)
        return_file="${base_name}/${return_file}"
        
        full_filepath=$(dirname $full_filepath)
        num_parent=$((num_parent - 1))
    done

    printf "${return_file}"
}

test_filename='foo/bar/baz/taz'

downsize=$(get_parent_directory $test_filename -n 1)
printf "${downsize}\n"

downsize=$(get_parent_directory $test_filename -n 2)
printf "${downsize}\n"

downsize=$(get_parent_directory $test_filename -n 3)
printf "${downsize}\n"

downsize=$(get_parent_directory $test_filename -n 4)
printf "${downsize}\n"
# echo $(get_parent_directory -n 1 $test_filename)
# echo $(get_parent_directory -n 2 $test_filename)
# echo $(get_parent_directory -n 3 $test_filename)



