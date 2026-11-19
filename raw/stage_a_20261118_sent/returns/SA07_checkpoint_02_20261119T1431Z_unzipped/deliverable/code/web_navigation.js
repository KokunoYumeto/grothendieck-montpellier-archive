// Research browser orchestration used in this run.
// Each saved evidence/web_*.json contains the exact request and complete tool result.
// tools is the ChatGPT code-mode runtime, not an external Node package.
async function recordWebSearch(label, request) {
  const result = await tools.mcp__codex_apps__search_service_web_run(request);
  await tools.apply_patch('*** Begin Patch\n*** Add File: /workspace/scratch/9c0c54a66f6c/deliverable/evidence/' + label + '.json\n' + JSON.stringify({request,result},null,2).split('\n').map(l=>'+'+l).join('\n') + '\n*** End Patch');
  return result;
}
