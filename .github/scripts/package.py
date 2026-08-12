import shutil, os

os.makedirs("pkg/tabby-quick-cmds-lite", exist_ok=True)
files = ["package.json", "dist/index.js", "README_CN.md", "LICENSE",
         "CHANGELOG.md", "INSTALL-Windows.txt"]
for f in files:
    if os.path.exists(f):
        shutil.copy(f, os.path.join("pkg", "tabby-quick-cmds-lite", os.path.basename(f)))
    else:
        print("WARNING: missing", f)
shutil.make_archive("tabby-quick-cmds-lite", "zip", "pkg")
print("packaged tabby-quick-cmds-lite.zip")
