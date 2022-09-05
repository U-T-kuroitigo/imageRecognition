# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PIL import Image
import pyocr

# OCRエンジンを取得
engines = pyocr.get_available_tools()
engine = engines[0]
# 対応言語取得
langs = engine.get_available_languages()
print("対応言語:",langs) # ['eng', 'jpn', 'osd']

# 画像の文字を読み込む
txt = engine.image_to_string(Image.open('test1.png'), lang="jpn") # 修正点：lang="eng" -> lang="jpn"
print(txt)
