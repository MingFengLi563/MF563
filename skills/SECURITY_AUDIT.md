# 🔒 技能安全审计报告

**审计日期:** 2026-03-23  
**审计范围:** 新安装的 3 个技能 + 现有高风险技能  
**审计人:** StormClaw

---

## 📊 审计结果汇总

| 技能 | 风险等级 | 外部请求 | 数据收集 | 建议 |
|------|----------|----------|----------|------|
| **gstack** | 🟡 中等 | ✅ 是 (Supabase) | ✅ 遥测数据 | 需配置关闭 |
| **planning-with-files** | 🟢 低 | ❌ 否 | ❌ 无 | 安全 |
| **lenny-skills** | 🟢 低 | ❌ 否 | ❌ 无 | 安全 |
| **stock-analysis** | 🟡 中等 | ✅ 是 (yfinance) | ❌ 仅本地缓存 | 注意 API 限制 |
| **weather** | 🟢 低 | ✅ 是 (wttr.in) | ❌ 无 | 安全 |
| **searxng** | 🟢 低 | ✅ 是 (本地) | ❌ 无 | 安全 (本地部署) |

---

## 🔍 详细分析

### 1️⃣ gstack (garrytan/gstack) — 🟡 中等风险

#### 发现的风险行为：

**1. 遥测数据收集**
- **位置:** `bin/gstack-telemetry-log`, `bin/gstack-telemetry-sync`
- **收集内容:**
  - 技能名称和使用时间
  - 执行时长和结果 (success/error/abort)
  - 操作系统和架构
  - 并发会话数
  - Git 仓库名和分支 (本地存储，不发送)
  - **installation_id** (社区模式：基于 hostname+username 的 SHA256 哈希)

