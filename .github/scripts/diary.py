from bs4 import BeautifulSoup
import sys
import re
from datetime import datetime

def add_entry(title, body, issue_id):
    # Генерируем HTML записи
    entry_html = f'''
    <div class="entry" onclick="toggleEntry(this)">
        <div class="entry-header">
            <div class="entry-date">{datetime.now().strftime('%d.%m.%Y')}</div>
            <div class="entry-title">{title}</div>
            <div class="entry-toggle">▼</div>
        </div>
        <div class="entry-content">
            <div class="entry-text">{body}</div>
        </div>
    </div>
    '''
    
    # Обновляем thoughts.html
    with open('thoughts.html', 'r+', encoding='utf-8') as f:
        content = f.read()
        new_content = content.replace(
            '<!-- НОВЫЕ ЗАПИСИ -->', 
            f'{entry_html}\n<!-- НОВЫЕ ЗАПИСИ -->'
        )
        f.seek(0)
        f.write(new_content)

if __name__ == "__main__":
    add_entry(sys.argv[1], sys.argv[2], sys.argv[3])
