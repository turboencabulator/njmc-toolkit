#define sign_extend(N,SIZE) (((int)((N) << (sizeof(unsigned)*8-(SIZE)))) >> (sizeof(unsigned)*8-(SIZE)))
#include <assert.h>

#line 2 "../../../toolkit/www/examples/xs/xs.m"
#line 243 "xs.nw"
#include <stdio.h>
#include <stdlib.h>
#line 36 "xs.nw"
typedef struct machine {
  unsigned MEM[1024];
  unsigned AC, XR, PC;
  unsigned PCHI:1;
} *Machine;
#line 48 "xs.nw"
#define validate(A) ((A) & 0x3ff)
#line 72 "xs.nw"
#define setPC(M, A)  (((M)->PC = validate(A)), ((M)->PCHI = 0))
#define advancePC(M) ((M)->PCHI ? setPC(M, (M)->PC+1) : ((M)->PCHI = 1))
#define getPC(A)     ((A)->PC)
#line 173 "xs.nw"
#define FETCH16(A) ((A)->PCHI ? (A)->MEM[(A)->PC] >> 16 : (A)->MEM[(A)->PC] & 0xffff)
#line 87 "xs.nw"
unsigned address(Machine M) {


#line 20 "../../../toolkit/www/examples/xs/xs.m"
{ 
  Machine MATCH_p = 
    
    #line 20 "../../../toolkit/www/examples/xs/xs.m"
    M
    ;
  unsigned /* [0..65535] */ MATCH_w_16_0;
  { 
    MATCH_w_16_0 = FETCH16(MATCH_p); 
    
      switch((MATCH_w_16_0 >> 10 & 0x3) /* md at 0 */) {
        case 0: 
          { 
            unsigned adr = (MATCH_w_16_0 & 0x3ff) /* adr at 0 */;
            
            #line 21 "../../../toolkit/www/examples/xs/xs.m"
             return adr;

            
            
            
          }
          
          break;
        case 1: 
          { 
            unsigned adr = (MATCH_w_16_0 & 0x3ff) /* adr at 0 */;
            
            #line 22 "../../../toolkit/www/examples/xs/xs.m"
             return adr + M->XR;

            
            
            
          }
          
          break;
        case 2: 
          { 
            unsigned adr = (MATCH_w_16_0 & 0x3ff) /* adr at 0 */;
            
            #line 23 "../../../toolkit/www/examples/xs/xs.m"
             return adr + M->XR++;

            
            
            
          }
          
          break;
        case 3: 
          { 
            unsigned adr = (MATCH_w_16_0 & 0x3ff) /* adr at 0 */;
            
            #line 24 "../../../toolkit/www/examples/xs/xs.m"
             return adr + --M->XR;

            
            
            
          }
          
          break;
        default: assert(0);
      } /* (MATCH_w_16_0 >> 10 & 0x3) -- md at 0 --*/ 
    
  }goto MATCH_finished_h; 
  
  MATCH_finished_h: (void)0; /*placeholder for label*/
  
}

#line 27 "../../../toolkit/www/examples/xs/xs.m"
}
#line 121 "xs.nw"
static void show_inst(Machine m);