**2. 外部数据发送**
- **目标:** Supabase (https://frugpmstpnojnhfyimgv.supabase.co)
- **频率:** 每 5 分钟同步一次（最多 100 条记录/次）
- **API Key:** `sb_publishable_tR4i6cyMIrYTE3s6OyHGHw_ppx2p6WK` (公开密钥，仅 INSERT 权限)

**3. 自动打开浏览器**
- **位置:** SKILL.md preamble
- **行为:** 首次运行时建议打开 "Boil the Lake" 文章
- **触发:** 需要用户确认后才执行 `open` 命令

#### 隐私保护机制：

✅ **三档遥测模式:**
- `community` — 发送带 installation_id 的使用数据
- `anonymous` — 仅发送使用计数，无唯一标识
- `off` — 完全关闭遥测（默认）

✅ **数据过滤:**
- 不发送代码内容、文件路径、仓库名
- `_repo_slug` 和 `_branch` 字段在发送前被剥离
- 匿名模式下移除 installation_id

✅ **本地存储优先:**
- 所有数据先写入 `~/.gstack/analytics/skill-usage.jsonl`
- 用户可随时删除或审查

#### 建议操作：

```bash
# 1. 关闭遥测（推荐）
~/.openclaw/workspace/skills/gstack/bin/gstack-config set telemetry off

# 2. 验证配置
~/.openclaw/workspace/skills/gstack/bin/gstack-config list

# 3. 可选：删除已收集的遥测数据
rm -rf ~/.gstack/analytics/
```

---

### 2️⃣ planning-with-files (OthmanAdi) — 🟢 低风险

#### 审计结果：

✅ **无外部请求** — 所有操作都在本地文件系统
✅ **无数据收集** — 不收集任何使用数据
✅ **无网络通信** — 纯本地 Markdown 文件管理

#### 功能范围：
- 创建 `.planning/` 目录存储任务规划
- 读写 Markdown 文件
- 会话恢复（读取之前的规划文件）

#### 结论：
**安全** — 无外部通信，无数据收集，仅本地文件操作。

---

### 3️⃣ lenny-skills (RefoundAI) — 🟢 低风险

#### 审计结果：

✅ **无外部请求** — 纯文档/知识库技能
✅ **无数据收集** — 不提供任何运行时功能
✅ **无网络通信** — 仅包含产品管理框架的 Markdown 文档

#### 功能范围：
- 86 个产品管理技能的文档集合
- 提供参考框架和检查清单
- 无执行代码，无脚本

#### 结论：
**安全** — 纯文档技能，无任何执行能力。

---

### 4️⃣ stock-analysis — 🟡 中等风险

#### 发现的风险行为：

**1. 外部 API 请求**
- **目标:** Yahoo Finance (yfinance 库)
- **内容:** 股票价格、财务数据、新闻
- **频率:** 按需请求（用户触发）

**2. 本地缓存**
- **位置:** 未指定（由 yfinance 库管理）
- **内容:** 股票数据缓存

#### 隐私保护：
✅ 不发送任何用户数据
✅ 仅读取公开的股票信息
✅ 无遥测或分析

#### 建议：
- 注意 Yahoo Finance API 速率限制
- 敏感操作前确认用户意图

---

### 5️⃣ weather — 🟢 低风险

#### 审计结果：

✅ **公开数据** — 仅查询天气信息
✅ **无用户数据** — 不发送任何个人信息
✅ **无持久化** — 不存储查询历史

#### 数据源：
- wttr.in (无需 API Key)
- Open-Meteo (开源天气 API)

#### 结论：
**安全** — 仅查询公开天气数据。

---

### 6️⃣ searxng — 🟢 低风险

#### 审计结果：

✅ **本地部署** — 使用用户自己的 SearXNG 实例
✅ **隐私保护** — SearXNG 本身就是隐私搜索引擎
✅ **无外部依赖** — 不依赖商业 API

#### 结论：
**安全** — 本地隐私搜索引擎集成。

---

## 🛡️ 安全建议

### 立即执行：

```bash
# 1. 关闭 gstack 遥测
~/.openclaw/workspace/skills/gstack/bin/gstack-config set telemetry off

# 2. 验证配置
~/.openclaw/workspace/skills/gstack/bin/gstack-config list
# 应显示：telemetry: off

# 3. 清理已收集的遥测数据（可选）
rm -rf ~/.gstack/analytics/
```

### 长期监控：

1. **定期检查新技能** — 安装前审查 `allowed-tools` 和网络请求
2. **监控网络流量** — 使用 `tcpdump` 或 `wireshark` 检查异常外连
3. **审查脚本权限** — 限制 `Bash` 工具的使用范围

### 技能安装最佳实践：

```bash
# 安装前检查清单：
# 1. 检查 SKILL.md 中的 allowed-tools
grep "allowed-tools" SKILL.md

# 2. 搜索网络请求
grep -r "curl\|wget\|http\|fetch" .

# 3. 搜索遥测/分析
grep -r "telemetry\|analytics\|tracking" .

# 4. 检查外部 API 配置
find . -name "config.sh" -o -name ".env*" | xargs cat
```

---

## 📋 技能权限矩阵

| 技能 | Bash | Read | Write | Network | 风险等级 |
|------|------|------|-------|---------|----------|
| gstack | ✅ | ✅ | ❌ | ✅ (Supabase) | 🟡 |
| planning-with-files | ✅ | ✅ | ✅ | ❌ | 🟢 |
| lenny-skills | ❌ | ❌ | ❌ | ❌ | 🟢 |
| stock-analysis | ✅ | ✅ | ✅ | ✅ (yfinance) | 🟡 |
| weather | ✅ | ❌ | ❌ | ✅ (wttr.in) | 🟢 |
| searxng | ✅ | ❌ | ❌ | ✅ (本地) | 🟢 |

---

## ✅ 总结

**新安装的 3 个技能中：**
- ✅ **planning-with-files** — 安全，无风险
- ✅ **lenny-skills** — 安全，纯文档
- ⚠️ **gstack** — 中等风险，需关闭遥测

**建议立即执行：**
```bash
# 关闭 gstack 遥测
~/.openclaw/workspace/skills/gstack/bin/gstack-config set telemetry off
```

**整体评估：** 技能来源可靠（GitHub 知名作者），无明显恶意行为。gstack 的遥测功能透明且可关闭，符合开源项目常见做法。

---

*最后更新：2026-03-23*
