#line 25 "z80.nw"
fields of opcodet (8) 
  lo 0:2 mid 3:5 hi 6:7 r 3:5 r1 0:2 op 0:7 dd 4:5 qq 4:5 bit3 3
fields of lit8 (8) n 0:7 d 0:7
fields of lit16 (16) nn 0:15
fieldinfo [r r1] is [names [B C D E H L _ A]]
fieldinfo dd is [names [BC DE HL SP]]
fieldinfo qq is [names [BC DE HL AF]]
#line 35 "z80.nw"
placeholder for opcodet is lo = 0
#line 18 "z80.nw"
relocatable reloc
constructors 
#line 39 "z80.nw"
pair0 dd : regpair is dd = dd & bit3 = 0
pair1 dd : regpair is dd = dd & bit3 = 1
#line 45 "z80.nw"
ld.r      r, r1        is  hi = 0b01 & mid = r     & lo = r1
ld.n      r, n         is  hi = 0b00 & mid = r     & lo = 0b110; n
ld.h.n    ("HL"), n    is  hi = 0b00 & mid = 0b110 & lo = 0b110; n
ld.fromh  r, ("HL")    is  hi = 0b01 & mid = r & lo = 0b110
ld.fromix r, ("IX"+d)  is  op = 0b11011101; hi = 0b01 & mid = r & lo = 0b110; d
ld.fromiy r, ("IY"+d)  is  op = 0b11111101; hi = 0b01 & mid = r & lo = 0b110; d
ld.toh    ("HL"), r    is  hi = 0b01 & mid = 0b110 & lo = r
ld.toix   ("IX"+d), r  is  op = 0b11011101; hi = 0b01 & mid = 0b110 & lo = r; d
ld.toiy   ("IY"+d), r  is  op = 0b11111101; hi = 0b01 & mid = 0b110 & lo = r; d
ld.ix.n   ("IX"+d), n  is  op = 0b11011101; hi = 0b00 & mid = 0b110 & lo = 0b110; d; n
ld.iy.n   ("IY"+d), n  is  op = 0b11111101; hi = 0b00 & mid = 0b110 & lo = 0b110; d; n
ld.a.bc   "A,(BC)"     is  op = 0b00001010
ld.a.de   "A,(DE)"     is  op = 0b00011010
ld.a.n    "A",(nn)     is  op = 0b00111010; nn
ld.a.i    "A, I"       is  op = 0b11101101; op = 0b01010111
ld.a.r    "A, R"       is  op = 0b11101101; op = 0b01011111
ld.i.a    "I, A"       is  op = 0b11101101; op = 0b01000111
ld.r.a    "R, A"       is  op = 0b11101101; op = 0b01001111
#line 67 "z80.nw"
ld.dd.nn  dd, nn       is  hi = 0b00 & pair0(dd)   & lo = 0b001; nn
ld.ix.nn  "IX", nn     is  hi = 0b11 & mid = 0b011 & lo = 0b101; op = 0b00100001; nn
ld.iy.nn  "IY", nn     is  hi = 0b11 & mid = 0b111 & lo = 0b101; op = 0b00100001; nn
ld.hl.nn  "HL", (nn)   is  op = 0b00101010; nn
ld.dd.mnn dd, (nn)     is  op = 0b11101101; hi = 0b01 & pair1(dd) & lo = 0b011; nn
