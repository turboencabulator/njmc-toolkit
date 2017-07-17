#line 54 "../specs/pentium.nw"
keep 
#line 534 "../specs/pentium.nw"
Indir Disp32 Reg Index Index32 E
#line 779 "../specs/pentium.nw"
arith^"iEAX" arithI^"d" arith^"mr"^od arith^"rm"^od
#line 808 "../specs/pentium.nw"
AAA AAD AAM AAS
#line 833 "../specs/pentium.nw"
BOUND^od BSF^od BSR^od BSWAP BT^od BTi^od BTC^od BTCi^od BTR^od BTRi^od BTS^od BTSi^od
#line 844 "../specs/pentium.nw"
rel32
#line 876 "../specs/pentium.nw"
CALL.Jv^od CALL.Ep^od CALL.Ev^od CALL.aP^od CBW CWDE CLC CLD CLI CLTS CMC
CMPSv^od^av CMPXCHG.Ev.Gv^od CWD CDQ
#line 893 "../specs/pentium.nw"
DAA DAS DEC.Ev^od DEC^od DIV^"eAX"
#line 900 "../specs/pentium.nw"
ENTER F2XM1
#line 1085 "../specs/pentium.nw"
HLT
#line 1112 "../specs/pentium.nw"
IDIV^"eAX" IMUL^od IMULrm^od IMUL.Iv^"d" IN.eAX.DX^od INC.Ev^od INC^od 
INSv^od INT3 INT.Ib INTO INVD INVLPG IRET
#line 1127 "../specs/pentium.nw"
Jv^cond^od JMP.Jv^od JMP.Ap^od JMP.Ev^od JMP.Ep^od
#line 1155 "../specs/pentium.nw"
LAHF LAR^ov lfp^ov LEA^ov LEAVE LGDT LIDT LLDT LMSW LOCK LODSB LODSv^ov 
#line 1187 "../specs/pentium.nw"
MOV^"mrb" MOV^"mr"^ov MOV^"rmb" MOV^"rm"^ov
MOV.Ew.Sw MOV.Sw.Ew MOV.AL.Ob MOV.eAX.Ov^ov MOV.Ob.AL
MOV.Ov.eAX^ov MOVib MOViw MOVid MOV.Eb.Ib MOV.Ev.Iv^ow
MOV.Ev.Iv^od MOVSB MOVSv^ov MOVSX.Gv.Eb^od
MOVSX.Gv.Ew MOVZX.Gv.Eb^od MOVZX.Gv.Ew MUL.AL MUL.AX^ov 
#line 1201 "../specs/pentium.nw"
NEGb NEG^ov NOP NOTb NOT^ov
#line 1211 "../specs/pentium.nw"
OUT.Ib.AL OUT.Ib.eAX^ov OUT.DX.AL OUT.DX.eAX^ov OUTSB OUTSv^ov
#line 1235 "../specs/pentium.nw"
POPs POPv^ov  PUSH.Ev^ov PUSH^ov PUSH.Ib PUSH.Iv^ow PUSH.Iv^od PUSHs PUSHv^ov  
#line 1243 "../specs/pentium.nw"
rot^bshifts rot^vshifts^ov rot^B.Ev.Ib^ov
#line 1254 "../specs/pentium.nw"
RDMSR REP REPNE RET RET.far RET.Iw RET.far.Iw RSM
#line 1268 "../specs/pentium.nw"
SCASB SCASv^ov SETb^cond SGDT SIDT
#line 1286 "../specs/pentium.nw"
shdIb^ov shdCL^ov SLDT SMSW STC STD STI STOSB STOSv^ov STR
#line 1297 "../specs/pentium.nw"
TEST.AL.Ib TEST.eAX.Iv^ow TEST.eAX.Iv^od TEST.Eb.Ib TEST.Ew.Iw
TEST.Ed.Id TEST.Eb.Gb TEST.Ev.Gv^ov
#line 1303 "../specs/pentium.nw"
VERR VERW
#line 1309 "../specs/pentium.nw"
WAIT WBINVD WRMSR
#line 1321 "../specs/pentium.nw"
XADD.Eb.Gb XADD.Ev.Gv^ov XCHG^"eAX"^ov XCHG.Eb.Gb XCHG.Ev.Gv^ov XLATB 
#line 54 "../specs/pentium.nw"
                             
#line 913 "../specs/pentium.nw"
FABS FADD^Fmem FADD^Fstack
#line 921 "../specs/pentium.nw"
FCHS
#line 935 "../specs/pentium.nw"
FCOMs^Fmem FCOMs^.ST.STi FCOMPP FCOS
#line 945 "../specs/pentium.nw"
FDECSTP FDIV^Fmem FDIV^Fstack FDIVR^Fmem FDIVR^Fstack  
#line 961 "../specs/pentium.nw"
FICOM^Fint FICOMP^Fint FICOM16 FICOM32 FICOMP16 FICOMP32 
FILD^FlsI FILD64 FINIT FISTs^FlsI FISTP64
#line 982 "../specs/pentium.nw"
FLD^FlsR FLD80 FLD.STi Fconstants FLDCW FLDENV 
#line 987 "../specs/pentium.nw"
FMUL^Fmem FMUL^Fstack
#line 991 "../specs/pentium.nw"
FNOP
#line 998 "../specs/pentium.nw"
FPATAN FPREM FPREM1 FPTAN
#line 1027 "../specs/pentium.nw"
FSCALE FSIN FSINCOS FSQRT FSTs^FlsR FSTP80 FSTs.st^.STi FSTCW FNSTCW
#line 1033 "../specs/pentium.nw"
FSTENV FNSTENV
#line 1041 "../specs/pentium.nw"
FSTSW FSTSW.AX FNSTSW FNSTSW.AX
#line 1048 "../specs/pentium.nw"
FSUB^Fmem FSUB^Fstack FSUBR^Fmem FSUBR^Fstack  
#line 1052 "../specs/pentium.nw"
FTST
#line 1060 "../specs/pentium.nw"
FUCOMs FUCOMPP
#line 1064 "../specs/pentium.nw"
FWAIT
#line 1070 "../specs/pentium.nw"
FXAM FXCH FXTRACT
#line 1075 "../specs/pentium.nw"
FYL2X FYL2XP1
#line 864 "../specs/pentium.nw"
discard CALL.aP^ow CALL.aP^od
#line 937 "../specs/pentium.nw"
discard FCOMs^.ST.STi
#line 1129 "../specs/pentium.nw"
discard JMP.Ap^ow  JMP.Ap^ov 
#line 1193 "../specs/pentium.nw"
discard  MOVSX.Gv.Ew MOVZX.Gv.Eb^ov MOVZX.Gv.Ew MOV.Ew.Sw
#line 1256 "../specs/pentium.nw"
discard RDMSR
#line 1311 "../specs/pentium.nw"
discard WRMSR
#line 1875 "../specs/pentium.nw"
discard 
rot^B.Eb.1 rot^B.Ev.CL ROL^B.Eb.Ib RCL^B.Eb.Ib
SHLSAL^B.Eb.Ib SAR^B.Eb.Ib ROR^B.Ev.Ib^ov 
RCR^B.Ev.Ib^ov SHR^B.Ev.Ib^ov
