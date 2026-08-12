# tabby-quick-cmds-lite

A lightweight fork of [minyoad/tabby-quick-cmds](https://github.com/minyoad/tabby-quick-cmds), rebuilt to stay smooth even with **thousands of quick commands** in [Tabby](https://tabby.sh).

The original plugin became laggy once you grouped many commands — every keystroke rebuilt the entire list. This Lite version cuts the heavy parts and adds lightweight rendering.

## Why this fork (the "six cuts")

| # | Change | Removed | Benefit |
|---|--------|---------|---------|
| 1 | Dropped per-command shortcuts | `command.shortcut`, global `keydown` scanning, `handleDocumentKeyDown()` | Terminal typing is no longer intercepted — big perf win |
| 2 | Dropped SSH Profile scoping | `profileIds`, `SSHProfileOption`, `sshScope.ts` | No per-search SSH context evaluation |
| 3 | Reworked search | Full regroup on each keystroke | Pre-built `searchText` + 80–120 ms debounce, filter only |
| 4 | Group index built once | Rebuild groups on every refresh | `Map<string, Command[]>`, rebuilt only on add/edit/delete |
| 5 | Capped DOM rendering | Render all command DOM | Virtual scrolling (max ~50–100), `trackByCommandId()` |
| 6 | Dropped usage-count sorting | `qcUsageCount`, localStorage read | No init sort cost; predictable behavior |

## Features kept
- `Alt + Q` command palette + toolbar button
- Command name / text / group, search (100 ms debounce)
- Add / edit / delete / copy, click-to-run on current terminal
- Multi-line commands, `appendCR`, `\xHH` control chars, `\s<ms>` delay lines
- Reads your existing `qc.cmds` data directly

## Install (Windows)
See [INSTALL-Windows.txt](INSTALL-Windows.txt) (full Chinese guide in [README_CN.md](README_CN.md)).

Short version:
1. Disable / remove the original `tabby-quick-cmds` (avoid `Alt+Q` conflict).
2. Copy the whole `tabby-quick-cmds-lite` folder into `%APPDATA%\tabby\plugins\node_modules\`.
3. Restart Tabby, then press `Alt + Q`.

## Download
Grab the latest release zip from [Releases](https://github.com/xyblue135/tabby-quick-cmds-lite/releases).
It contains the ready-to-use `tabby-quick-cmds-lite` folder — just extract it into
`%APPDATA%\tabby\plugins\node_modules\`. No build step needed.

## Build from source
```bash
npm install          # installs TypeScript (peer deps are provided by Tabby at runtime)
npm run build        # compiles src/*.ts -> dist/index.js via tsc
```
`src/shims.d.ts` supplies ambient types for Tabby / Angular, so a standalone `tsc` build works without the full Tabby dev environment.

## Repository layout
```
src/            TypeScript source (index.ts, shims.d.ts)
dist/index.js   Prebuilt plugin (the file Tabby actually loads)
package.json    Plugin manifest
tsconfig.json   Build config (tsc -> dist)
```

## License
MIT — based on [minyoad/tabby-quick-cmds](https://github.com/minyoad/tabby-quick-cmds).
