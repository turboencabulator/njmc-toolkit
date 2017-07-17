CCOPTS=
INCLUDES=-I../src
CFLAGS=$(CCOPTS) $(INCLUDES)
CC=gcc

all: xs-direct.o xs-indirect.o xs-asm.o

clean:
	rm -f *.o *.c *.h *~ *.html *.tex *.dvi *.log *.ps 
	rm -f xs.spec xs.m xs.decode

Makefile xs.spec xs.m xs.decode : xs.nw
	noweb -t xs.nw
xs.c: xs.spec xs.decode xs.m
	tools -decoder xs.c -matcher xs.m xs.decode xs.spec 
xs-direct.c xs-direct.h: xs.spec
	tools -encoder xs-direct -late-const xs.spec
xs-indirect.c xs-indirect.h: xs.spec
	tools -encoder xs-indirect -late-const -indirect xs xs.spec
xs-asm.c: xs.spec
	tools -asm-encoder xs-asm -indirect xsasm xs.spec
xs.html: xs.nw
	noweave -filter l2h -html -x xs.nw > xs.html
xs.tex: xs.nw
	noweb -o xs.nw
xs.dvi: xs.tex
	latex '\scrollmode \input xs'
	sh -c "while grep -s 'Rerun to get cross-references right' xs.log; do latex '\scrollmode \input xs'; done"
xs.ps:	xs.dvi
	dvips -o xs.ps xs
distfiles: xs.ps xs.html
	noweb -t xs.nw
