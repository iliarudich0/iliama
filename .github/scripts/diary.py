import markdown
from bs4 import BeautifulSoup
from datetime import datetime
import sys

def convert_markdown(text):
    return markdown.markdown(text, extensions=['extra'])

def add_entry(title, body):
    entry_html = f'''
    <div class="entry" onclick="toggleEntry(this)">
        <div class="entry-header">
            <div class="entry-date">{datetime.now().strftime("%d.%m.%Y")}</div>
            <div class="entry-title">{title}</div>
            <div class="entry-toggle">▼</div>
        </div>
        <div class="entry-content">
            <div class="entry-text">{convert_markdown(body)}</div>
        </div>
    </div>
    '''
    
    with open('thoughts.html', 'r+', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        marker = soup.find(string='<!-- NEW ENTRIES WILL BE ADDED HERE AUTOMATICALLY -->')
        if marker:
            new_entry = BeautifulSoup(entry_html, 'html.parser')
            marker.insert_before(new_entry)
            f.seek(0)
            f.write(str(soup))
            f.truncate()

if __name__ == "__main__":
    add_entry(sys.argv[1], sys.argv[2])
