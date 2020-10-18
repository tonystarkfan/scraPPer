


with open('pdflinks.txt','r') as f, open('epublinks.txt','w') as epub_f:
    for line in f:
        id = line.split('/')[-1].rstrip()
        epub_url = 'https://link.springer.com/download/epub/' + id + '.epub'
        epub_f.write(epub_url)
        epub_f.write('\n')