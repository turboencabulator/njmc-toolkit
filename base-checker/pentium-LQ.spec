#line 282 "../specs/pentium.nw"
fields of opcodet (8) row 4:7 col 0:2 page 3:3
                     
#line 317 "../specs/pentium.nw"
r32 0:2
#line 322 "../specs/pentium.nw"
sr16 0:2
#line 327 "../specs/pentium.nw"
r16 0:2
#line 386 "../specs/pentium.nw"
r8 0:2
#line 319 "../specs/pentium.nw"
fieldinfo r32 is [names [ eAX eCX eDX eBX eSP eBP eSI eDI ]]
#line 324 "../specs/pentium.nw"
fieldinfo sr16 is [sparse [ cs=1, ss=2, ds=3, es=4, fs=5, gs=6 ] ]
#line 329 "../specs/pentium.nw"
fieldinfo r16 is [names [ AX CX DX BX SP BP SI DI ]]
#line 388 "../specs/pentium.nw"
fieldinfo r8 is [names [ AL CL DL BL AH CH DH BH ]]
#line 485 "../specs/pentium.nw"
fields of modrm (8) mod 6:7 reg_opcode 3:5 r_m 0:2
fields of sib   (8) ss 6:7 index 3:5 base 0:2
#line 488 "../specs/pentium.nw"
fieldinfo [ base index ] is 
          [ names [ eAX eCX eDX eBX eSP eBP eSI eDI ] ]
fieldinfo ss is [ sparse [ "1" = 0, "2" = 1, "4" = 2, "8" = 3 ] ]
#line 572 "../specs/pentium.nw"
fields of I8   (8) i8  0:7
fields of I16 (16) i16 0:15
fields of I32 (32) i32 0:31
#line 1838 "../specs/pentium.nw"
patterns 
#line 293 "../specs/pentium.nw"
arith is any of [ ADD OR
                  ADC SBB
                  AND SUB
                  XOR CMP ], which is row = {0 to 3} & page = [0 1]
[ Eb.Gb Ev.Gv Gb.Eb Gv.Ev AL.Ib eAX.Iv ] is col = {0 to 5}
#line 301 "../specs/pentium.nw"
[ PUSH.ES POP.ES    PUSH.CS esc2
  PUSH.SS POP.SS    PUSH.DS POP.DS
  SEG.ES  DAA	    SEG.CS  DAS
  SEG.SS  AAA       SEG.DS  AAS   ] is row = {0 to 3} & page = [0 1] & col = [6 7]
#line 313 "../specs/pentium.nw"
regops is any of [ INC  DEC 
                   PUSH POP ], which is row = [4 5] & page = [0 1]
#line 335 "../specs/pentium.nw"
[ PUSHA   POPA    BOUND   ARPL    SEG.FS  SEF.GS   OpPrefix AddrPrefix 
  PUSH.Iv IMUL.Iv PUSH.Ib IMUL.Ib INSB    INSv     OUTSB    OUTSv      
] is page = [0 1] & row = 6 & col = {0 to 7} 
#line 344 "../specs/pentium.nw"
Jb is row = 7
cond is any of [ .O .NO .B .NB .Z .NZ .BE .NBE .S .NS .P .NP .L .NL .LE .NLE ], 
      which is page = [0 1] & col = {0 to 7}
#line 356 "../specs/pentium.nw"
[ Eb.Ib Ev.Iv MOVB Ev.Ib TEST.Eb.Gb TEST.Ev.Gv  XCHG.Eb.Gb XCHG.Ev.Gv ] is
               row = 8 & page = 0 & col = {0 to 7}
MOV is row = 8 & page = 1
[ MOV.Ew.Sw LEA MOV.Sw.Ew POP.Ev ] is row = 8 & page = 1 & col = {4 to 7}
#line 366 "../specs/pentium.nw"
XCHG is row = 9 & page = 0
NOP is XCHG & col = 0
[ CBW CWDQ CALL.aP WAIT PUSHF POPF SAHF LAHF ] is row = 9 & page = 1 & col = {0 to 7}
#line 375 "../specs/pentium.nw"
[ MOV.AL.Ob  MOV.eAX.Ov  MOV.Ob.AL  MOV.Ov.eAX MOVSB    MOVSv     CMPSB   CMPSv
  TEST.AL.Ib TEST.eAX.Iv STOSB      STOSv      LODSB    LODSv     SCASB   SCASv
] is row = 10 & page = [0 1] & col = {0 to 7} 
#line 383 "../specs/pentium.nw"
MOVib is row = 11 & page = 0
MOViv is row = 11 & page = 1
#line 393 "../specs/pentium.nw"
[ B.Eb.Ib B.Ev.Ib RET.Iw  RET     LES LDS MOV.Eb.Ib MOV.Ev.Iv      	
  B.Eb.1  B.Ev.1  B.Eb.CL B.Ev.CL AAM AAD _         XLAT
]   is row = [12 13] & page = 0 & col = {0 to 7}
[ ENTER LEAVE RET.far.Iw RET.far INT3 INT.Ib INTO IRET ]
    is row = 12      & page = 1 & col = {0 to 7}
