#line 1333 "pentium.nw"
constructors
  
#line 923 "pentium.nw"
FCLEX            is  WAIT; FCLEX
#line 1007 "pentium.nw"
FSAVE  Mem  is WAIT; FNSAVE(Mem)
#line 1025 "pentium.nw"
FNSTCW        Mem  is  WAIT; FSTCW(Mem)
#line 1031 "pentium.nw"
FNSTENV       Mem  is  WAIT; FSTENV(Mem)
#line 1038 "pentium.nw"
FNSTSW        Mem  is  WAIT; FSTSW(Mem)
FNSTSW.AX          is  WAIT; FSTSW.AX()
#line 1062 "pentium.nw"
FWAIT is WAIT
