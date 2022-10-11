CM_ROOT := sources.cm
HEAPNAME := njmc-toolkit

# CM already tracks dependencies.  Always try to build unconditionally.
.PHONY: all
all:
	$(MAKE) -C ../tools
	echo "CM.make \"$(CM_ROOT)\" andalso SMLofNJ.exportML \"$(HEAPNAME)\";" | CM_LOCAL_PATHCONFIG=./pathconfig sml
