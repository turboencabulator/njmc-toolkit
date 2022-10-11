HEAPSUFFIX := $(shell sml @SMLsuffix)

.PHONY: all
all: ebnf dt-order tygen ml-lex+.$(HEAPSUFFIX)

ebnf: ebnf-dist.icn
	icont -o $@ ebnf-dist.icn
dt-order: dt-order-dist.icn
	icont -o $@ dt-order-dist.icn
tygen: tygen-dist.icn
	icont -o $@ tygen-dist.icn
ml-lex+.$(HEAPSUFFIX): ml-lex+.cm lexgen.sml export-lex.sml
	ml-build ml-lex+.cm ExportLexGen.lexGen
