# python $(find . -type f -maxdepth 3 -name "get_article-code.py" | grep macos)



import time
from lxml import html
import subprocess
from datetime import datetime


start_time=time.time()

target_os = "macos"
now = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
latest_html = "test/html/"+subprocess.run("ls -1t test/html | head -1", shell=True, capture_output=True, text=True).stdout.strip()
print("latest_html:"+latest_html)
search_quickstart_code = '(//code[@class="code-flex"])[2]'
search_procedure_code = '(//code[@class="code-flex"])[10]'
output_quickstart_name = f"test/macos/get_article_quickstart_code/auto_quickstart_output{now}.txt"
output_procedure_name = f"test/macos/get_article_procedure_code/auto_procedure_output{now}.txt"

# 1. 保存しておいたHTMLファイルを読み込む
with open(latest_html, "r", encoding="utf-8") as f:
    page_text = f.read()

# 2. lxmlでパースする
tree = html.fromstring(page_text)

# 3. 今までSeleniumで使っていたXPathをそのまま使える！
quickstart_code = tree.xpath(search_quickstart_code)
quickstart_code_array = quickstart_code[0].text_content().split("\n")
with open(output_quickstart_name, "w", encoding="utf-8") as quickstart_f:
    for line in quickstart_code_array:
        quickstart_f.write(line+"\n")

# 3. 今までSeleniumで使っていたXPathをそのまま使える！
procedure_code = tree.xpath(search_procedure_code)
procedure_code_array = procedure_code[0].text_content().split("\n")
with open(output_procedure_name, "w", encoding="utf-8") as procedure_f:
    for line in procedure_code_array:
        procedure_f.write(line+"\n")


end_time=time.time()
print("かかった時間:"+str(end_time-start_time))



