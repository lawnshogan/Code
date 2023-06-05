from bs4 import BeautifulSoup

def extract_info(text):
    soup = BeautifulSoup(text, 'lxml')

    items = []

    titles = soup.find_all('title')
    contents = soup.find_all('content:encoded')
    for title, content in zip(titles, contents):
        cleaned_title = title.text.replace("<![CDATA[", "").replace("]]>", "").strip()
        cleaned_content = content.text.replace("<![CDATA[", "").replace("]]>", "").strip()
        items.append((cleaned_title, cleaned_content))

    return items

def write_to_file(items, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for title, content in items:
            f.write(title + '\n')
            f.write('\n')  # Adds a line break between the title and the content
            f.write(content + '\n')
            # add 5 line breaks between each item and the next title
            f.write('\n'*6)  # separate each pair by 6 newlines

def main():
    with open('C:\\Users\\shawn\\DataScienceMaster\\Code\\SLB\\XML_Extract\\TEST.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    items = extract_info(text)
    write_to_file(items, 'C:\\Users\\shawn\\DataScienceMaster\\Code\\SLB\\XML_Extract\\Extracted_Text.txt')

if __name__ == "__main__":
    main()
