const queries=[
 {q:'"Lieberman" "numerical" ("offprint" OR "tiré à part" OR "tirés-à-part")'},
 {q:'"Lieberman" (site:archives.ihes.fr OR site:archives.umontpellier.fr OR site:patrimoine.bu.umontpellier.fr)'},
 {q:'"Lieberman" "Hodge manifolds" ("collection" OR "Nachlass") -site:researchgate.net -site:scispace.com -site:arxiv.org'}
];
const start=Date.now();
const result=await tools.mcp__codex_apps__search_service_web_run({system1_search_query:queries,response_length:"long"});
const elapsed=(Date.now()-start)/1000;
store("part_b_lieberman_archival_queries1",{queries,elapsed_seconds:elapsed,result,started_utc:new Date(start).toISOString()});
text(result);text({elapsed_seconds:elapsed});
