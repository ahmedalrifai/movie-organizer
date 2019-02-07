def title_formater(title):
    if '(' in title:
        title = title[:title.index(' (')]
    return title
