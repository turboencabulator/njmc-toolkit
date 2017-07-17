#line 22 "alpha.nw"
fields of instruction (32) 
#line 55 "alpha.nw"
opcode_ 26:31   ra 21:25 rb 16:20 sbz 13:15 opfmt 12:12 func 5:11   rc 0:4
                         imm 13:20
                fa 21:25 fb 16:20 fpfunc 5:15                       fc 0:4
                                  mdisp 0:15 
                                  mop 14:15 mhint 0:13 
                         bdisp 0:20
                palfunc 0:25
                    
#line 77 "alpha.nw"
flo 5:8 fhi 9:11 fplo 5:10 fphi 11:15
#line 82 "alpha.nw"
fieldinfo
  [ ra rb rc ] is [ 
#line 86 "alpha.nw"
names [ r0  r1  r2  r3  r4  r5  r6  r7
        r8  r9  r10 r11 r12 r13 r14 r15
        r16 r17 r18 r19 r20 r21 r22 r23
        r24 r25 r26 r27 r28 r29 r30 r31 ]
#line 83 "alpha.nw"
                                                              ]
  [ fa fb fc ] is [ 
#line 91 "alpha.nw"
names [ f0  f1  f2  f3  f4  f5  f6  f7
        f8  f9  f10 f11 f12 f13 f14 f15
        f16 f17 f18 f19 f20 f21 f22 f23
        f24 f25 f26 f27 f28 f29 f30 f31 ]
#line 84 "alpha.nw"
                                                            ]
#line 288 "alpha.nw"
fieldinfo palfunc is 
  [ sparse 
    [ halt = 0, draina = 2, cserve = 0xa, swppal = 0xb,
      bpt = 0x80, bugchk = 0x81, imb = 0x86,
      rdunique = 0x9e, wrunique = 0x9f, gentrap = 0xaa ] ]
#line 100 "alpha.nw"
patterns 
  [ call_pal  _      _     _      _    _      _     _
    lda       ldah   _     ldq_u  _    _      _     stq_u
    inta      intl   ints  intm   _    fltv   flti  fltl
    misc      pal19  jsrs  pal1b  _    pal1d  pal1e pal1f
    ldf       ldg    lds   ldt    stf  stg    sts   stt
    ldl       ldq    ldl_l ldq_l  stl  stq    stl_c stq_c
    br        fbeq   fblt  fble   bsr  fbne   fbge  fbgt
    blbc      beq    blt   ble    blbs bne    bge   bgt  ] 
  is opcode_ = { 0 to 63 }
#line 114 "alpha.nw"
patterns
  ldst    is lda | ldah | ldl | ldq | ldq_u | ldl_l | ldq_l 
                        | stl | stq | stl_c | stq_c | stq_u 
  fldst   is ldf | ldg | lds | ldt | stf | stg | sts | stt  
  branch  is br | bsr | blbc | beq | blt | ble | blbs | bne | bge | bgt
  fbranch is fbeq | fblt | fble | fbne | fbge | fbgt
  [ jmp jsr ret jsr_co ] is jsrs & mop = {0 to 3} 
  jump_hint    is jmp | jsr
  jump_predict is ret | jsr_co
