from bs4 import BeautifulSoup

def extract_info(xml_doc):
    soup = BeautifulSoup(xml_doc, 'lxml')
    
    items = []
    
    # Assuming every <title> is followed by a <div class='field-item even'>
    titles = soup.find_all('title')
    for title in titles:
        div = title.find_next('div', class_='field-item even')
        items.append((title.text, div.text if div else None))  # use .text to get text without html tags
    
    return items

def write_to_file(items, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for title, div in items:
            f.write(title + '\n')
            # add 5 line breaks
            f.write('\n'*5)
            if div:
                f.write(div + '\n')
            f.write('\n')  # separate each pair by a newline

def main():
    with open('posts_debbierosas.wordpress.2023-05-22.xml', 'r', encoding='utf-8') as f:
        xml_doc = f.read()
    
    items = extract_info(xml_doc)
    write_to_file(items, 'Debbie_Rosas_Posts.txt')

if __name__ == "__main__":
    main()

