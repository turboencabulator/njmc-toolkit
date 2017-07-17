#line 756 "../specs/sparc.nw"
assembly component
  decode_{*}             is $1
  {LDF,LDFSR,LDC,LDCSR}  is LD
  {LDDF,LDDC}            is LDD
  {STF,STFSR,STC,STCSR}  is ST
  {STDF,STDFQ,STDC,STDCQ} is STD
  {RDY,RDASR,RDPSR,RDWIM,RDTBR} is RD
  {WRY,WRASR,WRPSR,WRWIM,WRTBR} is WR
  {not,neg}2             is $1
  {set,ld,st,mov}r       is $1
  {ld2,st2}f             is $1	
  {call}a                is $1
  SWAP.                  is SWAP
  {*}{_,__}              is $1
  _{*}                   is $1
#line 774 "../specs/sparc.nw"
assembly syntax
  absoluteA "%g0 + " simm13!
