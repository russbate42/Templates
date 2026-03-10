#!/bin/zsh

function setup_latex(){
    if [[ -z "${1}" ]]; then
        printf "\n${1} not a file!\n"
        return 1
    else
        local folder_name=$(basename "${1}" .zip)
        printf "folder name: ${folder_name}\n"
    fi

    sudo unzip $1
    cd folder_name

    if [[ -n $(find ./ | grep sty) ]]; then
        printf "\nsty file exists\!\!\n"
    else
        local ins_file=$(find ./ | grep ins)
        latex $folder_name.sty
    fi

    sudo texhash
 
    return 0
}


