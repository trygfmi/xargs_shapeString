# python /Users/ojiro/Desktop/programming/running-terminal-commands-blog/xargs/xargs_shapeString/test/windows/wsl/check-DOM-string.py


import time
from lxml import html


start_time=time.time()

repository="xargs_shappeString2025-11-18 20:52:44"
# 1. 保存しておいたHTMLファイルを読み込む
with open("test/"+repository+".html", "r", encoding="utf-8") as f:
    page_text = f.read()

# 2. lxmlでパースする
tree = html.fromstring(page_text)

# 3. 今までSeleniumで使っていたXPathをそのまま使える！
results = tree.xpath('//code[@class="code-flex"]')

# 結果を確認
# print(f"見つかった数: {len(results)}")
# for i, el in enumerate(results, 1):
#     print(f"{i}個目")
#     print(el.text_content())
#     print()
    
quickstart_code = tree.xpath('(//code[@class="code-flex"])[3]')
for i, el in enumerate(quickstart_code, 1):
    print("#####quickstart_code#####")
    print(el.text_content())
    print()

procedure_code = tree.xpath('(//code[@class="code-flex"])[15]')
for i, el in enumerate(procedure_code, 1):
    print("#####procedure_code#####")
    print(el.text_content())
    print()
    
quickstart_output_code = tree.xpath('(//div[@class="entry-content"]/details/pre[@class="wp-block-code has-background"]/code)[3]')
for i, el in enumerate(quickstart_output_code, 1):
    print("#####quickstart_output_code#####")
    print(f"{i}個目")
    print(el.text_content())
    print()
    
procedure_output_code = tree.xpath('(//details//details//code)[3]')
for i, el in enumerate(procedure_output_code, 1):
    print("#####procedure_output_code#####")
    print(f"{i}個目")
    print(el.text_content())
    print()

end_time=time.time()
print("かかった時間:"+str(end_time-start_time))