#line 129 "alpha.nw"
patterns
  arith is any of 
    [ addl   s4addl subl   s4subl _      cmpbge 
      _      s8addl _      s8subl cmpult _ 
      addq   s4addq subq   s4subq cmpeq  _
      _      s8addq _      s8subq cmpule _ 
      addlv  _      sublv  _      cmplt  _ 
      addqv  _      subqv  _      cmple  _  ], 
  which is opcode_ = 0x10 & 
	   fhi = [ 0 1 2 3 4 6 ] & flo = [ 0x0 0x2 0x9 0xb 0xd 0xf ]

  logical is any of 
    [ and _       _       bic 
      _   cmovlbs cmovlbc _ 
      bis cmoveq  cmovne  ornot 
      xor cmovlt  cmovge  eqv 
      _   cmovle  cmovgt  _ ], 
  which is opcode_ = 0x11 & 
           fhi = [ 0 1 2 4 6 ] & flo = [ 0x0 0x4 0x6 0x8 ] 

  byteops is any of
    [ _   _      mskbl _    extbl  _     _   _     insbl _ 
      _   _      mskwl _    extwl  _     _   _     inswl _ 
      _   _      mskll _    extll  _     _   _     insll _ 
      zap zapnot mskql srl  extql  _     sll _   insql sra 
      _   _      mskwh _    _      inswh _   extwh _     _ 
      _   _      msklh _    _      inslh _   extlh _     _ 
      _   _      mskqh _    _      insqh _   extqh _     _  ], 
  which is opcode_ = 0x12 & 
           fhi = [ 0 1 2 3 5 6 7 ] & flo = [ 0 1 2 4 6 7 9 10 11 12 ]
 
  mulops is any of [ mull mullv mulq mulqv umulh ], 
    which is intm & func = [ 0x00 0x40 0x20 0x60 0x30 ]
#line 172 "alpha.nw"
constructors
  imode imm : reg_or_imm  is  opfmt = 1 & imm
  rmode rb  : reg_or_imm  is  opfmt = 0 & sbz = 0 & rb 
#line 179 "alpha.nw"
constructors
  ldst  ra, mdisp!(rb)
#line 199 "alpha.nw"
relocatable target
placeholder for instruction is call_pal & palfunc = 0  # halt (privileged)
constructors
  branch ra, target { target = L + 4 * bdisp! } is branch & ra & bdisp; L: epsilon
  jump_hint ra, (rb), mhint 
  proc    "0" : Return is mhint = 0
  nonproc "1" : Return is mhint = 1
  jump_predict ra, (rb), Return
#line 209 "alpha.nw"
constructors
  jump_hint^"*" ra, (rb), target { target = L + 4 * mhint } 
	is  L: jump_hint & ra & rb & mhint
#line 217 "alpha.nw"
patterns alu is arith | logical | byteops | mulops 
constructors
  alu ra, reg_or_imm, rc 
#line 237 "alpha.nw"
patterns           [ adds addt cmpteq cmptlt cmptle cmptun 
                     cvtqs cvtqt cvtts divs divt muls mult subs subt cvttq ] 
  is flti & fplo = [ 0x00 0x20 0x25 0x26 0x27 0x24
                     0x3c 0x3e 0x2c 0x03 0x23 0x02 0x22 0x01 0x21 0x2f ]
  fpqual is any of
  [ none c m d u uc um ud 
    su suc sum sud sui suic suim suid ], 
  which is flti & fphi = [ 0x02 0x00 0x01 0x03 0x06 0x04 0x05 0x07
                           0x16 0x14 0x15 0x17 0x1e 0x1c 0x1d 0x1f ]
#line 249 "alpha.nw"
patterns
  cmpqual is none | su
  cvtqual is none | c | m | d | sui | suic | suim | suid
  fpop  is adds | addt | divs | divt | muls | mult | subs | subt
  cmpop is cmpteq | cmptlt | cmptle | cmptun
  cvtop is cvtqs | cvtqt
  qqqual is any of [ qq qqc qqm qqd v vc vm vd 
                     sv svc svm svd svi svic svim svid ],
  which is flti & fphi = [ 0x02 0x00 0x01 0x03 0x06 0x04 0x05 0x07
                           0x16 0x14 0x15 0x17 0x1e 0x1c 0x1d 0x1f ]
#line 267 "alpha.nw"
constructors
  fldst         fa, mdisp(rb)
  fbranch       fa, target { target = L + 4 * bdisp! } 
			is fbranch & fa & bdisp; L: epsilon
#line 274 "alpha.nw"
constructors
  fpop^fpqual    fa, fb, fc
  cvtts^fpqual       fb, fc
  cvtop^cvtqual      fb, fc
  cmpop^cmpqual  fa, fb, fc
  cvttq^qqqual       fb, fc 
#line 294 "alpha.nw"
constructors 
 call_pal palfunc 
