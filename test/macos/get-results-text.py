# python /Users/ojiro/Desktop/programming/running-terminal-commands-blog/xargs/xargs_shapeString/test/macos/get-results-text.py


import time
from lxml import html


start_time=time.time()

repository="xargs_shappeString2025-11-18 17:13:12"
# 1. 保存しておいたHTMLファイルを読み込む
with open("test/"+repository+".html", "r", encoding="utf-8") as f:
    page_text = f.read()

# 2. lxmlでパースする
tree = html.fromstring(page_text)

# 3. 今までSeleniumで使っていたXPathをそのまま使える！
results = tree.xpath('//details//code')

# 結果を確認
print(f"見つかった数: {len(results)}")
for i, el in enumerate(results, 1):
    print(f"{i}個目")
    print(f"{el.text_content()}")
    # print(el.text_content())
    # print(html.tostring(el, encoding="unicode"))
    print()

end_time=time.time()
print("かかった時間:"+str(end_time-start_time))



