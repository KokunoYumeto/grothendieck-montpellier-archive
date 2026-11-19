kpse.set_program_name('lualatex')
local cache=kpse.expand_var('$TEXMFCACHE')
print('cache',cache)
print('attributes',lfs.attributes(cache,'mode'),lfs.attributes(cache,'permissions'))
print('writablefn',lfs.iswritablefile)
if lfs.iswritablefile then print('writable',lfs.iswritablefile(cache)) end
local f,err=io.open(cache..'/probe.tmp','w')
print('opened',f,err)
if f then f:write('probe');f:close();os.remove(cache..'/probe.tmp') end
require('lualibs')
print('file.is_writable',file.is_writable(cache))
print('lfs.isdir',lfs.isdir(cache))
