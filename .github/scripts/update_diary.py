from bs4 import BeautifulSoup
import sys
import re
from datetime import datetime

def parse_issue(body):
    """Извлекает дату, теги и текст из тела Issue"""
    date_match = re.search(r'Дата:(.*)', body)
    tags_match = re.search(r'Теги:(.*)', body)
    
    date = date_match.group(1).strip() if date_match else datetime.now().strftime('%d.%m.%Y')
    tags = [t.strip() for t in tags_match.group(1).split(',')] if tags_match else []
    
    # Удаляем служебные строки из текста
    text = re.sub(r'(Дата:|Теги:).*', '', body).strip()
    
    return date, text, tags

def update_html(title, body, issue_num):
    date, text, tags = parse_issue(body)
    
    with open('thoughts.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    # Создаем новую запись
    new_entry = soup.new_tag('div', **{'class': 'entry', 'onclick': 'toggleEntry(this)'})
    new_entry.append(f"""
    <div class="entry-header">
        <div class="entry-date">{date}</div>
        <div class="entry-title">{title} <small>(Issue #{issue_num})</small></div>
        <div class="entry-toggle">▼</div>
    </div>
    <div class="entry-content">
        <div class="entry-text">{text}</div>
        <div class="entry-tags">
            {''.join(f'<span class="tag">{tag}</span>' for tag in tags)}
        </div>
    </div>
    """)
    
    # Вставляем перед шаблоном
    template = soup.find(text=lambda t: 'Шаблон для новых записей' in t)
    if template:
        template.parent.insert_before(new_entry)
    
    with open('thoughts.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == "__main__":
    update_html(sys.argv[1], sys.argv[2], sys.argv[3])
