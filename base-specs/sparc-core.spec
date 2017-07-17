#line 37 "sparc.nw"
fields of instruction (32) 
#line 44 "sparc.nw"
inst 0:31 op 30:31 disp30 0:29 rd 25:29 op2 22:24 imm22 0:21 a 29:29 cond 25:28
disp22 0:21 op3 19:24 rs1 14:18 i 13:13 asi 5:12 rs2 0:4 simm13 0:12 opf 5:13
#line 371 "sparc.nw"
fd 25:29 cd 25:29 fs1 14:18 fs2 0:4
#line 458 "sparc.nw"
rs1i 14:18 rdi 25:29
#line 412 "sparc.nw"
fieldinfo
[ rd rs1 rs2 ] is [ 
#line 397 "sparc.nw"
names [ "%g0"  "%g1"  "%g2"  "%g3"  "%g4"  "%g5"  "%g6"  "%g7"
        "%o0"  "%o1"  "%o2"  "%o3"  "%o4"  "%o5"  "%sp"  "%o7"
        "%l0"  "%l1"  "%l2"  "%l3"  "%l4"  "%l5"  "%l6"  "%l7"
        "%i0"  "%i1"  "%i2"  "%i3"  "%i4"  "%i5"  "%fp"  "%i7" ]
#line 413 "sparc.nw"
                                                              ]
[ fd fs1 fs2 ] is [ 
#line 402 "sparc.nw"
names [ "%f0"  "%f1"  "%f2"  "%f3"  "%f4"  "%f5"  "%f6"  "%f7"
        "%f8"  "%f9"  "%f10" "%f11" "%f12" "%f13" "%f14" "%f15"
        "%f16" "%f17" "%f18" "%f19" "%f20" "%f21" "%f22" "%f23"
        "%f24" "%f25" "%f26" "%f27" "%f28" "%f29" "%f30" "%f31" ]
#line 414 "sparc.nw"
                                                               ]
            cd is [ 
#line 407 "sparc.nw"
names [ "%c0"  "%c1"  "%c2"  "%c3"  "%c4"  "%c5"  "%c6"  "%c7"
        "%c8"  "%c9"  "%c10" "%c11" "%c12" "%c13" "%c14" "%c15"
        "%c16" "%c17" "%c18" "%c19" "%c20" "%c21" "%c22" "%c23"
        "%c24" "%c25" "%c26" "%c27" "%c28" "%c29" "%c30" "%c31" ]
#line 415 "sparc.nw"
                                                                       ]
#line 502 "sparc.nw"
fieldinfo a is [ names [ "" ",a" ] ]
#line 67 "sparc.nw"
patterns
 [ TABLE_F2 CALL TABLE_F3 TABLE_F4 ] is op  = {0 to 3}
#line 76 "sparc.nw"
patterns
 [ UNIMP Bicc SETHI FBfcc CBccc ] is TABLE_F2 & op2 = [0 2 4 6 7]
 NOP                              is SETHI & rd = 0 & imm22 = 0
#line 90 "sparc.nw"
patterns
 [ ADD  ADDcc  TADDcc   WRxxx
   AND  ANDcc  TSUBcc   WRPSR
   OR   ORcc   TADDccTV WRWIM
   XOR  XORcc  TSUBccTV WRTBR
   SUB  SUBcc  MULScc   FPop1
   ANDN ANDNcc SLL      FPop2
   ORN  ORNcc  SRL      CPop1
   XNOR XNORcc SRA      CPop2
   ADDX ADDXcc RDxxx    JMPL
   _    _      RDPSR    RETT
   UMUL UMULcc RDWIM    Ticc
   SMUL SMULcc RDTBR    FLUSH
   SUBX SUBXcc _        SAVE
   _    _      _        RESTORE
   UDIV UDIVcc _        _
   SDIV SDIVcc _        _       ] is TABLE_F3 & op3 = {0 to 63 columns 4}
#line 117 "sparc.nw"
patterns
  WRASR          is WRxxx & rd != 0   # should be rdi != 0
  WRY            is WRxxx & rd = 0
  RDASR          is RDxxx & rs1 != 0  # should be rs1i != 0
  RDY            is RDxxx & rs1 = 0
  STBAR          is RDxxx & rs1 = 15 & rd = 0
#line 142 "sparc.nw"
patterns
 [ LD     LDA     LDF   LDC
   LDUB   LDUBA   LDFSR LDCSR
   LDUH   LDUHA   _ _
   LDD    LDDA    LDDF  LDDC
   ST     STA     STF   STC
   STB    STBA    STFSR STCSR
   STH    STHA    STDFQ STDCQ
   STD    STDA    STDF  STDC
   _      _       _     _
   LDSB   LDSBA   _     _
   LDSH   LDSHA   _     _
   _      _       _     _
   _      _       _     _
   LDSTUB LDSTUBA _     _
   _      _       _     _
   SWAP.  SWAPA   _     _  ]  is TABLE_F4 & op3 = {0 to 63 columns 4}
