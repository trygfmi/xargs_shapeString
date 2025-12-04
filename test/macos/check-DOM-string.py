# python /Users/ojiro/Desktop/programming/running-terminal-commands-blog/xargs/xargs_shapeString/test/macos/check-DOM-string.py


import time
from lxml import html
import subprocess


start_time = time.time()

latest_html = "test/html/"+subprocess.run("ls -1t test/html | head -1", shell=True, capture_output=True, text=True).stdout.strip()
print("latest_html:"+latest_html)
search_all_code = '//code[@class="code-flex"]'
search_quickstart_code = '(//code[@class="code-flex"])[2]'
search_procedure_code = '(//code[@class="code-flex"])[10]'
search_quickstart_output = '(//div/div/details/pre/code)[2]'
search_procedure_output = '(//details//details//code)[2]'


# 1. 保存しておいたHTMLファイルを読み込む
with open(latest_html, "r", encoding="utf-8") as f:
    page_text = f.read()

# 2. lxmlでパースする
tree = html.fromstring(page_text)

# 3. 今までSeleniumで使っていたXPathをそのまま使える！
results = tree.xpath(search_all_code)

# 結果を確認
print(f"見つかった数: {len(results)}")
for i, el in enumerate(results, 1):
    print(f"{i}個目")
    print(el.text_content())
    print()
    
quickstart_code = tree.xpath(search_quickstart_code)
for i, el in enumerate(quickstart_code, 1):
    print("#####quickstart_code#####")
    print(el.text_content())
    print()

procedure_code = tree.xpath(search_procedure_code)
for i, el in enumerate(procedure_code, 1):
    print("#####procedure_code#####")
    print(el.text_content())
    print()
    
quickstart_output_code = tree.xpath(search_quickstart_output)
for i, el in enumerate(quickstart_output_code, 1):
    print("#####quickstart_output#####")
    print(f"{i}個目")
    print(el.text_content())
    print()
    
procedure_output_code = tree.xpath(search_procedure_output)
for i, el in enumerate(procedure_output_code, 1):
    print("#####procedure_output#####")
    print(f"{i}個目")
    print(el.text_content())
    print()

end_time=time.time()
print("かかった時間:"+str(end_time-start_time))



