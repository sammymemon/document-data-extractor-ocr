import sys
import json
import os
from paddleocr import PaddleOCR

def main(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError("File not found.")

        ocr = PaddleOCR(use_angle_cls=True, lang="en")
        result = ocr.ocr(file_path, cls=True)
        
        # Combine recognized texts into one string
        extracted_text = ""
        if result and result[0]:
            extracted_text = " ".join([line[1][0] for line in result[0] if line[1][0]])
        
        output = {
            "status": "success",
            "extracted_text": extracted_text,
        }
    except Exception as e:
        output = {
            "status": "error",
            "message": str(e)
        }
    
    print(json.dumps(output))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"status": "error", "message": "No file path provided"}))
        sys.exit(1)
    main(sys.argv[1])
