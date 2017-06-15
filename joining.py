#pdf birleştirme
from PyPDF2 import PdfFileMerger
pdfs=['2017-03-22-113805-MÜHÜRLÜ.PDF', 'Harun-GÜLEÇ-Change-to-LA.pdf']
merger= PdfFileMerger() #ne yaptığımı anlamadım?
for pdf in pdfs: #pdfs dizisi içindeki her elemanı pdf olarak çağırdık.
    merger.append(open(pdf, 'rb'))
merger.write("result.pdf") #dosyaları alıp soyut bir dosyaya yazdırdık
