# 設定ファイル読み込み用です


import os
import sys
from dotenv import load_dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


load_dotenv()

user_data_dir = os.getenv("USER_DATA_DIR")
profile = os.getenv("PROFILE")
access_url=os.getenv("ACCESS_URL")
