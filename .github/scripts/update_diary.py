from bs4 import BeautifulSoup
import sys
import re
from datetime import datetime

def create_entry(title, body, issue_num):
    # Автоматическая дата и обработка текста
    date = datetime.now().strftime('%d.%m.%Y')
    text = body.replace('"', "'").strip()
    
    return f"""
<div class="entry" onclick="toggleEntry(this)">
  <div class="entry-header">
    <div class="entry-date">{date}</div>
    <div class="entry-title">{title}</div>
    <div class="entry-toggle">▼</div>
  </div>
  <div class="entry-content">
    <div class="entry-text">{text}</div>
    <div class="entry-tags">
      <span class="tag">запись</span>
    </div>
  </div>
</div>
"""

if __name__ == "__main__":
    entry = create_entry(sys.argv[1], sys.argv[2], sys.argv[3])
    with open('thoughts.html', 'r+', encoding='utf-8') as f:
        content = f.read()
        updated = content.replace('<!-- Шаблон для новых записей -->', 
                                f"{entry}\n<!-- Шаблон для новых записей -->")
        f.seek(0)
        f.write(updated)
