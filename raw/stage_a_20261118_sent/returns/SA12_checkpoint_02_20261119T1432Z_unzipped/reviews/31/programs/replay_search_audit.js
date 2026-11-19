// Replay the exact closing audit requests saved in search_manifest.json.
// Run within functions.exec; results are returned by the search-service tool.
// The original fourteen batches and their responses are preserved in outputs/search_audit_*.json.
const result = await tools.exec_command({cmd:"cat /workspace/scratch/a77a578fa7d4/SA12_work/reviews/31/search_manifest.json",max_output_tokens:12000});
const queries = JSON.parse(result.output);
let batches=[];
for (const engine of ["system2_search_query","system1_search_query"]) {
 const subset=queries.filter(q=>q.engine===engine);
 const step=engine==="system2_search_query"?4:3;
 for(let i=0;i<subset.length;i+=step) batches.push({engine,queries:subset.slice(i,i+step)});
}
// Each output includes the exact request and its response. Source mutations are not parallelized.
const outputs = await Promise.allSettled(batches.map(async (b,i)=>({batch:i+1,request:b,result:await tools.mcp__codex_apps__search_service_web_run({[b.engine]:b.queries.map(q=>({q:q.query})),response_length:"long"})})));
for(const output of outputs) text(output);
