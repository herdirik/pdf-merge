#pdf birleştirme
from PyPDF2 import PdfFileMerger
pdfs=['file1.pdf', 'file2.pdf']
merger= PdfFileMerger() #ne yaptığımı anlamadım?
for pdf in pdfs: #pdfs dizisi içindeki her elemanı pdf olarak çağırdık.
    merger.append(open(pdf, 'rb'))
merger.write("result.pdf") #dosyaları alıp soyut bir dosyaya yazdırdık
