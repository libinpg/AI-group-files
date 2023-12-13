import os
import random
from fpdf import FPDF
from PIL import Image, ImageDraw

def create_text_file(directory, filename, content):
    with open(os.path.join(directory, filename), 'w', encoding='utf-8') as file:
        file.write(content)

def create_pdf_file(directory, filename, content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=content, ln=True, align='C')
    pdf.output(os.path.join(directory, filename))

def create_image_file(directory, filename, content):
    image = Image.new('RGB', (200, 200), color='white')
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), content, fill='black')
    image.save(os.path.join(directory, filename))

def create_test_files(directory, file_count=5):
    if not os.path.exists(directory):
        os.makedirs(directory)

    categories = ['Finance', 'Health', 'Technology', 'Travel', 'Education']
    for i in range(file_count):
        for category in categories:
            content = f"This is a test file about {category}."
            filename_prefix = f"{category.lower()}_test_file_{i}"

            create_text_file(directory, f"{filename_prefix}.txt", content)
            create_pdf_file(directory, f"{filename_prefix}.pdf", content)
            create_image_file(directory, f"{filename_prefix}.png", content)

# 指定测试文件生成的目录
test_directory = "test_files"
create_test_files(test_directory)
