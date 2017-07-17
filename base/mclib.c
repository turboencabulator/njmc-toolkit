#line 1053 "mclib.nw"
#include <mclib.h>
#include <stdio.h> 

#define max(X,Y) ((X) > (Y) ? (X) : (Y))
#define min(X,Y) ((X) < (Y) ? (X) : (Y))
#define roundup(X,N) (((X)+((N)-1))&(~((N)-1)))


static void mcfail(char *fmt, ...) { 
  assert(("application didn't set fail", 0));  /* apps should provide their own */
}
void (*fail)(char *fmt, ...) = &mcfail;

#define BUFSZ 1024

#line 193 "mclib.nw"
static unsigned char bogus_buffer[MARGIN];
#line 334 "mclib.nw"
static void initial_cl_emitm(RBlock rb, unsigned lc, unsigned long bits, unsigned size);
#line 436 "mclib.nw"
static void initial_emitm(unsigned long bits, unsigned size);
#line 673 "mclib.nw"
struct reloc_block undefrblock;
#line 783 "mclib.nw"
static Buffer buffer_at_lc(RBlock rb, unsigned start);
#line 838 "mclib.nw"
static unsigned long initial_block_fetchm(RBlock rb, unsigned lc, unsigned size);
#line 964 "mclib.nw"
static void fail_if_undef(void *, RAddr);
#line 1020 "mclib.nw"
static void label_print(struct label *label);
#line 98 "reloc.nw"
static void reloc_print(RAddr addr);
#line 168 "mclib.nw"
void make_clean() {
  if (currb) {
    unsigned curlc = lc();
    currb->p = currb_p;
    if (currb->size < curlc) currb->size = curlc;
  }
}
#line 179 "mclib.nw"
void set_block(rb) RBlock rb; {
  make_clean();
  currb = rb;
  currb_p = currb->p;
  currb_safe = currb->curbuf->limit - MARGIN;
}
#line 199 "mclib.nw"
RBlock currb = (RBlock) 0;
unsigned char *currb_p, *currb_safe;
#line 225 "mclib.nw"
void emitl(val, n) unsigned long val; unsigned n; {
  if (currb_p <= currb_safe || currb_p + n <= currb->curbuf->limit) {
    register unsigned char *p = currb_p;
    
#line 235 "mclib.nw"
switch (n) {
  #define BYTE(N) case N+1: p[N] = val >> 8*N; /* fall through */
  BYTE(7) BYTE(6) BYTE(5) BYTE(4) BYTE(3) BYTE(2) BYTE(1) BYTE(0)
  #undef BYTE
  case 0: /* do nothing */
    break;
  default: assert(("unsigned long bigger than 8 bytes", 0));
}
#line 229 "mclib.nw"
    currb_p = p + n;
  } else {
    
#line 392 "mclib.nw"
if (!currb->curbuf->next) {
  int curbufsize = (currb->curbuf->limit - currb->curbuf->data);
  int minsize = 32 + (currb_p - currb->curbuf->data) - curbufsize;
  int size = roundup(max(minsize, currb->size_hint), 8);
  Buffer b = (Buffer) mc_alloc(roundup(sizeof(*b), 8) + size, RBlock_data_pool);

  b->data = (unsigned char *)(b) + roundup(sizeof(*b), 8);
  b->limit = b->data + size;
  b->next = (Buffer)0;
  b->datalc = currb->curbuf->datalc + curbufsize;
  currb->curbuf->next = b;
  currb->size_hint = BUFSZ;
}
#line 291 "mclib.nw"
{ unsigned roomhere = 
        currb_p < currb->curbuf->limit ? currb->curbuf->limit - currb_p : 0;
  if (roomhere > 0) emitl(val, roomhere);
  
#line 315 "mclib.nw"
{ unsigned templc = lc();
  currb->curbuf = currb->curbuf->next;
  currb_safe = currb->curbuf->limit - MARGIN;
  currb_p = templc - currb->curbuf->datalc + currb->curbuf->data;
}
#line 295 "mclib.nw"
  emitl(val >> 8*roomhere, n - roomhere);
}
#line 232 "mclib.nw"
  }
}
#line 255 "mclib.nw"
void emitb(val, n) unsigned long val; unsigned n; {
  if (currb_p <= currb_safe || currb_p + n <= currb->curbuf->limit) {
    register unsigned char *p = currb_p;
    
#line 265 "mclib.nw"
switch (n) {
  #define S(POS, N) (p[POS] = val >> 8*N)
  case 0: break;
  case 1: S(0,0); break;
  case 2: S(0,1); S(1,0); break;
  case 3: S(0,2); S(1,1); S(2,0); break;
  case 4: S(0,3); S(1,2); S(2,1); S(3,0); break;
  case 5: S(0,4); S(1,3); S(2,2); S(3,1); S(4,0); break;
  case 6: S(0,5); S(1,4); S(2,3); S(3,2); S(4,1); S(5,0); break;
  case 7: S(0,6); S(1,5); S(2,4); S(3,3); S(4,2); S(5,1); S(6,0); break;
  case 8: S(0,7); S(1,6); S(2,5); S(3,4); S(4,3); S(5,2); S(6,1); S(7,0); break;
  default: assert(("unsigned long bigger than 8 bytes", 0));
}
#line 259 "mclib.nw"
    currb_p = p + n;
  } else {
    
#line 392 "mclib.nw"
if (!currb->curbuf->next) {
  int curbufsize = (currb->curbuf->limit - currb->curbuf->data);
  int minsize = 32 + (currb_p - currb->curbuf->data) - curbufsize;
  int size = roundup(max(minsize, currb->size_hint), 8);
  Buffer b = (Buffer) mc_alloc(roundup(sizeof(*b), 8) + size, RBlock_data_pool);

  b->data = (unsigned char *)(b) + roundup(sizeof(*b), 8);
  b->limit = b->data + size;
  b->next = (Buffer)0;
  b->datalc = currb->curbuf->datalc + curbufsize;
  currb->curbuf->next = b;
  currb->size_hint = BUFSZ;
}
#line 305 "mclib.nw"
{ unsigned roomhere = 
        currb_p < currb->curbuf->limit ? currb->curbuf->limit - currb_p : 0;
  if (roomhere > 0) emitb(val >> 8*(n-roomhere), roomhere);
  
#line 315 "mclib.nw"
{ unsigned templc = lc();
  currb->curbuf = currb->curbuf->next;
  currb_safe = currb->curbuf->limit - MARGIN;
  currb_p = templc - currb->curbuf->datalc + currb->curbuf->data;
}
#line 309 "mclib.nw"
  emitb(val, n - roomhere);
}
#line 262 "mclib.nw"
  }
}
#line 336 "mclib.nw"
static void initial_cl_emitm(rb, lc, bits, size) 
         RBlock rb; unsigned lc; unsigned long bits; unsigned size; 
{
  static union { unsigned u; unsigned char c[sizeof(unsigned)]; } u = { 0xaabbccdd };
  switch (u.c[0]) {
    case 0xaa: cl_emitm = &cl_emitb; break;
    case 0xdd: cl_emitm = &cl_emitl; break;
    default:   assert(("byte-order botch", 0));
  }
  (*cl_emitm)(rb, lc, bits, size);
}
void (*cl_emitm)(RBlock rb, unsigned lc, unsigned long, unsigned) = &initial_cl_emitm; 
#line 350 "mclib.nw"
void cl_emitl(rb, lc, val, n) RBlock rb; unsigned lc; unsigned long val; unsigned n; {
  struct rblock_buffer *cb;
  register unsigned char *p;
  for (cb = &rb->firstbuf; cb->next && lc >= cb->next->datalc; cb = cb->next);
  p = cb->data + (lc - cb->datalc);
  if (p + n <= cb->limit) {
#line 235 "mclib.nw"
switch (n) {
  #define BYTE(N) case N+1: p[N] = val >> 8*N; /* fall through */
  BYTE(7) BYTE(6) BYTE(5) BYTE(4) BYTE(3) BYTE(2) BYTE(1) BYTE(0)
  #undef BYTE
  case 0: /* do nothing */
    break;
  default: assert(("unsigned long bigger than 8 bytes", 0));
}
#line 355 "mclib.nw"
                                                                                   }
  else {
#line 368 "mclib.nw"
{ unsigned roomhere = cb->limit - p;
  assert(roomhere > 0 && roomhere < n);
  cl_emitl(rb, lc, val, roomhere);
  cl_emitl(rb, lc+roomhere, val >> 8*roomhere, n - roomhere);
}
#line 356 "mclib.nw"
                                                        }
}
#line 359 "mclib.nw"
void cl_emitb(rb, lc, val, n) RBlock rb; unsigned lc; unsigned long val; unsigned n; {
  struct rblock_buffer *cb;
  register unsigned char *p;
  for (cb = &rb->firstbuf; cb->next && lc >= cb->next->datalc; cb = cb->next);
  p = cb->data + (lc - cb->datalc);
  if (p + n <= cb->limit) {
#line 265 "mclib.nw"
switch (n) {
  #define S(POS, N) (p[POS] = val >> 8*N)
  case 0: break;
  case 1: S(0,0); break;
  case 2: S(0,1); S(1,0); break;
  case 3: S(0,2); S(1,1); S(2,0); break;
  case 4: S(0,3); S(1,2); S(2,1); S(3,0); break;
  case 5: S(0,4); S(1,3); S(2,2); S(3,1); S(4,0); break;
  case 6: S(0,5); S(1,4); S(2,3); S(3,2); S(4,1); S(5,0); break;
  case 7: S(0,6); S(1,5); S(2,4); S(3,3); S(4,2); S(5,1); S(6,0); break;
  case 8: S(0,7); S(1,6); S(2,5); S(3,4); S(4,3); S(5,2); S(6,1); S(7,0); break;
  default: assert(("unsigned long bigger than 8 bytes", 0));
}
#line 364 "mclib.nw"
                                                                                }
  else {
#line 374 "mclib.nw"
{ unsigned roomhere = cb->limit - p;
  assert(roomhere > 0 && roomhere < n);
  cl_emitl(rb, lc, val >> 8*roomhere, roomhere);
  cl_emitl(rb, lc+roomhere, val, n - roomhere);
}
#line 365 "mclib.nw"
                                                     }
}
#line 438 "mclib.nw"
static void initial_emitm(bits, size) unsigned long bits; unsigned size; {
  static union { unsigned u; unsigned char c[sizeof(unsigned)]; } u = { 0xaabbccdd };
  switch (u.c[0]) {
    case 0xaa: emitm = &emitb; break;
    case 0xdd: emitm = &emitl; break;
    default:   assert(("byte-order botch", 0));
  }
  (*emitm)(bits, size);
}
void (*emitm)(unsigned long, unsigned) = &initial_emitm; 
#line 605 "mclib.nw"
void set_lc(rb, newlc) RBlock rb; unsigned newlc; {
    
#line 632 "mclib.nw"
if (!currb->firstbuf.next) {
  assert(currb->curbuf == &currb->firstbuf);
  currb->firstbuf.datalc = newlc;
  currb_p = currb->curbuf->data; /* might have been advanced by addlc */
  return;
}
#line 607 "mclib.nw"
    if (newlc < currb->curbuf->datalc) {
      currb->curbuf = &currb->firstbuf;
      currb_safe = currb->curbuf->limit - MARGIN;
    }
    assert(("above low water", newlc >= currb->curbuf->datalc));
    currb_p = newlc - currb->curbuf->datalc + currb->curbuf->data;
}
#line 642 "mclib.nw"
void align(n) unsigned n; {
    unsigned oldlc = lc();
    unsigned newlc;
    newlc = (oldlc + n - 1);
    newlc -= newlc % n;
    addlc(newlc-oldlc);
}
#line 657 "mclib.nw"
void set_register(rb, reg, rlc) RBlock rb; unsigned reg, rlc; {
    assert(!rb->known.reg);
    rb->reg = reg;
    rb->reglc = rlc;
    rb->known.reg = 1;
}

