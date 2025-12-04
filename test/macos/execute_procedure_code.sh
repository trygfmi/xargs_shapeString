#!/bin/bash
# ./execute_procedure_code.sh


echo "execute_procedure_code.sh"


shopt -s expand_aliases
file_absolute_path=$(readlink -f "$0")
parent_directory_path=$(dirname "$file_absolute_path")
repository=$(dirname "$(dirname "$parent_directory_path")")
repository_name=$(basename "$(dirname "$(dirname "$parent_directory_path")")")
test_os_path=$(basename "$(dirname "$parent_directory_path")")"/"$(basename "$parent_directory_path")"/"
now=$(date +%Y-%m-%d_%H:%M:%S)

output_procedure_path="$parent_directory_path""/compare-auto/auto_procedure_output"$now".txt"
read_procedure_file_path="get_article_procedure_code/"$(ls -1t "$test_os_path"get_article_procedure_code | sed -n '1p')

cd "$parent_directory_path"
#####################################################
rm -rf "$repository""/""$test_os_path""$repository_name"
#####################################################


i=0
while IFS= read -r command; do
    if [ $i == 3 ] || [ $i == 4 ]; then
        eval "$command" >> "$output_procedure_path"
        echo >> "$output_procedure_path"
    else
        eval "$command"
    fi
       
    echo
    i=$(($i+1))
done < "$read_procedure_file_path"


