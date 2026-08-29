def chunk_pages(pages:list[dict],max_chars:int=1200,overlap:int=150):
    chunks=[]
    for page in pages:
        text=page["text"].strip(); start=0; idx=0
        while text and start<len(text):
            end=min(len(text),start+max_chars); chunk=text[start:end].strip()
            if chunk: chunks.append({"content":chunk,"page_number":page["page_number"],"chunk_index":idx}); idx+=1
            if end>=len(text): break
            start=max(0,end-overlap)
    return chunks
