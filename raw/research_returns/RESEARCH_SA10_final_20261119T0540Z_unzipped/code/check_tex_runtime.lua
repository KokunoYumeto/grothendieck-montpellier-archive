local p='/workspace/scratch/83000dc30063/tex_cache'
local lfs=require'lfs'
for k,v in pairs(lfs.attributes(p) or {}) do print(k,v) end
print('isdir',lfs.isdir(p))
print('writable',lfs.iswritablefile and lfs.iswritablefile(p))
local f,e=io.open(p..'/runtime_test.tmp','wb')
print('write',f~=nil,e)
if f then f:close();os.remove(p..'/runtime_test.tmp') end
