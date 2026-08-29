import fitz,pytesseract
from PIL import Image
from io import BytesIO
def ocr_pdf(path:str,dpi:int=180):
    doc=fitz.open(path); pages=[]
    for i,page in enumerate(doc,start=1):
        pix=page.get_pixmap(dpi=dpi,alpha=False); image=Image.open(BytesIO(pix.tobytes("png"))); pages.append({"page_number":i,"text":pytesseract.image_to_string(image).strip()})
    doc.close(); return pages
