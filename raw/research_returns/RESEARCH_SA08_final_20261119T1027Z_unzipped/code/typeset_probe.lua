kpse.set_program_name("lualatex")
local p=os.getenv("SA08_CACHE_PROBE")
print("cache",p,kpse.expand_var("$TEXMFCACHE"))
print("lfsdir",lfs.isdir(p))
local f,e=io.open(p.."/probe.tmp","w"); print("write",f,e); if f then f:write("ok");f:close();os.remove(p.."/probe.tmp") end