ESC is row = 13      & page = 1
#line 403 "../specs/pentium.nw"
[ LOOPNE  LOOPE   LOOP    JCXZ    IN.AL.Ib  IN.eAX.Ib  OUT.Ib.AL OUT.Ib.eAX
  LOCK    _       REPNE   REP     HLT       CMC        grp3.Eb   grp3.Ev

  CALL.Jv JMP.Jv  JMP.Ap  JMP.Jb  IN.AL.DX  IN.eAX.DX  OUT.DX.AL OUT.DX.eAX
  CLC     STC     CLI     STI     CLD       STD        grp4      grp5       
] is page = [0 1] & row = [14 15] & col = {0 to 7}
#line 420 "../specs/pentium.nw"
[ grp6       grp7       LAR        LSL       
  MOV.Eb.Gb  MOV.Gv.Ev  MOV.Gb.Eb  MOV.Ev.Gv ]
is esc2; page = 0 & row = [0 1] & col = {0 to 3}
CLTS is esc2; page = 0 & row = 0 & col = 6
#line 427 "../specs/pentium.nw"
[ MOV.Rd.Cd  MOV.Rd.Dd  MOV.Cd.Rd  MOV.Dd.Rd  MOV.Rd.Td _  MOV.Td.Rd ]
is esc2; page = 0 & row = 3 & col = {0 to 6}
#line 432 "../specs/pentium.nw"
[ WRMSR RDTSC RDMSR ] is esc2; page = 0 & row = 4 & col = {0 to 2}
#line 438 "../specs/pentium.nw"
Jv   is esc2; row = 8
SETb is esc2; row = 9
#line 443 "../specs/pentium.nw"
[ PUSH.FS       POP.FS        CPUID  BT   SHLD.Ib SHLD.CL _            _
  CMPXCHG.Eb.Gb CMPXCHG.Ev.Gv LSS    BTR  LFS     LGS     MOVZX.Gv.Eb  MOVZX.Gv.Ew ]
is esc2; page = 0 & row = [10 11] & col = {0 to 7}
#line 449 "../specs/pentium.nw"
[ XADD.Eb.Gb XADD.Ev.Gv grp9 ] is esc2; page = 0 & row = 12 & col = [0 1 7]
#line 454 "../specs/pentium.nw"
[INVD WBINVD] is esc2; row = 0 & page = 1 & col = [0 1]
#line 459 "../specs/pentium.nw"
[ PUSH.GS POP.GS RSM  BTS   SHRD.Ib SHRD.CL _ IMUL.Gv.Ev] 
is esc2; row = 10 & page = 1 & col = {0 to 7}
#line 464 "../specs/pentium.nw"
[ grp8 BTC BSF BSR MOVSX.Gv.Eb MOVSX.Gv.Ew] 
is esc2; page = 1 & row = 11 & col = {2 to 7}
#line 469 "../specs/pentium.nw"
BSWAP is esc2; row = 12 & page = 1
#line 653 "../specs/pentium.nw"
patterns
  arithI    is any of [ ADDi ORi ADCi SBBi ANDi SUBi XORi CMPi ], 	# group 1
		       which is (Eb.Ib | Ev.Iv | Ev.Ib); reg_opcode = {0 to 7} ...
  bshifts   is B.Eb.1  | B.Eb.CL # D0 D2
  vshifts   is B.Ev.1  | B.Ev.CL # D1 D3
  immshifts is B.Eb.Ib | B.Ev.Ib # C0 C1
  rot       is any of [ ROL ROR RCL RCR SHLSAL SHR _ SAR], 
                       which is (bshifts | vshifts | immshifts); 
                                                         reg_opcode = {0 to 7} ...
  grp3ops   is any of 
      [ TEST.Ib.Iv _ NOT NEG MUL.AL.eAX IMUL.AL.eAX DIV.AL.eAX IDIV.AL.eAX ],
		       which is (grp3.Eb | grp3.Ev); reg_opcode = {0 to 7} ...
  grp4ops   is any of [ INC.Eb DEC.Eb ], 
                       which is grp4; reg_opcode = [0 1] ...
  grp5ops   is any of [ INC.Ev DEC.Ev CALL.Ev CALL.Ep JMP.Ev JMP.Ep PUSH.Ev _ ], 
		       which is grp5; reg_opcode = {0 to 7} ...
  grp6ops   is any of [ SLDT STR LLDT LTR VERR VERW _ _ ], 
		       which is grp6; reg_opcode = {0 to 7} ...
  grp7ops   is any of [ SGDT SIDT LGDT LIDT SMSW _ LMSW INVLPG ], 
		       which is grp7; reg_opcode = {0 to 7} ...
  bittestI  is any of [ BTi BTSi BTRi BTCi ], 
                       which is grp8; reg_opcode = {4 to 7} ...
  CMPXCHG8B is                  grp9; reg_opcode = 1 ...