void interpretXS(Machine m, unsigned start_address) {
  unsigned trace = 0;
  unsigned branch;
#define MEMORY(a) (m->MEM[validate(address(a))])
#define BRANCH(a) (setPC(m, validate(address(a))), branch = 1)
  for (setPC(m, validate(start_address)); ; branch ? 0 : advancePC(m)) {
    if (trace) show_inst(m);
    branch = 0;


#line 38 "../../../toolkit/www/examples/xs/xs.m"
{ 
  Machine MATCH_p = 
    
    #line 38 "../../../toolkit/www/examples/xs/xs.m"
    m
    ;
  unsigned /* [0..65535] */ MATCH_w_16_0;
  { 
    MATCH_w_16_0 = FETCH16(MATCH_p); 
    
      switch((MATCH_w_16_0 >> 12 & 0xf) /* op at 0 */) {
        case 0: 
          if (11 <= (MATCH_w_16_0 & 0x3ff) /* adr at 0 */ && 
            (MATCH_w_16_0 & 0x3ff) /* adr at 0 */ < 1024) 
            
            #line 50 "../../../toolkit/www/examples/xs/xs.m"
             assert(("invalid instruction", 0));

            
             /*opt-block+*/
          else 
            switch((MATCH_w_16_0 & 0x3ff) /* adr at 0 */) {
              case 0: 
                
                #line 39 "../../../toolkit/www/examples/xs/xs.m"
                 return;

                
                
                
                break;
              case 1: 
                
                #line 40 "../../../toolkit/www/examples/xs/xs.m"
                 m->AC = - m->AC;

                
                
                
                break;
              case 2: 
                
                #line 41 "../../../toolkit/www/examples/xs/xs.m"
                 m->AC = ~ m->AC;

                
                
                
                break;
              case 3: 
                
                #line 42 "../../../toolkit/www/examples/xs/xs.m"
                 m->AC <<= 1;

                
                
                
                break;
              case 4: 
                
                #line 43 "../../../toolkit/www/examples/xs/xs.m"
                 m->AC >>= 1;

                
                
                
                break;
              case 5: 
                
                #line 44 "../../../toolkit/www/examples/xs/xs.m"
                 m->AC = getchar();

                
                
                
                break;
              case 6: 
                
                #line 45 "../../../toolkit/www/examples/xs/xs.m"
                 putchar(m->AC);

                
                
                
                break;
              case 7: 
                
                #line 46 "../../../toolkit/www/examples/xs/xs.m"
                 putchar('\n');

                
                
                
                break;
              case 8: 
                
                #line 47 "../../../toolkit/www/examples/xs/xs.m"
                 /* do nothing */;

                
                
                
                break;
              case 9: 
                
                #line 48 "../../../toolkit/www/examples/xs/xs.m"
                 trace = 1;

                
                
                
                break;
              case 10: 
                
                #line 49 "../../../toolkit/www/examples/xs/xs.m"
                 trace = 0;

                
                
                
                break;
              default: assert(0);
            } /* (MATCH_w_16_0 & 0x3ff) -- adr at 0 --*/ 
          break;
        case 1: 
          { 
            unsigned a = getPC(MATCH_p);
            
            #line 51 "../../../toolkit/www/examples/xs/xs.m"
             m->AC = address(m);

            
            
            
          }
          
          break;
        case 2: 
          { 
            unsigned a = getPC(MATCH_p);
            
            #line 52 "../../../toolkit/www/examples/xs/xs.m"
             m->AC = MEMORY(m);

            
            
            
          }
          
          break;
        case 3: 
          { 
            unsigned a = getPC(MATCH_p);
            
            #line 53 "../../../toolkit/www/examples/xs/xs.m"
             MEMORY(m) = m->AC;

            
            
            
          }
          
          break;
        case 4: 
          { 
            unsigned a = getPC(MATCH_p);
            
            #line 54 "../../../toolkit/www/examples/xs/xs.m"
             m->XR = MEMORY(m);

            
            
            
          }
          
          break;
        case 5: 
          { 
            unsigned a = getPC(MATCH_p);
            
            #line 55 "../../../toolkit/www/examples/xs/xs.m"
             MEMORY(m) = m->XR;

            
            
            
          }
          
          break;
        case 6: 
          { 
            unsigned a = getPC(MATCH_p);
            
            #line 56 "../../../toolkit/www/examples/xs/xs.m"
             m->AC += MEMORY(m);

            
            
            
          }
          
          break;
        case 7: 
          { 
            unsigned a = getPC(MATCH_p);
            
            #line 57 "../../../toolkit/www/examples/xs/xs.m"
             m->AC -= MEMORY(m);

            
            
            
          }
          
          break;
        case 8: 
          { 
            unsigned a = getPC(MATCH_p);
            
            #line 58 "../../../toolkit/www/examples/xs/xs.m"
             m->AC |= MEMORY(m);

            
            
            
          }
          
          break;
        case 9: 
          { 
            unsigned a = getPC(MATCH_p);
            
            #line 59 "../../../toolkit/www/examples/xs/xs.m"
             m->AC &= MEMORY(m);

            
            
            
          }
          
          break;
        case 10: 
          { 
            unsigned a = getPC(MATCH_p);
            
            #line 60 "../../../toolkit/www/examples/xs/xs.m"
             MEMORY(m)++;

            
            
            
          }
          
          break;
        case 11: 
          { 
            unsigned a = getPC(MATCH_p);
            
            #line 61 "../../../toolkit/www/examples/xs/xs.m"
             MEMORY(m)--;

            
            
            
          }
          
          break;
        case 12: 
          { 
            unsigned a = getPC(MATCH_p);
            
            #line 62 "../../../toolkit/www/examples/xs/xs.m"
             BRANCH(m);

            
            
            
          }
          
          break;
        case 13: 
          { 
            unsigned a = getPC(MATCH_p);
            
            #line 63 "../../../toolkit/www/examples/xs/xs.m"
             if (m->AC == 0) then BRANCH(m);

            
            
            
          }
          
          break;
        case 14: 
          { 
            unsigned a = getPC(MATCH_p);
            
            #line 64 "../../../toolkit/www/examples/xs/xs.m"
             if (m->AC <  0) then BRANCH(m);

            
            
            
          }
          
          break;
        case 15: 
          { 
            unsigned a = getPC(MATCH_p);
            
            #line 65 "../../../toolkit/www/examples/xs/xs.m"
             m->XR = m->PC; BRANCH(m);

            
            
            
          }
          
          break;
        default: assert(0);
      } /* (MATCH_w_16_0 >> 12 & 0xf) -- op at 0 --*/ 
    
  }goto MATCH_finished_g; 
  
  MATCH_finished_g: (void)0; /*placeholder for label*/
  
}

#line 68 "../../../toolkit/www/examples/xs/xs.m"
  }
}
#line 177 "xs.nw"
static char *adrstring(Machine m);

