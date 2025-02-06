import pymupdf4llm
import pymupdf

# md_text = pymupdf4llm.to_markdown("./testXactimateData/Water-Damage-Xactimate.pdf")

# print(md_text)

# open_file = open("./test.txt", "w")

# open_file.write(md_text)

# open_file.close()

doc = pymupdf.open("./testXactimateData/Resume.pdf")  # open a document
out = open("test.txt", "wb")  # create a text output
for page in doc:  # iterate the document pages
    text = page.get_text().encode("utf8")  # get plain text (is in UTF-8)
    print(text)
    out.write(text)  # write text of page
    out.write(bytes((12,)))  # write page delimiter (form feed 0x0C)
out.close()