#line 720 "../specs/pentium.nw"
patterns
  [ D8 D9 DA DB DC DD DE DF ] is ESC & col = {0 to 7}
  [ FADD FMUL FCOM FCOMP FSUB FSUBR FDIV FDIVR ] is reg_opcode = {0 to 7}
  [ FLD _ FST FSTP FLDENV FLDCW FSTENV FSTCW ]   is reg_opcode = {0 to 7} ...
  [ FNOP ]                         is D9; mod = 3 & reg_opcode = 2 & r_m = [0]
  [ FCHS FABS _ _ FTST FXAM _ _  ] is D9; mod = 3 & reg_opcode = 4 & r_m = {0 to 7}
  [ F2XM1 FYL2X FPTAN FPATAN FXTRACT FPREM1 FDECSTP FINCSTP ] 
                                   is D9; mod = 3 & reg_opcode = 6 & r_m = {0 to 7}
  FXCH                             is D9; mod = 3 & reg_opcode = 1
  Fconstants is any of [ FLD1 FLDL2T FLDL2E FLDPI FLDLG2 FLDLN2 FLDZ _ ], which
                                   is D9; mod = 3 & reg_opcode = 5 & r_m = {0 to 7}
  [ FPREM FYL2XP1 FSQRT FSINCOS FRNDINT FSCALE FSIN FCOS ]
                                   is D9; mod = 3 & reg_opcode = 7 & r_m = {0 to 7}
  [ FIADD FIMUL FICOM FICOMP FISUB FISUBR FIDIV FIDIVR ] is reg_opcode = {0 to 7} ...
  FUCOMPP                          is DA; mod = 3 & reg_opcode = 5 & r_m = 1
  [ FILD _ FIST FISTP FBLD FLD.ext FBSTP FSTP.ext ] is reg_opcode = {0 to 7} ...
  [ FCLEX FINIT ]                  is DB; mod = 3 & reg_opcode = 4 & r_m = [2 3]
  [ FRSTOR _ FSAVE FSTSW ]          is reg_opcode = {4 to 7} ... 
  [ FFREE _ FST.st FSTP.st FUCOM FUCOMP  _ _ ]  is mod = 3 & reg_opcode = {0 to 7}
  [ FADDP _ FUBSRP FDIVRP FMULP _ FSUBP FDIVP ] is mod = 3 & reg_opcode = {0 to 7}
  FCOMPP    is DE; mod = 3 & reg_opcode = 3 & r_m = 1
  FSTSW.AX  is DF; mod = 3 & reg_opcode = 4 & r_m = 0
#line 746 "../specs/pentium.nw"
patterns
  .STi      is DD; mod = 3
  Fstack is any of [ .ST.STi .STi.St P.STi.ST ], which is [ D8 DC DE ]; mod = 3
  Fint   is any of [.I32 .I16], which is [DA DE]
  Fmem   is any of [.R32 .R64], which is [D8 DC]
  FlsI   is any of [.lsI16 .lsI32], which is [DF DB]
  FlsR   is any of [.lsR32 .lsR64], which is [D9 DD]
#line 927 "../specs/pentium.nw"
   patterns FCOMs is FCOM | FCOMP
#line 955 "../specs/pentium.nw"
   patterns FISTs is FIST | FISTP
