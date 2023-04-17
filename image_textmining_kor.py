import pytesseract
from pytesseract import Output
import docx

# 한국어 학습 데이터 경로 추가
custom_config = r'--oem 3 --psm 6 tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ --tessdata-dir "C:/Tesseract-OCR/tessdata"'

# pytesseract가 인식하는 환경변수 경로 지정
pytesseract.pytesseract.tesseract_cmd = r'/Tesseract-OCR/tesseract.exe'

# 이미지 파일에서 텍스트 추출
result = pytesseract.image_to_string('/Users/desktop/test/page_1.jpg', lang='kor', config=custom_config, output_type=Output.DICT)

# 추출한 텍스트 출력
doc = docx.Document()
doc.add_paragraph(result['text'])
doc.save('/Users/desktop/result.docx')

# 텍스트 파일 출력
# with open('result.txt', mode='w', encoding='utf-8') as f:
#     f.write(result)
