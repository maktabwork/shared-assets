#!/usr/bin/env node
// Before finish_work: add the tokens this session used since start_work, read
// from the Claude Code transcript, so the ticket shows the real cost.
// Never blocks the call: on any problem it passes the input through unchanged.
const fs = require('fs');

let raw = '';
process.stdin.on('data', (d) => { raw += d; });
process.stdin.on('end', () => {
  let event;
  try { event = JSON.parse(raw); } catch { return; }
  const input = event.tool_input || {};
  try {
    const lines = fs.readFileSync(event.transcript_path, 'utf8').split('\n');
    const seen = new Map(); // message id -> usage (a message is written once per content block)
    for (const line of lines) {
      if (!line.trim()) continue;
      let entry;
      try { entry = JSON.parse(line); } catch { continue; }
      const msg = entry.message;
      if (entry.type !== 'assistant' || !msg) continue;
      const blocks = Array.isArray(msg.content) ? msg.content : [];
      if (blocks.some((b) => b.type === 'tool_use' && /start_work$/.test(b.name || ''))) seen.clear();
      if (msg.usage && msg.id) seen.set(msg.id, msg.usage);
    }
    let inputTokens = 0;
    let outputTokens = 0;
    for (const u of seen.values()) {
      inputTokens += (u.input_tokens || 0) + (u.cache_creation_input_tokens || 0) + (u.cache_read_input_tokens || 0);
      outputTokens += u.output_tokens || 0;
    }
    if (inputTokens + outputTokens === 0) return;
    process.stdout.write(JSON.stringify({
      hookSpecificOutput: {
        hookEventName: 'PreToolUse',
        permissionDecision: 'allow',
        permissionDecisionReason: 'Added the tokens used since start_work',
        updatedInput: { ...input, input_tokens: inputTokens, output_tokens: outputTokens },
      },
    }));
  } catch {
    // No transcript: finish_work goes ahead without tokens.
  }
});