#line 685 "mclib.nw"
RBlock block_new(size) unsigned size; {
    RBlock rb, tmprb; 
    
    rb = (RBlock) mc_alloc(sizeof(*rb), RBlock_pool);
    
#line 89 "mclib.nw"
rb->curbuf = &rb->firstbuf;
#line 195 "mclib.nw"
rb->firstbuf.data = rb->firstbuf.limit = bogus_buffer + MARGIN;
#line 91 "mclib.nw"
rb->p = rb->firstbuf.data;
rb->firstbuf.next = (Buffer)0;
rb->firstbuf.datalc = 0;	/* lc is initially 0 */
#line 117 "mclib.nw"
rb->known.address = rb->known.reg = 0;
rb->label = label_new("unnamed");
rb->label->block = rb;
rb->label->offset = 0;
#line 390 "mclib.nw"
rb->size_hint = BUFSZ;
#line 690 "mclib.nw"
    rb->size_hint = size > 0 ? size : BUFSZ;
    
#line 701 "mclib.nw"
nblocks++; /* do we really need this instrumentation? */
rb->next = defined_rbs;		/* instrumentation */
defined_rbs = rb; 		/* instrumentation */
#line 692 "mclib.nw"
    return rb;
}
#line 710 "mclib.nw"
RBlock defined_rbs = (RBlock) 0;/* instrumentation */
int nblocks = 0;		/* instrumentation */
#line 718 "mclib.nw"
void set_address(rb, address) RBlock rb; unsigned address; {
    assert(rb);
    rb->address = address;
    rb->known.address = 1;
}
#line 738 "mclib.nw"
void block_copy(dest, rb, start, n) unsigned char *dest; RBlock rb; unsigned start, n; {
  void *memcpy(void *dest, const void *src, size_t n);
  #define TRANSFER(SRC, N) (memcpy(dest, (SRC), (N)), dest += (N))
  
#line 745 "mclib.nw"
{ Buffer buf;
  unsigned char *p;
  for (buf = buffer_at_lc(rb, start), p = buf->data + (start - buf->datalc);
       buf && (n > 0);
       buf = buf->next, p = buf ? buf->data : p
      ) {
    unsigned blk_size = min(buf->limit - p, n);
    TRANSFER(p, blk_size);
    n -= blk_size;
  }
  assert(n == 0);
}
#line 742 "mclib.nw"
  #undef TRANSFER
}
#line 759 "mclib.nw"
void block_write(fd, rb, start, n) RBlock rb; unsigned start, n; {
  #define TRANSFER(SRC, N) (write(fd, SRC, N))
  
#line 745 "mclib.nw"
{ Buffer buf;
  unsigned char *p;
  for (buf = buffer_at_lc(rb, start), p = buf->data + (start - buf->datalc);
       buf && (n > 0);
       buf = buf->next, p = buf ? buf->data : p
      ) {
    unsigned blk_size = min(buf->limit - p, n);
    TRANSFER(p, blk_size);
    n -= blk_size;
  }
  assert(n == 0);
}
#line 762 "mclib.nw"
  #undef TRANSFER
}
#line 772 "mclib.nw"
static Buffer buffer_at_lc(rb, start) RBlock rb; unsigned start; {
  Buffer b = rb->curbuf;
  if (start < b->datalc)
    b = &rb->firstbuf;
  assert(start >= b->datalc);
  while (b && start > b->datalc + (b->limit - b->data))
    b = b->next;
  assert(b);
  return b;
}
#line 789 "mclib.nw"
unsigned long block_fetchl(rb, lc, n) 
    RBlock rb; unsigned lc; unsigned n; 
{
  unsigned char bytes[8];
  unsigned long val = 0;
  assert(n <= sizeof(bytes));
  block_copy(bytes, rb, lc, n);
  
#line 811 "mclib.nw"
val = 0;
switch (n) {
  #define BYTE(N) case N+1: val |= bytes[N] << 8*N; /* fall through */
  BYTE(7) BYTE(6) BYTE(5) BYTE(4) BYTE(3) BYTE(2) BYTE(1) BYTE(0)
  #undef BYTE
  case 0: /* do nothing */
    break;
  default: assert(("unsigned long bigger than 8 bytes", 0));
}
#line 797 "mclib.nw"
  return val;
}
#line 800 "mclib.nw"
unsigned long block_fetchb(rb, lc, n) 
    RBlock rb; unsigned lc; unsigned n; 
{
  unsigned char bytes[8];
  unsigned long val;
  assert(n <= sizeof(bytes));
  block_copy(bytes, rb, lc, n);
  
#line 821 "mclib.nw"
switch (n) {
  #define B(POS, N) (bytes[POS] << 8*N)
  case 0: break;
  case 1: val = B(0,0); break;
  case 2: val = B(0,1) | B(1,0); break;
  case 3: val = B(0,2) | B(1,1) | B(2,0); break;
  case 4: val = B(0,3) | B(1,2) | B(2,1) | B(3,0); break;
  case 5: val = B(0,4) | B(1,3) | B(2,2) | B(3,1) | B(4,0); break;
  case 6: val = B(0,5) | B(1,4) | B(2,3) | B(3,2) | B(4,1) | B(5,0); break;
  case 7: val = B(0,6) | B(1,5) | B(2,4) | B(3,3) | B(4,2) | B(5,1) | B(6,0); break;
  case 8: val = B(0,7) | B(1,6) | B(2,5) | B(3,4) | B(4,3) | B(5,2) | B(6,1) | B(7,0); 
          break;
  default: assert(("unsigned long bigger than 8 bytes", 0));
  #undef B
}
#line 808 "mclib.nw"
  return val;
}
#line 840 "mclib.nw"
static unsigned long initial_block_fetchm(rb, lc, size) 
         RBlock rb; unsigned lc; unsigned size; 
{
  static union { unsigned u; unsigned char c[sizeof(unsigned)]; } u = { 0xaabbccdd };
  switch (u.c[0]) {
    case 0xaa: block_fetchm = &block_fetchb; break;
    case 0xdd: block_fetchm = &block_fetchl; break;
    default:   assert(("byte-order botch", 0));
  }
  return (*block_fetchm)(rb, lc, size);
}
unsigned long (*block_fetchm)(RBlock rb, unsigned lc, unsigned) = &initial_block_fetchm; 
#line 882 "mclib.nw"
void label_define(lbl, offset) RLabel lbl; int offset; {
    label_define_at(lbl, currb, lc() + offset);
}
void label_define_at(lbl, block, lc) RLabel lbl; RBlock block; unsigned lc; {
    assert(lbl);
    assert(!block_defined(lbl->block));  /* fail on multiple definition */
    lbl->block = block;
    lbl->offset = lc;
}
#line 894 "mclib.nw"
RLabel label_new(name) char *name; {
    RLabel lbl;

    lbl = (RLabel) mc_alloc(sizeof(*lbl), RLabel_pool);
    lbl->block = &undefrblock;
    lbl->name = name;
    return lbl;
}
#line 966 "mclib.nw"
static void fail_if_undef(void *closure, RAddr a) {
    if (!location_known(a)) 
       ((FailCont)closure)("Label %s undefined or unbound", a->label->name);
}

