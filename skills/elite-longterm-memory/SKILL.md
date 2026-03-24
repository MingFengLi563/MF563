# Elite Longterm Memory Skill

**终极 AI 代理记忆系统** — 永不丢失上下文

---

## 核心架构

结合 7 种记忆方法于一体：

| 层级 | 存储 | 用途 | 持久性 |
|-----|------|------|--------|
| 1. Hot RAM | SESSION-STATE.md | 活跃任务上下文 |  survives compaction |
| 2. Warm Store | LanceDB | 语义搜索 | 自动召回 |
| 3. Cold Store | Git-Notes | 结构化决策 | 永久 |
| 4. Archive | MEMORY.md + daily/ | 人类可读 | 精选 |
| 5. Cloud | SuperMemory | 跨设备同步 | 可选 |

---

## WAL 协议（关键）

**核心原则：** 在回复之前写入状态，而不是之后。

```
用户："这个项目用 Tailwind"

代理（内部）：
1. 写入 SESSION-STATE.md → "决策：使用 Tailwind"
2. 然后回复 → "好的，就用 Tailwind..."
```

如果先回复再保存，崩溃时上下文就丢失了。WAL 确保持久性。

---

## 激活条件

自动激活当：
- 会话开始 → 读取 MEMORY.md + 昨日/今日记忆
- 任务完成 → 写入经验教训
- 发现重要事实 → 自动提取并存储
- 用户说"记住这个" → 写入记忆

---

## 文件结构

```
workspace/
├── SESSION-STATE.md    # Hot RAM（活跃上下文）
├── MEMORY.md           # 精选长期记忆
└── memory/
    ├── 2026-03-17.md   # 每日日志
    └── ...
```

---

## 命令

```bash
# 初始化
npx elite-longterm-memory init

# 检查状态
npx elite-longterm-memory status

# 创建今日日志
npx elite-longterm-memory today
```

---

## Mem0 集成（推荐）

自动从对话中提取事实，减少 80% token：

```bash
npm install mem0ai
export MEM0_API_KEY="your-key"
```

```javascript
const { MemoryClient } = require('mem0ai');
const client = new MemoryClient({ apiKey: process.env.MEM0_API_KEY });

// 自动提取事实
await client.add(messages, { user_id: "user123" });

// 检索记忆
const memories = await client.search(query, { user_id: "user123" });
```

---

## 常见问题修复

| 问题 | 原因 | 解决方案 |
|-----|------|---------|
| 忘记一切 | memory_search 禁用 | 启用 + 添加 OpenAI key |
| 重复错误 | 经验未记录 | 写入 memory/lessons.md |
| 子代理隔离 | 无上下文继承 | 在 task prompt 中传递上下文 |
| 事实未捕获 | 无自动提取 | 使用 Mem0 |

---

## 参考

- GitHub: https://github.com/NextFrontierBuilds/elite-longterm-memory
- npm: https://www.npmjs.com/package/elite-longterm-memory
