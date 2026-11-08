#!/usr/bin/env bash
# Builds the ZIP for platform.openai.com/plugins from chatgpt/, with plugin.json
# at the archive root. Prints the path of the ZIP.
set -euo pipefail

root=$(cd "$(dirname "$0")/.." && pwd)
version=$(python3 -c 'import json, sys; print(json.load(open(sys.argv[1]))["version"])' "$root/chatgpt/plugin.json")
out="$root/dist/papernexus-chatgpt-$version.zip"

mkdir -p "$root/dist"
rm -f "$out"
cd "$root/chatgpt"
zip -X -q "$out" plugin.json mcp.json assets/logo.png
echo "$out"
