# تعيين الملفات (Markdown) لتحويلها إلى DOCX و PDF
FILES = $(patsubst %.md, %.docx, $(wildcard *.md))
FILES += $(patsubst %.md, %.pdf, $(wildcard *.md))

# تحديد المرشحات (filters)
FILTERS = --filter pandoc-crossref

# إعدادات تحويل PDF (محرك XeLaTeX)
PDF_ENGINE = --pdf-engine=xelatex --pdf-engine-opt=--shell-escape

# خيارات إضافية
OPTIONS = --number-sections
BIB_OPTIONS = --citeproc

# تحويل ملفات Markdown إلى DOCX
%.docx: %.md
	-pandoc "$<" $(FILTERS) $(OPTIONS) $(BIB_OPTIONS) -o "$@"

# تحويل ملفات Markdown إلى PDF باستخدام XeLaTeX
%.pdf: %.md
	-pandoc "$<" $(FILTERS) $(PDF_ENGINE) $(BIB_OPTIONS) $(OPTIONS) -o "$@"

# تنفيذ جميع التحويلات (DOCX و PDF)
all: $(FILES)

# تنظيف الملفات المؤقتة
clean:
	-rm -f $(FILES) *~

# تنظيف كامل الملفات بما في ذلك النسخ الاحتياطية
cleanall: clean
