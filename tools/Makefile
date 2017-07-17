BINDIR=/dev/null

all: ebnf dt-order tygen

install: ebnf dt-order tygen
	cp ebnf dt-order tygen $(BINDIR)
	for i in ebnf dt-order tygen; do chmod +x $(BINDIR)/$$i; done

ebnf: ebnf-dist.icn
	icont -o ebnf ebnf-dist.icn
dt-order: dt-order-dist.icn
	icont -o dt-order dt-order-dist.icn
tygen: tygen-dist.icn
	icont -o tygen tygen-dist.icn