#line 172 "sparc.nw"
patterns
  float2 is any of [ FMOVs FNEGs FABSs FSQRTs FSQRTd FSQRTq
                     FiTOs FdTOs FqTOs FiTOd  FsTOd  FqTOd
                     FiTOq FsTOq FdTOq FsTOi  FdTOi  FqTOi ],
  which is FPop1 & opf =  
                   [ 0x1   0x5   0x9   0x29   0x2a   0x2b
                     0xc4  0xc6  0xc7  0xc8   0xc9   0xcb
                     0xcc  0xcd  0xce  0xd1   0xd2   0xd3 ]
  float2s is FMOVs | FNEGs | FABSs | FSQRTs
  FTOs    is FiTOs | FsTOi
  FTOd    is FiTOd | FsTOd 
  FTOq    is FiTOq | FsTOq 
  FdTO    is FdTOi | FdTOs 
  FqTO    is FqTOs | FqTOi

  float3 is any of [ FADDs FADDd FADDq FSUBs FSUBd FSUBq  FMULs
                     FMULd FMULq FDIVs FDIVd FDIVq FsMULd FdMULq ],
    which is FPop1 & opf =
                   [ 0x41  0x42  0x43  0x45  0x46  0x47   0x49
                     0x4a  0x4b  0x4d  0x4e  0x4f  0x69   0x6e ]
  float3s is  FADDs | FSUBs | FMULs | FDIVs
  float3d is  FADDd | FSUBd | FMULd | FDIVd
  float3q is  FADDq | FSUBq | FMULq | FDIVq
#line 223 "sparc.nw"
patterns
 fcompares is any of      [ FCMPs FCMPEs ],
   which is FPop2 & opf = [ 0x51  0x55 ]
 fcompared is any of      [ FCMPd FCMPEd ],
   which is FPop2 & opf = [ 0x52  0x56 ]
 fcompareq is any of      [ FCMPq FCMPEq ],
   which is FPop2 & opf = [ 0x53  0x57 ]
#line 241 "sparc.nw"
patterns
  ibranch is any of [ BN BE  BLE BL  BLEU BCS BNEG BVS
                      BA BNE BG  BGE BGU  BCC BPOS BVC ],
    which is Bicc & cond = {0 to 15}

  fbranch is any of [ FBN FBNE FBLG FBUL FBL   FBUG FBG   FBU
                      FBA FBE  FBUE FBGE FBUGE FBLE FBULE FBO ],
    which is FBfcc & cond = {0 to 15}

  cbranch is any of [ CBN CB123 CB12 CB13 CB1   CB23 CB2   CB3
                      CBA CB0   CB03 CB02 CB023 CB01 CB013 CB012 ],
    which is CBccc & cond = {0 to 15}

  trap is any of    [ TN TE  TLE TL  TLEU TCS TNEG TVS
                      TA TNE TG  TGE TGU  TCC TPOS TVC ],
    which is Ticc & cond = {0 to 15}

  branch is ibranch | fbranch | cbranch
#line 292 "sparc.nw"
constructors
  imode simm13! : reg_or_imm  is  i = 1 & simm13
  rmode rs2     : reg_or_imm  is  i = 0 & rs2
#line 313 "sparc.nw"
constructors
  generalA  rs1 + reg_or_imm : address_
  dispA     rs1 + simm13!    : address_  is  generalA(rs1, imode(simm13!))
  absoluteA simm13!          : address_  is  generalA(0,   imode(simm13!))
  indexA    rs1 + rs2        : address_  is  generalA(rs1, rmode(rs2))
  indirectA rs1              : address_  is  generalA(rs1, rmode(0))
#line 332 "sparc.nw"
patterns 
  loadg  is LDSB  | LDSH  | LDUB  | LDUH  | LD  | LDSTUB  | SWAP.
  loada  is LDSBA | LDSHA | LDUBA | LDUHA | LDA | LDSTUBA | SWAPA
  storeg is STB   | STH  | ST 
  storea is STBA  | STHA | STA
#line 351 "sparc.nw"
constructors
  loadg  [address_], rd
  LDD    [address_], rd    # { rd = 2 * _ }
  LDF    [address_], fd
  LDDF   [address_], fd    # { fd = 2 * _ }
  LDC    [address_], cd
  LDDC   [address_], cd    # { cd = 2 * _ }

  storeg rd, [address_]
  STD    rd, [address_]    # { rd = 2 * _ }
  STF    fd, [address_]
  STDF   fd, [address_]    # { fd = 2 * _ }
  STC    cd, [address_]
  STDC   cd, [address_]    # { cd = 2 * _ }
