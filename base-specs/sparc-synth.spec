#line 271 "sparc.nw"
patterns
  B    is BA
  BGEU is BCC
  BLU  is BCS
  BNZ  is BNE
  branch.synonyms is B | BGEU | BLU | BNZ
#line 604 "sparc.nw"
constructors
  jmp address          is JMPL (address, "%g0")
  calla address        is JMPL (address, "%o7")
  tst  rs2              is ORcc ("%g0", rmode(rs2), "%g0")
  ret                   is JMPL (dispA("%i7",8), "%g0")
  retl                  is JMPL (dispA("%o7",8), "%g0")
  restore_              is RESTORE ("%g0", rmode("%g0"), "%g0")
  save_                 is SAVE("%g0", rmode("%g0"), "%g0")
  not   rd              is XNOR(rd,    rmode("%g0"), rd)
  not2  rs1, rd         is XNOR(rs1,   rmode("%g0"), rd)
  neg   rd              is SUB ("%g0", rmode(rd),    rd)
  neg2  rs2, rd         is SUB ("%g0", rmode(rs2),   rd)
  inc   val, rd         is ADD (rd, imode(val), rd)
  inccc val, rd         is ADDcc (rd, imode(val), rd)
  dec   val, rd         is SUB (rd, imode(val), rd)
  deccc val, rd       	is SUBcc (rd, imode(val), rd)
  cmp rs1, reg_or_imm   is SUBcc(rs1, reg_or_imm, "%g0")   # must follow dec
  btst reg_or_imm, rs1  is ANDcc(rs1, reg_or_imm, "%g0")
  bset reg_or_imm, rd   is OR  (rd, reg_or_imm, rd)
  bclr reg_or_imm, rd   is ANDN(rd, reg_or_imm, rd)
  btog reg_or_imm, rd   is XOR (rd, reg_or_imm, rd)
  mov  reg_or_imm, rd   is OR  ("%g0", reg_or_imm, rd)
  movr rs2, rd          is OR  ("%g0", rmode(rs2),   rd)
  clr  rd               is OR  ("%g0", rmode("%g0"), rd)
  clrw [address]       is ST  ("%g0", address)
  clrb [address]       is STB ("%g0", address)
  clrh [address]      	is STH ("%g0", address)
#line 649 "sparc.nw"
constructors
  set val, rd  
    when { val@[0:9] = 0 }  is  sethi(val, rd)
    otherwise               is  OR("%g0", imode(val), rd)
    otherwise               is  sethi(val, rd); OR(rd, imode(val@[0:9]), rd)