static void show_inst(Machine m) {
  fprintf(stderr, "%03x%s : ", m->PC, m->PCHI ? "'" : " ");


#line 74 "../../../toolkit/www/examples/xs/xs.m"
{ 
  Machine MATCH_p = 
    
    #line 74 "../../../toolkit/www/examples/xs/xs.m"
    m
    ;
  char *MATCH_name;
  static char *MATCH_name_adr_0[] = {
    "HALT", "NEG", "COM", "SHL", "SHR", "READ", "WRT", "NEWL", "NOOP", "TRA", 
    "NOTR", 
  };
  static char *MATCH_name_op_1[] = {
    (char *)0, "LIT", "LDA", "STA", "LDX", "STX", "ADD", "SUB", "OR", "AND", 
    "INC", "DEC", "JMP", "JPZ", "JPN", "JSR", 
  };
  unsigned /* [0..65535] */ MATCH_w_16_0;
  { 
    MATCH_w_16_0 = FETCH16(MATCH_p); 
    if ((MATCH_w_16_0 >> 12 & 0xf) /* op at 0 */ == 0) 
      if (11 <= (MATCH_w_16_0 & 0x3ff) /* adr at 0 */ && 
        (MATCH_w_16_0 & 0x3ff) /* adr at 0 */ < 1024) 
        
        #line 76 "../../../toolkit/www/examples/xs/xs.m"
         fprintf(stderr, "INVALID [%08x]", m->MEM[validate(m->PC)]);

        
         /*opt-block+*/
      else { 
        MATCH_name = MATCH_name_adr_0[(MATCH_w_16_0 & 0x3ff) /* adr at 0 */]; 
        { 
          char *name = MATCH_name;
          
          #line 75 "../../../toolkit/www/examples/xs/xs.m"
           fprintf(stderr, "%s", name);

          
          
          
        }
        
      } /*opt-block*/ /*opt-block+*/
    else { 
      MATCH_name = MATCH_name_op_1[(MATCH_w_16_0 >> 12 & 0xf) /* op at 0 */]; 
      { 
        char *name = MATCH_name;
        unsigned a = getPC(MATCH_p);
        
        #line 77 "../../../toolkit/www/examples/xs/xs.m"
         fprintf(stderr, "%s %s", name, adrstring(m));

        
        
        
      }
      
    } /*opt-block*/
    
  }goto MATCH_finished_f; 
  
  MATCH_finished_f: (void)0; /*placeholder for label*/
  
}

#line 80 "../../../toolkit/www/examples/xs/xs.m"
  fprintf(stderr, "  (AC=%08x, XR=%08x)\n", m->AC, m->XR);
}

