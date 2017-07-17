match [nextPC] lc to
| ret() =>
        lc = nextPC;
        return true;
else
        return false;
endmatch
