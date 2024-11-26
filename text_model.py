import random
import cv2
from paddleocr import PaddleOCR


def text_out(path):   
    ocr = PaddleOCR(lang = 'korean') #다국어 사용시 multilingual
    result = ocr.ocr(path, cls = False)
    

    texts = [item[1][0] for line in result for item in line]
    
    combined_text = " ".join(texts)
    
    spell_checked = spell_checker.check(combined_text)
    combined_text = spell_checked.checked
    print("Combined Text (Spell Checked):", combined_text)

    combined_text_file_path = "static/text/combined_text.txt"
    #with open(combined_text_file_path, "w", encoding="utf-8") as file:
        #file.write(combined_text)
    
    return combined_text 
