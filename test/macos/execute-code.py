# python /Users/ojiro/Desktop/programming/running-terminal-commands-blog/xargs/xargs_shapeString/test/macos/execute-code.py


import time
from lxml import html
import subprocess


start_time=time.time()

# repository="xargs_shappeString2025-11-18 17:13:12"
repository="xargs_shappeString2025-11-18 20:52:44"
# 1. 保存しておいたHTMLファイルを読み込む
with open("test/"+repository+".html", "r", encoding="utf-8") as f:
    page_text = f.read()

# 2. lxmlでパースする
tree = html.fromstring(page_text)

# 3. 今までSeleniumで使っていたXPathをそのまま使える！
quickstart_code = tree.xpath('(//code[@class="code-flex"])[2]')
quickstart_code_array = quickstart_code[0].text_content().split("\n")
quickstart_cmd = f"""i=0
source_command_number=0
git_command_number=1
cd_command_number=2
source_command="{quickstart_code_array[0]}"
target_directory="test/macos/"
cd_command="{quickstart_code_array[2]}"
output_file_name="macos_quickstart_result.txt"
while IFS= read -r keyword; do
    if [ $i == $source_command_number ]; then
        :
    elif [ $i == $git_command_number ]; then
        #bash -c "$source_command && cd $target_directory && $keyword"
        bash -c "cd $target_directory && $keyword"
    elif [ $i == $cd_command_number ]; then
        :
    else
        #bash -c "$source_command && cd $target_directory && $cd_command && $keyword" >> results.txt
        bash -c "cd $target_directory && $cd_command && $keyword >> ../$output_file_name"
        echo >> $target_directory$output_file_name
    fi
       
    echo
    i=$(($i+1))
done << EOF
""" + "\n".join(quickstart_code_array) + "\nEOF"
subprocess.run(quickstart_cmd, shell=True)

# 3. 今までSeleniumで使っていたXPathをそのまま使える！
procedure_code = tree.xpath('(//code[@class="code-flex"])[10]')
procedure_code_array = procedure_code[0].text_content().split("\n")
procedure_cmd = f"""i=0
source_command_number=0
git_command_number=1
cd_command_number=2
source_command="{procedure_code_array[0]}"
target_directory="test/macos/"
cd_command="{procedure_code_array[2]}"
output_file_name="macos_procedure_result.txt"
while IFS= read -r keyword; do
    if [ $i == $source_command_number ]; then
        :
    elif [ $i == $git_command_number ]; then
        #bash -c "$source_command && cd $target_directory && $keyword"
        bash -c "cd $target_directory && $keyword"
    elif [ $i == $cd_command_number ]; then
        :
    else
        #bash -c "$source_command && cd $target_directory && $cd_command && $keyword" >> results.txt
        bash -c "cd $target_directory && $cd_command && $keyword >> ../$output_file_name"
        echo >> $target_directory$output_file_name
    fi
       
    echo
    i=$(($i+1))
done << EOF
""" + "\n".join(procedure_code_array) + "\nEOF"
subprocess.run(procedure_cmd, shell=True)

end_time=time.time()
print("かかった時間:"+str(end_time-start_time))



