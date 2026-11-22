// Executed in functions.exec, once; requires the tools runtime.
const queries = [
  {q: '"Lieberman" "Hodge manifolds" ("syllabus" OR "course") -site:jstor.org -site:researchgate.net -site:scispace.com -site:cam.ac.uk -site:ed.ac.uk'},
  {q: '"Lieberman" "Numerical and Homological" ("reading" OR "seminar") (site:math.columbia.edu OR site:math.harvard.edu OR site:math.stanford.edu)'},
  {q: '"Liebermann" "Hodge manifolds" ("cours" OR "séminaire") -site:zbmath.org -site:core.ac.uk'}
];
const start = Date.now();
const result = await tools.mcp__codex_apps__search_service_web_run({system1_search_query:queries,response_length:"long"});
const record = {started_utc:new Date(start).toISOString(),elapsed_seconds:(Date.now()-start)/1000,query_count:queries.length,queries,result};
store("part_b_lieberman_course_queries",record);
text(result);
text({started_utc:record.started_utc,elapsed_seconds:record.elapsed_seconds,query_count:record.query_count});
