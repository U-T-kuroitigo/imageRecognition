#U_T
#2022/09/14

from fastapi import FastAPI,File,UploadFile
import shutil
from PIL import Image
import pyocr
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/test/")
def read_root():
    return {"Hello": "World"}

@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/", response_class=HTMLResponse)
async def create_upload_file(file: UploadFile):
    with open('files/save.png', 'w+b') as buffer:
        shutil.copyfileobj(file.file, buffer)
            
    builder = pyocr.builders.TextBuilder(tesseract_layout=6)
    
        # OCRエンジンを取得
    engines = pyocr.get_available_tools()
    engine = engines[0]
    # 対応言語取得
    # langs = engine.get_available_languages()
    # print("対応言語:",langs) # ['eng', 'jpn', 'osd']
    
    img = Image.open('files/save.png')
    
    #画像を読みやすいように加工。
    img = img.convert('RGB')
    size = img.size
    img2 = Image.new('RGB',size)
     
    border=110  #この数値以上の彩度を白に
    
    # 彩度が一定以上あれば白色に置き換える
    for x in range(size[0]):
        for y in range(size[1]):
            r,g,b = img.getpixel((x,y))
            if r > border or g > border or b > border:
                r = 255
                g = 255
                b = 255
            img2.putpixel((x,y),(r,g,b))
    
    img2.save('files/save.png')
    # 画像の文字を読み込む
    txt = engine.image_to_string(img2, lang="jpn",builder = builder)
    print(txt)
    return ("<p style=\"white-space: pre-line\">" + txt + "</p>")