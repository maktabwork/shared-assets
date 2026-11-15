#!/usr/bin/env bash
# Builds the Claude Code plugin (monjizeen@tools) into a folder that is the
# whole content of the private monjizeen/tools repo: the manifests, the hook,
# and only the skills in plugin/skills.txt. Account managers get read access to
# that repo only, never to shared-assets.
#   scripts/build-plugin.sh <out-dir> [version]
set -euo pipefail

OUT="${1:?usage: scripts/build-plugin.sh <out-dir> [version]}"
VERSION="${2:-0.1.0}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

mkdir -p "$OUT"
# Keep the target repo's .git; replace everything else.
find "$OUT" -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
mkdir -p "$OUT/.claude-plugin" "$OUT/skills"

cp "$ROOT/plugin/marketplace.json" "$OUT/.claude-plugin/marketplace.json"
node -e '
  const fs = require("fs");
  const [src, dest, version] = process.argv.slice(1);
  const manifest = JSON.parse(fs.readFileSync(src, "utf8"));
  manifest.version = version;
  fs.writeFileSync(dest, JSON.stringify(manifest, null, 2) + "\n");
' "$ROOT/plugin/plugin.json" "$OUT/.claude-plugin/plugin.json" "$VERSION"
cp -R "$ROOT/plugin/hooks" "$OUT/hooks"
cp "$ROOT/docs/CLAUDE-CODE-PLUGIN.md" "$OUT/README.md"

count=0
while IFS= read -r skill; do
  [[ -z "$skill" || "$skill" == \#* ]] && continue
  if [[ ! -d "$ROOT/skills/$skill" ]]; then
    echo "Missing skill: $skill" >&2
    exit 1
  fi
  cp -R "$ROOT/skills/$skill" "$OUT/skills/$skill"
  count=$((count + 1))
done < "$ROOT/plugin/skills.txt"

echo "Built monjizeen@tools $VERSION with $count skills in $OUT"
