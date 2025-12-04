# python /Users/ojiro/Desktop/programming/running-terminal-commands-blog/xargs/xargs_shapeString/test/windows/msys2/execute-article-code.py


import time
from lxml import html
import subprocess


start_time=time.time()

repository="xargs_shappeString2025-11-18 20:52:44"
# 1. 保存しておいたHTMLファイルを読み込む
with open("test/"+repository+".html", "r", encoding="utf-8") as f:
    page_text = f.read()

# 2. lxmlでパースする
tree = html.fromstring(page_text)

# 3. 今までSeleniumで使っていたXPathをそのまま使える！
quickstart_code = tree.xpath('(//code[@class="code-flex"])[1]')
quickstart_code_array = quickstart_code[0].text_content().split("\n")
quickstart_cmd = f"""i=0
git_command_number=0
cd_command_number=1
target_directory="test/windows/msys2/"
cd_command="{quickstart_code_array[1]}"
output_file_name="auto_quickstart.txt"
while IFS= read -r keyword; do
    if [ $i == $git_command_number ]; then
        bash -c "cd $target_directory && $keyword"
    elif [ $i == $cd_command_number ]; then
        :
    else
        bash -c "cd $target_directory && $cd_command && $keyword >> ../$output_file_name"
        echo >> $target_directory$output_file_name
    fi
       
    echo
    i=$(($i+1))
done << EOF
""" + "\n".join(quickstart_code_array) + "\nEOF"
subprocess.run(quickstart_cmd, shell=True)

# 3. 今までSeleniumで使っていたXPathをそのまま使える！
procedure_code = tree.xpath('(//code[@class="code-flex"])[7]')
procedure_code_array = procedure_code[0].text_content().split("\n")
procedure_cmd = f"""rm -rf test/windows/msys2/xargs_shapeString
i=0
git_command_number=0
cd_command_number=1
target_directory="test/windows/msys2/"
cd_command="{procedure_code_array[1]}"
output_file_name="auto_procedure.txt"
while IFS= read -r keyword; do
    if [ $i == $git_command_number ]; then
        bash -c "cd $target_directory && $keyword"
    elif [ $i == $cd_command_number ]; then
        :
    else
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



