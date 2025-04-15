from markdown import markdown
from bs4 import BeautifulSoup
import sys
from datetime import datetime

def process_content(body):
    # Добавляем переносы для стихов
    body = (
        body.replace('"', '&quot;')
            .replace('\n', '  \n')
            .replace(':', ':  \n')  # Перенос после двоеточия
    )
    return markdown(
        body, 
        extensions=['extra', 'nl2br', 'md_in_html'],
        output_format='html5'
    )

def add_entry(title, body):
    entry_html = f'''
    <div class="entry" onclick="toggleEntry(this)">
        <div class="entry-header">
            <div class="entry-date">{datetime.now().strftime("%d.%m.%Y")}</div>
            <div class="entry-title">{title}</div>
            <div class="entry-toggle">▼</div>
        </div>
        <div class="entry-content">
            <div class="entry-text">{process_content(body)}</div>
        </div>
    </div>
    '''
    
    with open('thoughts.html', 'r+', encoding='utf-8') as f:
        content = f.read()
        new_content = content.replace(
            '<!-- NEW ENTRIES WILL BE ADDED HERE AUTOMATICALLY -->',
            f'{entry_html}\n<!-- NEW ENTRIES WILL BE ADDED HERE AUTOMATICALLY -->'
        )
        f.seek(0)
        f.truncate()
        f.write(new_content)

if __name__ == "__main__":
    add_entry(sys.argv[1], sys.argv[2])
