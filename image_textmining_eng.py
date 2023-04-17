import pytesseract
from pytesseract import Output
import docx

# pytesseract가 인식하는 환경변수 경로 지정
pytesseract.pytesseract.tesseract_cmd = r'C:/Tesseract-OCR/tesseract.exe'

# 이미지 파일에서 텍스트 추출
result = pytesseract.image_to_string('/Users/jjong/desktop/get2.jpg', lang='eng', output_type=Output.DICT)

# 추출한 텍스트 출력
doc = docx.Document()
doc.add_paragraph(result['text'])
doc.save('/Users/jjong/desktop/result.docx')
