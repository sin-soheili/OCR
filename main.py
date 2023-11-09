from fastapi import FastAPI,File,UploadFile
import shutil
import pytesseract

app = FastAPI()

''' Enter your image to extract its text!'''

@app.post('/ocr',description='it gives an image file that contains text and extract the text on the image')
def ocr(image: UploadFile = File(...,description='Upload your image in here')):
    filepath = 'textfile'
    with open(filepath,'w+b') as buffer:
        shutil.copyfileobj(image.file,buffer)
    return pytesseract.image_to_string(filepath,lang='eng')
