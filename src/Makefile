HEAPNAME := njmc-toolkit
CM_HEAPROOT := toolkit.cm
CM_TESTROOT := test.cm

# CM already tracks dependencies.  Always try to build unconditionally.
.PHONY: all check
all:
	$(MAKE) -C ../tools
	echo "CM.make \"$(CM_HEAPROOT)\" andalso SMLofNJ.exportML \"$(HEAPNAME)\";" | CM_LOCAL_PATHCONFIG=./pathconfig sml

check:
	$(MAKE) -C ../tools
	echo "CM.make \"$(CM_TESTROOT)\";" | CM_LOCAL_PATHCONFIG=./pathconfig sml
