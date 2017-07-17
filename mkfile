DIRS=src specs examples checker
VERSION=0.5a
TARFILE=v$VERSION.tar
TARZIP=$TARFILE.gz
SMALLTARS=base.tar src.tar base-specs.tar base-checker.tar specs.tar examples.tar


all:V: news
	# do nothing

%.tar:V:
	tar cvf $target $stem

distfiles:V: version_check
	for i in $DIRS; do (cd $i; mk distfiles); done

distclean:V: clean
	for i in $DIRS; do (cd $i; mk distclean); done

dist:VQ: version_check news
	if [ -r ../archive/$TARZIP ]; then
          echo "Need to bump VERSION in mkfile; $TARZIP already in ../archive" 1>&2
	  exit 1
	fi
	if [ ! -d ../$VERSION ]; then
	  mkdir ../$VERSION
	fi
	for i in $DIRS; do (cd $i; mk distfiles); done
	if [ -x "`which copy`" ]; then
	  copy -R * ../$VERSION
	else
	  /bin/rm -rf ../$VERSION/*
	  tar cf - . | (cd ../$VERSION; tar xvf -)
	fi
	cd ../$VERSION
	/bin/rm -rf *.tar.gz */RCS
	mk distclean
	tar cvf ../$TARFILE .
	mv ../$TARFILE .
	mk $SMALLTARS
	gzip -v $TARFILE $SMALLTARS

archive:V: dist
	cp -i ../$VERSION/$TARZIP ../archive

version_check:VQ:
	if [ '"'"$VERSION"'"' != "`notangle -R'version string' src/main.nw | 
			           sed 's@ of [0-9]*/[0-9]*/[0-9]*@@'`" ]; then
	  echo "Version mismatch! mkfile $VERSION, main.nw `notangle -R'version string' src/main.nw`" 1>&2
	  exit 1
	fi
	if [ "$VERSION" != "`notangle -Rversion src/refman.nw`" ]; then
	  echo "Version mismatch! mkfile $VERSION, refman.nw `notangle -Rversion src/refman.nw`" 1>&2
	  exit 1
	fi
	if fgrep $TARZIP readme.html > /dev/null; then
	  : ok
	else
	  echo "Version mismatch! readme.html doesn't refer to $TARZIP"
	  exit 1
	fi
	if fgrep "Toolkit version~$VERSION}" specs/specs.nw > /dev/null; then
	  : ok
	else
	  echo "Version mismatch in title of specs/specs.nw"
	  exit 1
	fi
	if fgrep "<title>NJ Machine-Code Toolkit Source Distribution v$VERSION</title>" readme.html > /dev/null; then
	  : ok
	else
	  echo "Version mismatch! <title> of readme.html isn't version $VERSION"
	  exit 1
	fi
	echo "=========== Version $VERSION OK ========================================"

news:V: news/index.html

news/index.html:Q: `echo news/[0-9]*.html`
	echo "Building $target from $prereq" 1>&2
	echo "<html><head><title>NJ Machine-Code Toolkit News</title></head><body>" > $target
	echo " " >> $target
	echo "<h2>NJ Machine-Code Toolkit News</h2>" >> $target
	echo "This file points to release notes from previous versions" >> $target
	echo "of the toolkit, as well as old announcements" >> $target
	echo "<ul>" >> $target
	for i in $prereq; do
	  echo "<li><a href=`basename $i`>"
	  fgrep "<h2>" $i | sed 's/<[^>]*>//g'
	  echo "</a>"
	done >> $target
	echo "</ul></body></html>" >> $target



clean:V:
	for i in $DIRS; do (cd $i; mk clean); done
	/bin/rm -f *~ *.tar.gz

minimal:V:
	for i in $DIRS; do (cd $i; mk minimal); done
	/bin/rm -f *~ *.tar.gz 

