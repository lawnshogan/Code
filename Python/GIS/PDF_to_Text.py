import PyPDF2

# Open the PDF file
with open("example.pdf", "rb") as file:
    # Create a PDF reader object
    reader = PyPDF2.PdfFileReader(file)
    # Get the number of pages in the PDF
    num_pages = reader.numPages
    # Create a variable to store the text
    text = ""
    # Loop through the pages
    for i in range(num_pages):
        # Get the page object
        page = reader.getPage(i)
        # Extract the text from the page
        text += page.extractText()
    # split the text into a list of lines
    lines = text.split("\n")
    # create variable to store the modified text
    new_text = ""
    # loop through the lines
    for line in lines:
        # check if the line contains "beginning" or "Beginning"
        if "beginning" in line.lower():
            new_text += "\n" + line
        elif "thence" in line.lower():
            new_text += "\n" + line
        else:
            new_text += " " + line
    # write the modified text to a txt file
    with open("output.txt", "w") as text_file:
        text_file.write(new_text)
