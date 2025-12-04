#!/bin/bash
# ./get_article_code_output.sh
# $(find . -type f -maxdepth 3 -name "get_article_code_output.sh" | grep macos)


echo "get_article_code_output.sh"


file_absolute_path=$(readlink -f "$0")
parent_directory_path=$(dirname "$file_absolute_path")

"$parent_directory_path""/""execute_quickstart_code.sh"
"$parent_directory_path""/""execute_procedure_code.sh"