static char *adrstring(Machine m) {
  static char buf[100];


#line 84 "../../../toolkit/www/examples/xs/xs.m"
{ 
  Machine MATCH_p = 
    
    #line 84 "../../../toolkit/www/examples/xs/xs.m"
    m
    ;
  unsigned /* [0..65535] */ MATCH_w_16_0;
  { 
    MATCH_w_16_0 = FETCH16(MATCH_p); 
    
      switch((MATCH_w_16_0 >> 10 & 0x3) /* md at 0 */) {
        case 0: 
          { 
            unsigned adr = (MATCH_w_16_0 & 0x3ff) /* adr at 0 */;
            
            #line 85 "../../../toolkit/www/examples/xs/xs.m"
             sprintf(buf, "%08x", adr);

            
            
            
          }
          
          break;
        case 1: 
          { 
            unsigned adr = (MATCH_w_16_0 & 0x3ff) /* adr at 0 */;
            
            #line 86 "../../../toolkit/www/examples/xs/xs.m"
             sprintf(buf, "XR#%08x", adr);

            
            
            
          }
          
          break;
        case 2: 
          { 
            unsigned adr = (MATCH_w_16_0 & 0x3ff) /* adr at 0 */;
            
            #line 87 "../../../toolkit/www/examples/xs/xs.m"
             sprintf(buf, "XR+%08x", adr);

            
            
            
          }
          
          break;
        case 3: 
          { 
            unsigned adr = (MATCH_w_16_0 & 0x3ff) /* adr at 0 */;
            
            #line 88 "../../../toolkit/www/examples/xs/xs.m"
             sprintf(buf, "XR-%08x", adr);

            
            
            
          }
          
          break;
        default: assert(0);
      } /* (MATCH_w_16_0 >> 10 & 0x3) -- md at 0 --*/ 
    
  }goto MATCH_finished_e; 
  
  MATCH_finished_e: (void)0; /*placeholder for label*/
  
}

#line 91 "../../../toolkit/www/examples/xs/xs.m"
  return buf;
}
#line 218 "xs.nw"
static unsigned getword(FILE *fp);
void load_and_goXS(Machine m, FILE *loadfile) {
  unsigned LA, N, START;  
  unsigned i;
  LA = getword(loadfile);
  N  = getword(loadfile);
  for (i = 0; i < N; i++)
    m->MEM[validate(LA+i)] = getword(loadfile);
  START = getword(loadfile);
  interpretXS(m, START);
}
#line 231 "xs.nw"
static unsigned getword(FILE *fp) {
  unsigned u;
  u = 0;
  u |= ((unsigned char) getc(fp)) <<  0;
  u |= ((unsigned char) getc(fp)) <<  8;
  u |= ((unsigned char) getc(fp)) << 16;
  u |= ((unsigned char) getc(fp)) << 24;
  return u;
}

#line 253 "xs.nw"
main(int argc, char *argv[]) {
  FILE *loadfile;
  Machine m;
  
#line 265 "xs.nw"
if (argc != 2) {
  fprintf(stderr, "Usage: %s loadfile\n", argv[0]);
  exit(1);
}
#line 257 "xs.nw"
  loadfile = fopen(argv[1], "r");
  
#line 270 "xs.nw"
if (loadfile == NULL) {
  fprintf(stderr, "%s: Could not open file %s for read\n", argv[0], argv[1]);
  exit(1);
}
#line 259 "xs.nw"
  m = (Machine) malloc(sizeof(*m));
  assert(m);
  load_and_go(m, loadfile);
}


