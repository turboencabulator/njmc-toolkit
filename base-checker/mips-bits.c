#include <mclib.h>
#include <assert.h>
#include <stdio.h>
void emitbits(val, n) unsigned long val; unsigned n; {
  switch (n) {
  case sizeof(unsigned char):  
    printf("\t.byte 0x%01x\n", (unsigned char)val); break; 
  case sizeof(unsigned short): 
    printf("\t.half 0x%04x\n", (unsigned short)val); break; 
  case sizeof(unsigned):       
    printf("\t.word 0x%08x\n", val); break; 
  default: assert(0);
  }  
  addlc(n);
}
  
