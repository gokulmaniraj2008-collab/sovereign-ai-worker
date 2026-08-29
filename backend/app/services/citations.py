def build_sources(rows):
    return [{"document":r["filename"],"page":r["page_number"],"relevance":round(float(r["relevance"]),4)} for r in rows]
