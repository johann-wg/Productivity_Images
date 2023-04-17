# 이미지에서 텍스트 추출 후 각각의 파일로 docx 저장
import os
import pytesseract
import docx
from pytesseract import Output

# 한국어 학습 데이터 경로 추가
custom_config = r'--oem 3 --psm 6 tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ --tessdata-dir "C:/Tesseract-OCR/tessdata"'

# pytesseract가 인식하는 환경변수 경로 지정
pytesseract.pytesseract.tesseract_cmd = r'C:/Tesseract-OCR/tesseract.exe'

# a 폴더 경로 지정
folder_path = '/Users/jjong/desktop/test'

# 폴더 내의 모든 이미지 파일 경로 가져오기
image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.png') or f.endswith('.jpg')]

# 각 이미지 파일에서 텍스트 추출하여 해당 이미지 파일 이름과 동일한 이름의 docx 파일로 저장
for image_file in image_files:
    result = pytesseract.image_to_string(image_file, lang='kor', config=custom_config, output_type=Output.DICT)
    text = result['text']
    doc = docx.Document()
    doc.add_paragraph(text)
    doc.save(os.path.splitext(image_file)[0] + '.docx')