#line 1015 "../specs/pentium.nw"
   patterns
FSTs is FST | FSTP
FSTs.st is FST.st | FSTP.st
#line 1054 "../specs/pentium.nw"
   patterns FUCOMs is FUCOM | FUCOMP
#line 1134 "../specs/pentium.nw"
   patterns lfp is LDS | LES | LFS | LGS | LSS
#line 1148 "../specs/pentium.nw"
    patterns LOOPs is LOOP | LOOPE | LOOPNE
#line 1216 "../specs/pentium.nw"
   patterns POPs is POP.ES | POP.SS | POP.DS | POP.FS | POP.GS 
            POPv is POPA | POPF
#line 1228 "../specs/pentium.nw"
   patterns PUSHs is PUSH.CS | PUSH.SS | PUSH.DS | PUSH.ES | PUSH.FS | PUSH.GS
            PUSHv is PUSHA | PUSHF
#line 1270 "../specs/pentium.nw"
  patterns shdIb is SHRD.Ib | SHLD.Ib
           shdCL is SHRD.CL | SHLD.CL
#line 697 "../specs/pentium.nw"
patterns ow is OpPrefix
         od is epsilon
         ov is ow | od
#line 704 "../specs/pentium.nw"
patterns aw is AddrPrefix
         ad is epsilon
         av is aw | ad
#line 285 "../specs/pentium.nw"
placeholder for opcodet is HLT
#line 493 "../specs/pentium.nw"
placeholder for modrm is HLT
placeholder for sib is HLT
#line 576 "../specs/pentium.nw"
placeholder for I8  is HLT
placeholder for I16 is HLT; HLT
placeholder for I32 is HLT; HLT; HLT; HLT
#line 839 "../specs/pentium.nw"
constructors
  rel8  reloc : Rel8  { reloc = L + i8!  } is i8;  L: epsilon
  rel16 reloc : Rel16 { reloc = L + i16! } is i16; L: epsilon
  rel32 reloc : Rel32 { reloc = L + i32! } is i32; L: epsilon
#line 514 "../specs/pentium.nw"
relocatable d a
constructors
  Indir    [reg] : Mem { reg != 4, reg != 5 } is mod = 0 & r_m = reg
  Disp8   d[reg] : Mem { reg != 4 }           is mod = 1 & r_m = reg; i8  = d
  Disp32  d[reg] : Mem { reg != 4 }           is mod = 2 & r_m = reg; i32 = d
  Abs32    [a]   : Mem                        is mod = 0 & r_m = 5;   i32 = a
  Reg     reg    : Eaddr                      is mod = 3 & r_m = reg
  Index    [base][index * ss] : Mem { index != 4, base != 5 } is 
                        mod = 0 & r_m = 4; index & base     & ss
  Index8  d[base][index * ss] : Mem { index != 4 } is 
                        mod = 1 & r_m = 4; index & base     & ss; i8  = d
  Index32 d[base][index * ss] : Mem { index != 4 } is 
                        mod = 2 & r_m = 4; index & base     & ss; i32 = d
  ShortIndex    d[index * ss] : Mem { index != 4 } is 
                        mod = 0 & r_m = 4; index & base = 5 & ss; i32 = d
  E Mem : Eaddr is Mem
#line 1131 "../specs/pentium.nw"
LAHF
LAR^ov  reg, Eaddr  is  ov; LAR; Eaddr & reg_opcode = reg ...
#line 1150 "../specs/pentium.nw"
    constructors
