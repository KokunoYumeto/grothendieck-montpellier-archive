function Code(el)
  local repl={['\\']='\\textbackslash{}',['{']='\\{',['}']='\\}',['$']='\\$',['&']='\\&',['#']='\\#',['%']='\\%',['_']='\\_',['^']='\\textasciicircum{}',['~']='\\textasciitilde{}'}
  local chars={}
  for _,c in utf8.codes(el.text) do
    local s=utf8.char(c)
    table.insert(chars,repl[s] or s)
    if s==',' or s==';' or s=='=' or s=='_' or s=='/' or s=='+' or s=='-' or s=='(' or s==')' or s=='[' or s==']' or s==':' or s=='≤' or s=='≥' or s=='⊗' or s=='⊕' or s=='→' then table.insert(chars,'\\allowbreak{}') end
  end
  return pandoc.RawInline('latex','\\texttt{\\small '..table.concat(chars)..'}')
end
