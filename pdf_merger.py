import PyPDF2
import sys
from sys import argv 
import os
import re



def check_string(s):
    is_pdf = s.lower().endswith('.pdf')
    
    # Check for a digit
    has_number = re.search(r'\d', s) is not None

    # Check for 'lesson' in any case
    has_lesson = 'lecture' in s.lower()

    return is_pdf and has_number and has_lesson


def get_lesson_number(s):
    digits = re.findall(r'\d', s)

    # Join the digits to form a number and convert to integer
    number = int(''.join(digits))
    return number
    

def get_relevant_files():
    all_files = os.listdir(os.curdir)
    pdf_files = [file for file in all_files if check_string(file)]
    pdf_files = sorted(pdf_files, key=get_lesson_number)
    return pdf_files



def merge_pdfs(paths, output):
    pdf_merger = PyPDF2.PdfMerger()
    for path in paths:
        pdf_merger.append(path)
    with open(output, 'wb') as fileobj:
        pdf_merger.write(fileobj)
    pdf_merger.close()


if __name__ == "__main__":
    merge_pdfs(get_relevant_files(), 'final_exam.pdf')  # 'merged.pdf' is the output file