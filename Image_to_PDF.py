from PIL import Image

# 이미지 파일 경로 설정
img_path = "/Users/jjong/desktop/개인정보동의.jpg"

# 이미지 열기
img = Image.open(img_path)

# PDF 파일 경로 설정
pdf_path = "/Users/jjong/desktop/개인정보동의.pdf"

# 이미지를 PDF 파일로 저장
img.save(pdf_path, "PDF", resolution=100.0)

# 아래는 다른 라이브러리를 사용한 다른 방법
# import os
# from pdf2image import convert_from_path

# # PDF 파일 경로 설정
# pdf_path = "/Users/jjong/desktop/test/테스트-테스트.pdf"

# # 이미지 파일 경로 설정
# image_dir = "/Users/jjong/desktop/"

# # 이미지 파일 이름 설정
# image_name = "test"

# # 이미지 저장 폴더가 존재하지 않으면 생성
# if not os.path.exists(image_dir):
#     os.makedirs(image_dir)

# # PDF 파일을 이미지로 변환하여 저장
# pages = convert_from_path(pdf_path)
# for i, page in enumerate(pages):
#     image_path = os.path.join(image_dir, f"{image_name}_{i+1}.jpg")
#     page.save(image_path, "JPEG")