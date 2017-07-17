#line 1327 "pentium.nw"
constructors
  
#line 919 "pentium.nw"
FCLEX            is  WAIT; FCLEX
#line 1003 "pentium.nw"
FSAVE  Mem  is WAIT; FNSAVE(Mem)
#line 1021 "pentium.nw"
FNSTCW        Mem  is  WAIT; FSTCW(Mem)
#line 1027 "pentium.nw"
FNSTENV       Mem  is  WAIT; FSTENV(Mem)
#line 1034 "pentium.nw"
FNSTSW        Mem  is  WAIT; FSTSW(Mem)
FNSTSW.AX          is  WAIT; FSTSW.AX()
#line 1058 "pentium.nw"
FWAIT is WAIT
