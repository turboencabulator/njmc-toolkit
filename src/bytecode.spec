#line 8 "expbc.nw"
fields of op (8)
  op3 0:2 lit5 3:7
  op4 3   lit4 4:7
  op6 4:5 lit2 6:7
  op7 6   lit1 7
  op8 7

fields of lit (8) lit8 0:7

#line 23 "expbc.nw"
# operators for 0..31
patterns 
  u5 is any of [ narrows_lit narrowu_lit loslice ], which is op3 = [0 1 2]
#line 39 "expbc.nw"
# operators for -8..7  --- can have at most 13
patterns
  s4 is any of [ intlit addlit emitlocplus bitshiftlit ], 
  which is op3 = [3 4] & op4 = [0 1] 
#line 52 "expbc.nw"
# operators for 1 2 4 8
patterns emit_at_loc is op3 = 5 & op4 = 0 & op6 = 0
#line 62 "expbc.nw"
# operators for 1..2
patterns lit1.2 is any of [ cla_force_lit clv_lit clv_orb_lit ], 
which is op3 = 5 & op4 = 0 & op6 = [1 2 3] & op7 = 0
#line 74 "expbc.nw"
# raw operations
patterns
  [ 
    sint8 sint16 sint32 
  ] is op3 = 5 & op4 = 0 & op6 = [1 2 3] & op7 = 1
  [ mark array set procmark proc stringlit null uint64
  ] is op3 = 5 & op4 = 1 & op6 = [0 1 2 3] & op7 = [0 1]
  [
    bitslice bitshift narrowu narrows widen fitsu fitss failmsg 
    lt le gt ge ne eq false true
    orb and not add sub mul idiv mod
    cl_loc cla clv force known emit_at if_guard neg
  ] is op3 = [6 7] & op4 = [0 1] & op6 = [0 1 2 3] & op7 = [0 1]

patterns
  nullary is mark | array | set | procmark | proc | stringlit | null 
           | lt | le | gt | ge | ne | eq | false | true
           | orb | and | not | add | sub | mul | idiv | mod
           | cl_loc | force | known | if_guard | neg | failmsg
  unary is emit_at | widen | fitsu | fitss
#line 95 "expbc.nw"
constructors
  nullary
  sint n!
     when {lit4! = n} is intlit & lit4
     when {lit8! = n} is sint8;  lit8
     when {lit8! = n@[8:31]!}  is sint16; lit8 = n@[0:7]; lit8
     when {lit8! = n@[24:31]!} is sint32; lit8 = n@[0:7]; lit8 = n@[8:15];
			                  lit8 = n@[16:23]; lit8
  unary n!  is sint(n); unary  
#line 19 "expbc.nw"
constructors
  
#line 27 "expbc.nw"
  narrows n!
     when {n != 0} is narrows_lit & lit5 = n
     otherwise is sint(n); narrows
  halt  is narrows_lit & lit5 = 0
  narrowu n!
     when {n != 0}   is narrowu_lit & lit5 = n
     otherwise is sint(n); narrowu
  unsat is narrowu_lit & lit5 = 0
  bitslice lo! hi! 
     when {lo = 0, lit5 = hi}  is  loslice & lit5
     when {}           is sint(lo); sint(hi); bitslice  # lo <= hi fails!
#line 44 "expbc.nw"
addlit n!  when {n != 0, lit4! = n}   is addlit & lit4
           otherwise is sint(n); add
cl_loc_force  is addlit & lit4 = 0
#  emitlocplus n   when {lit4! = n} is emitlocplus & lit4
#                  otherwise is cl_loc; force; sint(n); add; emit_at
bitshift n!  when {lit4! = n} is bitshiftlit & lit4
               otherwise is sint(n); bitshift
#line 55 "expbc.nw"
emit_at_loc n
  when {n = 1} is emit_at_loc & lit2 = 0
  when {n = 2} is emit_at_loc & lit2 = 1
  when {n = 4} is emit_at_loc & lit2 = 2
  when {n = 8} is emit_at_loc & lit2 = 3
  otherwise    is cl_loc; force; sint(n); emit_at
#line 66 "expbc.nw"
cla n          is sint(n); cla
cla_force n    when {} is  cla_force_lit & lit1 = n-1
               otherwise is sint(n); cla; force
clv       n    when { n <= 2 } is  clv_lit & lit1 = n-1  # condition shouldn't be needed
               otherwise is sint(n); clv
clv_orb     n  when {} is  clv_orb_lit & lit1 = n-1
               otherwise is sint(n); clv; orb

