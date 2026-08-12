# Quick Commands Lite for Tabby

这是基于 `minyoad/tabby-quick-cmds` 思路重构的轻量版本，目标是命令数量很多时仍保持流畅。

## 保留
- Alt + Q 打开命令面板
- 工具栏按钮
- 命令名称 / 内容 / 分组
- 搜索（100ms 防抖）
- 新增、编辑、删除、复制
- 点击执行到当前终端
- 多行命令
- appendCR 自动回车
- `\\xHH` 控制字符
- `\\s毫秒` 延迟行
- 直接读取旧版 `qc.cmds`

## 删除/忽略
- 每条命令的全局快捷键
- document 全局 keydown 扫描
- SSH Profile Scoping
- 使用次数统计和排序
- 参数弹窗
- Ctrl+Click 发送全部终端

## 性能设计
- 平时在终端敲键盘时插件不扫描命令列表
- 命令索引只在加载或增删改时重建
- 搜索只做一次 O(N) 扫描，并有 100ms 防抖
- 页面默认最多渲染 150 条结果，可手动“显示更多”
- Angular 使用 OnPush + trackBy，减少列表重绘

## 安装（Windows）
1. 先在 Tabby 中禁用/删除原 `tabby-quick-cmds`，避免两个插件同时响应 Alt+Q。
2. 解压本 ZIP。
3. 把整个 `tabby-quick-cmds-lite` 文件夹复制到：
   `%APPDATA%\\tabby\\plugins\\node_modules\\`
4. 重启 Tabby。
5. 按 `Alt + Q`，或点击工具栏终端图标。

旧版命令保存在同一个 `qc.cmds` 配置中，Lite 会直接读取。建议首次使用前备份 Tabby 配置。
