# ./start_update-readme.sh "testtest"
# "$(find . -type f -maxdepth 2 -name "start_update-readme.sh")" "testtest"


argument_number=${#@}
if [ $argument_number != 1 ]; then
    echo "引数は一つだけにしてください"
    exit 1
fi

shopt -s expand_aliases
source ~/.bash_profile

START_TIME=$(date +%s.%N)

commit_message="${1:-"auto update"}"
file_absolute_path="$(readlink -f "$0")"
directory_path="$(dirname "$file_absolute_path")"
echo "$directory_path"
cd "$directory_path"

python "$directory_path""/get-code-editor-value.py"
"$directory_path""/""update_readme.sh" "$commit_message"

END_TIME=$(date +%s.%N)
ELAPSED_TIME=$(echo "$START_TIME - $END_TIME" | bc)
echo "実行時間:""$ELAPSED_TIME""s"
