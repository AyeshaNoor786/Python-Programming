import pdfplumber as pdftool
def fetch_text(file_path):
    # extract page by page
    with pdftool.open(file_path) as tool:
        for p_no,page in enumerate(tool.pages,1):
            print(" Page no: ",p_no,"--->")
            data=page.extract_text()
            print(data)
fetch_text("Practice.pdf")