#line 384 "sparc.nw"
constructors
  indexR    rs1 + rs2     : regaddr  is  i = 0 & rs1 & rs2
  indirectR rs1           : regaddr  is  i = 0 & rs2 = 0 & rs1

  loada  [regaddr]asi, rd
  LDDA   [regaddr]asi, rd # { rd = 2 * _ }
  storea rd, [regaddr]asi
  STDA   rd, [regaddr]asi # { rd = 2 * _ }
#line 424 "sparc.nw"
constructors
  LDFSR  [address_], "%fsr"
  LDCSR  [address_], "%csr"
  STFSR  "%fsr", [address_]
  STCSR  "%csr", [address_]
  STDFQ  "%fq",  [address_]
  STDCQ  "%cq",  [address_]
#line 438 "sparc.nw"
constructors
  RDY    "%y",   rd
  RDPSR  "%psr", rd
  RDWIM  "%wim", rd
  RDTBR  "%tbr", rd
  WRY    rs1, reg_or_imm, "%y"
  WRPSR  rs1, reg_or_imm, "%psr"
  WRWIM  rs1, reg_or_imm, "%wim"
  WRTBR  rs1, reg_or_imm, "%tbr"
#line 451 "sparc.nw"
constructors
  RDASR   "%asr"rs1i, rd
  WRASR   rs1, reg_or_imm, "%asr"rdi
  STBAR
#line 470 "sparc.nw"
patterns 
  logical is AND | ANDcc | ANDN | ANDNcc | OR | ORcc | ORN | ORNcc |
             XOR | XORcc | XNOR | XNORcc
  shift   is SLL | SRL   | SRA
  arith   is ADD | ADDcc | ADDX | ADDXcc | TADDcc | TADDccTV |
             SUB | SUBcc | SUBX | SUBXcc | TSUBcc | TSUBccTV |
             MULScc | UMUL | SMUL | UMULcc | SMULcc |
             UDIV | SDIV | UDIVcc | SDIVcc |
             SAVE | RESTORE
  alu     is logical | shift | arith

constructors
  alu rs1, reg_or_imm, rd
#line 493 "sparc.nw"
placeholder for instruction is UNIMP & imm22 = 0xbad
#line 505 "sparc.nw"
relocatable reloc
constructors
  branch^a reloc  { reloc = L + 4 * disp22! } is L: branch & a & disp22
#line 522 "sparc.nw"
constructors
  call  reloc   { reloc = L + 4 * disp30! } is L: CALL & disp30
#line 539 "sparc.nw"
constructors
  float2s fs2, fd 
  FSQRTd  fs2, fd # { fs2 = 2 * _, fd = 2 * _ }
  FSQRTq  fs2, fd # { fs2 = 4 * _, fd = 4 * _ }

  FTOs fs2, fd
  FTOd fs2, fd  # { fd = 2 * _ }
  FTOq fs2, fd  # { fd = 4 * _ }
  FdTO fs2, fd  # { fs2 = 2 * _ }
  FqTO fs2, fd  # { fs2 = 4 * _ }
  FqTOd fs2, fd  # { fs2 = 4 * _, fd = 2 * _ }
  FdTOq fs2, fd  # { fs2 = 2 * _, fd = 4 * _ }

  float3s  fs1, fs2, fd
  float3d  fs1, fs2, fd # { fs1 = 2 * _, fs2 = 2 * _, fd = 2 * _ }
  float3q  fs1, fs2, fd # { fs1 = 4 * _, fs2 = 4 * _, fd = 4 * _ }
  FsMULd   fs1, fs2, fd # { fd = 4 * _ }
  FdMULq   fs1, fs2, fd # { fs1 = 2 * _, fs2 = 2 * _, fd = 4 * _ }

  fcompares fs1, fs2
  fcompared fs1, fs2 # { fs1 = 2 * _, fs2 = 2 * _ }
  fcompareq fs1, fs2 # { fs1 = 4 * _, fs2 = 4 * _ }
#line 565 "sparc.nw"
constructors
  NOP
  FLUSH address_
  JMPL  address_, rd
  RETT  address_
  trap  address_
  UNIMP imm22
#line 585 "sparc.nw"
constructors
  sethi        "%hi("val")", rd                   is  SETHI & rd & imm22 = val@[10:31]
  decode_sethi "%hi("val")", rd { val@[0:9] = 0 } is  SETHI & rd & imm22 = val@[10:31]
