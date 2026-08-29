import fitz
def extract_pdf(path:str):
    doc=fitz.open(path); pages=[]
    for i,page in enumerate(doc,start=1): pages.append({"page_number":i,"text":page.get_text("text").strip()})
    doc.close(); return pages