#line 972 "mclib.nw"
void apply_closure(RClosure cl, Emitter emitter, FailCont fail) {
    (*cl->h->relocfn)(cl, &fail_if_undef, (void*)fail);
    (*cl->h->apply)(cl, emitter, fail);
}
#line 996 "mclib.nw"
RClosure mc_create_closure_at_offset(unsigned size, ClosureHeader h, unsigned offset) {
  RBlock   this_block = crb();
  unsigned this_lc    = lc() + offset;
  RClosure c = (RClosure) mc_alloc_closure(size, this_block, this_lc);
  c->h = h;
  c->loc.dest_block = this_block;
  c->loc.dest_lc    = this_lc;
  return c;
}
#line 1010 "mclib.nw"
RClosure mc_create_closure_here(unsigned size, ClosureHeader h) {
  return mc_create_closure_at_offset(size, h, 0);
}
#line 1016 "mclib.nw"
static void label_print(struct label *label) {
  asmprintf(asmprintfd, "%s", label->name ? label->name : "???");
}
#line 1022 "mclib.nw"
typedef void (*asmprinter)(void *closure, const char *fmt, ...);
extern int fprintf(FILE *stream, const char *fmt, ...); /* needed at Purdue -- ugh */
void (*asmprintf)(void *closure, const char *fmt, ...) = (asmprinter) fprintf;
void *asmprintfd = (void *)stdout;
void (*asmprintreloc)(RAddr reloc) = reloc_print; /* calls asmprintf */
#line 79 "reloc.nw"
RAddr addr_new(label, offset) RLabel label; int offset; {
    RAddr ra;

    ra = (RAddr) mc_alloc(sizeof(*ra), RAddr_pool);
    ra->label = label;
    ra->offset = offset;
    return ra;
}
#line 100 "reloc.nw"
static void reloc_print(RAddr addr) {
  label_print(addr->label);
  if (addr->offset > 0) asmprintf(asmprintfd, "+%d", addr->offset);
  if (addr->offset < 0) asmprintf(asmprintfd,  "%d", addr->offset);
}
#line 113 "reloc.nw"
RAddr unsigned_to_raddr(unsigned lc) {
  static RBlock rb;
  RLabel lbl = label_new("stands for an unsigned value");
  if (!rb) { rb = block_new(0); set_address(rb, 0); }
  label_define_at(lbl, rb, lc);
  return addr_new(lbl, 0);
}

