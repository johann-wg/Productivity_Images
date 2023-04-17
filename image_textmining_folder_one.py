# 이미지에서 텍스트 추출 후 하나의 docx파일로 저장하는 코드
import os
import pytesseract
import docx
from pytesseract import Output

# 한국어 학습 데이터 경로 추가
custom_config = r'--oem 3 --psm 6 tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ --tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'

# pytesseract가 인식하는 환경변수 경로 지정
pytesseract.pytesseract.tesseract_cmd = r'C:/Tesseract-OCR/tesseract.exe'

# a 폴더 경로 지정
folder_path = '/Users/desktop/test'

# 폴더 내의 모든 이미지 파일 경로 가져오기
image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.png') or f.endswith('.jpg')]

# 추출한 텍스트를 저장할 변수 초기화
text = ''

# 모든 이미지 파일에서 텍스트 추출
for image_file in image_files:
    result = pytesseract.image_to_string(image_file, lang='kor', config=custom_config, output_type=Output.DICT)
    text += result['text'] + '\n'

# 추출한 텍스트를 docx 파일로 저장
doc = docx.Document()
doc.add_paragraph(text)
doc.save('/Users/desktop/testresult.docx')
