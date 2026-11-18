const fs = require('node:fs');
const path = require('node:path');
function balance(s){const issues=[],env=[],math=[];let brace=0;for(let i=0;i<s.length;i++){const c=s[i];if(c==="%"){while(i<s.length&&s[i]!=="\n")i++;continue;}if(c==="\\"){const z=s[i+1];if(z==="["||z==="]"){if(z==="["){if(math.length)issues.push("nested math at "+i);math.push("[");}else if(math.pop()!=="[")issues.push("display close at "+i);i++;continue;}const e=s.slice(i).match(/^\\(begin|end)\{([^}]+)\}/);if(e){if(e[1]==="begin")env.push(e[2]);else if(env.pop()!==e[2])issues.push("environment mismatch "+e[2]);i+=e[0].length-1;continue;}if(z&&/[^A-Za-z]/.test(z)){i++;continue;}}if(c==="{")brace++;else if(c==="}"){brace--;if(brace<0)issues.push("unexpected } at "+i);}else if(c==="$"){if(math[math.length-1]==="$")math.pop();else{if(math.length)issues.push("inline in display at "+i);math.push("$");}}}if(brace)issues.push("brace balance "+brace);if(math.length)issues.push("math remains "+math.join());if(env.length)issues.push("environments remain "+env.join());return issues;}
const root=__dirname;
const files=fs.readdirSync(path.join(root,'pages')).filter(x=>x.endsWith('.tex')).map(x=>path.join(root,'pages',x)).concat([path.join(root,'K34-02_transcription.tex'),path.join(root,'K34-02_standalone.tex')]);
let failed=false;
for(const file of files){const errors=balance(fs.readFileSync(file,'utf8'));console.log(path.relative(root,file)+': '+(errors.length?errors.join('; '):'PASS'));failed ||= errors.length>0;}
process.exitCode=failed?1:0;
