# bash $(find . -type f -maxdepth 2 -name "start_test-macos.sh")
# "$(find . -type f -maxdepth 2 -name "start_test-macos.sh")"


file_absolute_path=$(readlink -f "$0")
project_root_directory=$(dirname "$(dirname "$file_absolute_path")")
shopt -s expand_aliases
source ~/.bash_profile

# python $(find . -type f -maxdepth 2 -name "save-DOM-string.py")
python "$project_root_directory"/test/save_DOM-string.py
python "$project_root_directory"/test/macos/get_article-code.py
"$project_root_directory"/test/macos/get_article_code_output.sh
python "$project_root_directory"/test/macos/get_article-output.py
python "$project_root_directory"/test/macos/compare_diff-output.py
