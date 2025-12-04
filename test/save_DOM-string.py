# python $(find . -type f -maxdepth 2 -name "save_DOM-string.py")


import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from feature.use_selenium_feature import getDriver
from feature.read_env import *
from datetime import datetime


start_time=time.time()

now = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
repository="test/html/"+repository_name+now

driver = getDriver()

driver.get(article_url)
title = driver.title
print(title)

# input()
# その瞬間のページ全体のHTML（JSで生成されたものも含む）を保存
html = driver.page_source
# ファイルに保存（UTF-8で日本語もバッチリ）
with open(repository+".html", "w", encoding="utf-8") as f:
    f.write(html)
print("保存完了！ → "+repository+now+".html")

driver.quit()

end_time=time.time()
print("かかった時間:"+str(end_time-start_time))



