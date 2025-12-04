# python $(find . -type f -maxdepth 3 -name "get_article-output.py" | grep macos)


import time
from lxml import html
import subprocess
from datetime import datetime


start_time=time.time()

target_os = "macos"
now = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
latest_html = "test/html/"+subprocess.run("ls -1t test/html | head -1", shell=True, capture_output=True, text=True).stdout.strip()
search_quickstart_output = '(//div/div/details/pre/code)[2]'
search_procedure_output = '(//details//details//code)[2]'
output_quickstart_name = f"manual_quickstart_output{now}.txt"
output_procedure_name = f"manual_procedure_output{now}.txt"

print("latest_html:"+latest_html)

# 1. 保存しておいたHTMLファイルを読み込む
with open(latest_html, "r", encoding="utf-8") as f:
    page_text = f.read()

# 2. lxmlでパースする
tree = html.fromstring(page_text)

# 3. 今までSeleniumで使っていたXPathをそのまま使える！
quickstart_output = tree.xpath(search_quickstart_output)
quickstart_output_text = quickstart_output[0].text_content()
print("quickstart_output_text:"+quickstart_output_text)
with open("test/"+target_os+"/compare-manual/"+output_quickstart_name, "w", encoding="utf-8") as f:
    page_text = f.write(quickstart_output_text)
    
print()

# 3. 今までSeleniumで使っていたXPathをそのまま使える！
procedure_output = tree.xpath(search_procedure_output)
procedure_output_text = procedure_output[0].text_content()
print("procedure_output_text:"+procedure_output_text)
with open("test/"+target_os+"/compare-manual/"+output_procedure_name, "w", encoding="utf-8") as f:
    page_text = f.write(procedure_output_text)


end_time=time.time()
print("かかった時間:"+str(end_time-start_time))



