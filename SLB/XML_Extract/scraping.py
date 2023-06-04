from bs4 import BeautifulSoup

def extract_info(xml_doc):
    soup = BeautifulSoup(xml_doc, 'lxml')  # Use 'lxml' parser as it's suitable for both HTML and XML documents
    
    # Find the title and div elements
    titles = soup.find_all('title')
    divs = soup.find_all('div', class_='field-item even')
    
    return titles, divs

def write_to_file(titles, divs, filename):
    with open(filename, 'w') as f:
        for title in titles:
            f.write(str(title) + '\n')
        
        for div in divs:
            f.write(str(div) + '\n')

def main():
    # Replace with your XML file
    with open('posts_debbierosas.wordpress.2023-05-22.xml', 'r') as f:
        xml_doc = f.read()
    
    titles, divs = extract_info(xml_doc)
    write_to_file(titles, divs, 'Debbie_Rosas_Posts.txt')

if __name__ == "__main__":
    main()
