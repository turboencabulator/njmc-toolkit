#define sign_extend(N,SIZE) (((int)((N) << (sizeof(unsigned)*8-(SIZE)))) >> (sizeof(unsigned)*8-(SIZE)))
#include <assert.h>
{ 
  dword MATCH_p = 
    
    #line 1 "tests/sret.m"
    lc
    
    ;
  unsigned MATCH_w_32_0;
  { 
    MATCH_w_32_0 = getDword(MATCH_p); 
    if ((MATCH_w_32_0 & 0xffffffff) 
            /* op*rd*op3*rs1*i*simm13 at 0 */ == 0x81C7E008) { 
      nextPC = 4 + MATCH_p; 
      
      #line 2 "tests/sret.m"
      
              lc = nextPC;
              return true;
      
      
      
    } /*opt-block*//*opt-block+*/
    else { 
      nextPC = MATCH_p; 
      
      #line 5 "tests/sret.m"
      
              return false;
      
      
      
    } /*opt-block*//*opt-block+*/
    
  }goto MATCH_finished_a; 
  
  MATCH_finished_a: (void)0; /*placeholder for label*/
  
}
