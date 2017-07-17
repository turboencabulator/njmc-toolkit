#line 302 "alpha.nw"
constructors
  andnot ra, rb, rc          is  bic(ra, rmode(rb), rc)
  clr    rc                  is  bis(r31, rmode(r31), rc)
  mov    reg_or_imm, rc      is  bis(r31, reg_or_imm, rc)
  nop                        is  bis(r31, rmode(r31), r31)
  not    rb, rc              is  ornot(r31, rmode(rb), rc)
  or     ra, reg_or_imm, rc  is  bis(ra, reg_or_imm, rc)
