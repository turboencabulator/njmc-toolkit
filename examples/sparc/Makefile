SPEC=../../specs/sparc.spec
CC=gcc
CFLAGS=-I../../src

all: selfdis

################################################################
#
#	making a distribution

distfiles: driver.html sparcdis.html 

dist: distfiles
	make distclean
distclean:
	make clean cleanaux

sparcdis.html: sparcdis.nw
	noweave -filter l2h -autodefs c -index -html $^ > $@
driver.html: driver.nw
	noweave -filter l2h -autodefs c -index -html $^ > $@

################################################################
#
#	cleanup

clean: 
	/bin/rm -f sample *.[choms] *~ sparcdis.spec *.dvi *.log
	/bin/rm -f *.tex *.defs *.sml *.out *.blg

cleanaux:
	/bin/rm -f *.aux *.bbl *.ind *.idx *.ilg *.nwi *.toc

clobber: clean
	/bin/rm -f *.ps driver.html sparcdis.html

minimal: clobber cleanaux


################################################################
#
#	building a disassembler

.SUFFIXES: .nw

spec: 
	cd `dirname $(SPEC)`; make `basename $(SPEC)`

$(SPEC):
	cd `dirname $(SPEC)`; make `basename $(SPEC)`


sparc-names.c sparc-names.h: $(SPEC)
	tools -fieldnames sparc-names $^

sparcdis.m: sparcdis.nw
	notangle -L -R$@ $^ | cpif $@

sparcdis.h: sparcdis.nw
	notangle -L -R$@ $^ | cpif $@

sparcdis.spec: sparcdis.nw
	notangle -L -R$@ $^ | cpif $@

sparcdis.c: sparcdis.m sparcdis.spec $(SPEC)
	tools -c -lc-pat-names -matcher sparcdis.m -decoder $@ $(SPEC) sparcdis.spec

sparcdis.o: sparc-names.h sparcdis.h

driver.c: driver.nw
	notangle -L $^ | cpif $@

driver.o: sparcdis.h

selfdis: sparcdis.o driver.o sparc-names.o
	$(CC) -o $@ $(LDFLAGS) $^
