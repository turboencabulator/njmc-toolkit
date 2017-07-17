# new architectures should be added to the ARCHS variable

ARCHS=mips sparc pentium spent ppc alpha
TOOLS=../base
CFLAGS=-I. -I$(TOOLS) -DemitX=emitbits
BUILTINS=
GDB=gdb
TOOLFLAGS=-verbose -lc-cons-names $(XTOOLFLAGS)
OBJS=$(TARGET)-check.o $(TARGET)-asm.o $(TARGET)-bin.o $(TARGET)-bits.o 
PENTSPECS=$(shell ls pentium-{[A-Z]*,arith,float}.spec)
CC=gcc -ansi -pedantic
################################################################
#
#	RULES TO BUILD CHECKER
# 
$(ARCHS):
	-rm chkraddr
	make check$@ TARGET=$@

$(TARGET)-checker: $(OBJS) mclib.o
	$(CC) $(OBJS) mclib.o -o $@

$(TARGET)-asm.o: $(TARGET)-asm.h $(TARGET)-asm.c $(TOOLS)/mclib.h
	$(CC) -c $(CFLAGS) $(TARGET)-asm.c -o $@
$(TARGET)-bits.o: $(TARGET)-bits.h $(TARGET)-bits.c $(TOOLS)/mclib.h
	$(CC) -c $(CFLAGS) $(TARGET)-bits.c -o $@
$(TARGET)-bin.o: $(TARGET)-bin.h $(TARGET)-bin.c  $(TOOLS)/mclib.h
	$(CC) -c $(CFLAGS) $(TARGET)-bin.c -o $@
chkraddr:
	-echo "==> 'make chkraddr' MUST be executed on the $(TARGET) machine"
	echo "main(){}" >_boot.c    
	$(CC) -g _boot.c -o _boot
	nm _boot | egrep "T _main|T main" | \
                   awk '{print "0x"$$1}' | cpif $@
	rm -f _boot.c _boot

$(TARGET)-check.o: $(TARGET)-check.c chkraddr
	$(CC) -c -DCHKRADDR=`cat chkraddr` -I. -I$(TOOLS) \
            $(TARGET)-check.c -o $@

$(TARGET)-check.c: $(TARGET).spec $(TARGET)-asm.h \
                                $(TARGET)-check.spec
	$(TOOLS)/tools $(TOOLFLAGS) -checker $(TARGET)-check \
          -indirect $(TARGET) $(TARGET).spec $(TARGET)-check.spec
	echo "#include \"$(TARGET)-asm.h\""> $(TARGET)-check.h

$(TARGET)-asm.h: $(TARGET)-asm.c
$(TARGET)-bin.h: $(TARGET)-bin.c
$(TARGET)-bits.h: $(TARGET)-bits.c
        # Created by rule for .c file

$(TARGET)-bin.c: $(TARGET).spec $(TOOLS)/tools
	$(TOOLS)/tools $(TOOLFLAGS) -late-const -byteorder X -indirect \
          $(TARGET)_bin:$(TARGET)_asm -encoder $(TARGET)-bin \
          $(TARGET).spec

$(TARGET)-asm.c: $(TARGET).spec $(TARGET)-names.spec $(TOOLS)/tools
	$(TOOLS)/tools $(TOOLFLAGS) -asm-encoder $(TARGET)-asm \
          -indirect $(TARGET)_asm $(TARGET).spec \
          $(TARGET)-names.spec

################################################################
#
#	RULES TO RUN CHECKER
# 
_$(TARGET).s: $(TARGET)-checker
	cat $(TARGET)-checker.s >$@
	./$(TARGET)-checker >> $@

_sparc.s: sparc-checker 
	cat $(TARGET)-checker.s > $@
	./$(TARGET)-checker | sed -e 's/main/_main/g' >> $@

_$(TARGET).out: _$(TARGET).s 
	-echo "===> Subsequent commands MUST be executed on the target $(TARGET)"
	$(CC) -g _$(TARGET).s -o _$(TARGET).out

#
# The Pentium spec is too big to check all at once, 
# so we break it up into pieces and check each one individually.
#
checkpentium:
	- rm pentium.spec
	@(for i in $(PENTSPECS); do \
	    echo "Checking $${i}"; \
	    cp $${i} pentium.spec; \
	    make dopentium TARGET=pentium; \
	done)

check$(TARGET): do$(TARGET)

do$(TARGET): _$(TARGET).out chkrfilter gdb-asmoutput gdb-binoutput
	echo "Checking $(TARGET)"
	./chkrfilter nawk _$(TARGET).out

dopentium: _pentium.out chkrfilter gdb-asmoutput gdb-binoutput
	./chkrfilter gawk _$(TARGET).out

dosparc: _sparc.out chkrfilter gdb-asmoutput gdb-binoutput
	echo "Checking sparc"
	sed -e 's/_//g' <gdb-asmoutput >_gdb
	mv _gdb gdb-asmoutput
	sed -e 's/_//g' <gdb-binoutput >_gdb
	mv _gdb gdb-binoutput

################################################################
#
#	MISCELLANY
# 
$(TOOLS)/tools $(TOOLS)/mclib.h $(TOOLS)/mclib.c $(TARGET).spec: 

mclib.o: $(TOOLS)/mclib.c
	$(CC) -c -I. -I$(TOOLS) $(TOOLS)/mclib.c -o $@

clean:
	/bin/rm -f *checker _*.[os] *.o *{-asm,-bin,-check}.[ch] *.out.* chkraddr *~