LOOPs^ov  reloc  is  ov; LOOPs; rel8(reloc)
LSL^ov  reg, Eaddr  is  ov; LSL; Eaddr & reg_opcode = reg ...
LTR  Eaddr  is  (grp6; Eaddr) & LTR
#line 1157 "../specs/pentium.nw"
MOV^"mrb"    Eaddr, reg    is      MOV & Eb.Gb; Eaddr & reg_opcode = reg ...
MOV^"mr"^ov  Eaddr, reg    is  ov; MOV & Ev.Gv; Eaddr & reg_opcode = reg ...
MOV^"rmb"    reg, Eaddr    is      MOV & Gb.Eb; Eaddr & reg_opcode = reg ...
MOV^"rm"^ov  reg, Eaddr    is  ov; MOV & Gv.Ev; Eaddr & reg_opcode = reg ...
MOV.Ew.Sw    Mem, sr16     is  ow; MOV.Ew.Sw;   Mem   & reg_opcode = sr16 ...
MOV.Sw.Ew    Mem, sr16     is      MOV.Sw.Ew;   Mem   & reg_opcode = sr16 ...
# assume 32-bit address mode
MOV.AL.Ob      offset      is      MOV.AL.Ob;  i32 = offset
MOV.eAX.Ov^ov  offset      is  ov; MOV.eAX.Ov; i32 = offset
MOV.Ob.AL      offset      is      MOV.Ob.AL;  i32 = offset
MOV.Ov.eAX^ov  offset      is  ov; MOV.Ov.eAX; i32 = offset
MOVib          r8,  i8!    is      MOVib & r8; i8
MOViw          r16, i16!   is  ow; MOViv & r16; i16
MOVid          r32, i32!   is  od; MOViv & r32; i32
MOV.Eb.Ib      Eaddr, i8!  is      MOV.Eb.Ib; Eaddr & reg_opcode = 0 ...; i8
MOV.Ev.Iv^ow   Eaddr, i16! is  ow; MOV.Ev.Iv; Eaddr & reg_opcode = 0 ...; i16
MOV.Ev.Iv^od   Eaddr, i32! is  od; MOV.Ev.Iv; Eaddr & reg_opcode = 0 ...; i32
MOV.Cd.Rd      cr, reg     is  MOV.Cd.Rd; mod = 3 & r_m = reg & reg_opcode = cr
MOV.Rd.Cd      reg, cr     is  MOV.Rd.Cd; mod = 3 & r_m = reg & reg_opcode = cr
MOV.Dd.Rd      dr, reg     is  MOV.Dd.Rd; mod = 3 & r_m = reg & reg_opcode = dr
MOV.Rd.Dd      reg, dr     is  MOV.Rd.Dd; mod = 3 & r_m = reg & reg_opcode = dr
MOVSB
MOVSv^ov is ov; MOVSv
MOVSX.Gv.Eb^ov    r32, Eaddr    is ov; MOVSX.Gv.Eb; Eaddr & reg_opcode = r32 ...
MOVSX.Gv.Ew       r16, Eaddr    is     MOVSX.Gv.Ew; Eaddr & reg_opcode = r16 ...
MOVZX.Gv.Eb^ov    r32, Eaddr    is ov; MOVZX.Gv.Eb; Eaddr & reg_opcode = r32 ...
MOVZX.Gv.Ew       r16, Eaddr    is     MOVZX.Gv.Ew; Eaddr & reg_opcode = r16 ...
MUL.AL      Eaddr  is      (grp3.Eb; Eaddr) & MUL.AL.eAX
MUL.AX^ov   Eaddr  is  ov; (grp3.Ev; Eaddr) & MUL.AL.eAX
#line 1195 "../specs/pentium.nw"
NEGb    Eaddr  is      (grp3.Eb; Eaddr) & NEG
NEG^ov  Eaddr  is  ov; (grp3.Ev; Eaddr) & NEG
NOP
NOTb    Eaddr  is      (grp3.Eb; Eaddr) & NOT
NOT^ov  Eaddr  is  ov; (grp3.Ev; Eaddr) & NOT
#line 1203 "../specs/pentium.nw"
# OR is in the arith group
OUT.Ib.AL       i8! is      OUT.Ib.AL;  i8
OUT.Ib.eAX^ov   i8! is  ov; OUT.Ib.eAX; i8
OUT.DX.AL
OUT.DX.eAX^ov       is  ov; OUT.DX.eAX
OUTSB
OUTSv^ov is ov; OUTSv
#line 1213 "../specs/pentium.nw"
POP.Ev^ov   Mem   is  ov; POP.Ev; Mem & reg_opcode = 0 ...
POP^ov      r32   is  ov; POP & r32
#line 1219 "../specs/pentium.nw"
   constructors
POPs
POPv^ov  is  ov; POPv
PUSH.Ev^ov  Eaddr  is  ov; (grp5; Eaddr) & PUSH.Ev
PUSH^ov     r32    is  ov; PUSH & r32
PUSH.Ib     i8!    is      PUSH.Ib; i8
PUSH.Iv^ow  i16!   is  ow; PUSH.Iv; i16
PUSH.Iv^od  i32!   is  od; PUSH.Iv; i32
#line 1231 "../specs/pentium.nw"
   constructors
PUSHs
PUSHv^ov  is  ov; PUSHv
