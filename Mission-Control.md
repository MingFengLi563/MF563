# 🎯 StormClaw Mission Control

**最后更新**: 2026-03-16 16:25 | **时区**: Asia/Shanghai

---

## 📊 系统状态

| 状态 | 值 |
|------|-----|
| OpenClaw 版本 | `2026.3.13 (61d171a)` |
| 网关状态 | 🟢 运行中 |
| 活跃代理 | `main` (StormClaw) |
| 当前模型 | `qwen3.5-plus` |
| 会话上下文 | 80k/100k (80%) |

---

## ⏰ 每日任务 (Cron)

| 任务名称 | 调度 | 状态 | 下次执行 | 投递 |
|----------|------|------|----------|------|
| 竞品监控日报 | `0 18 * * *` (每天 18:00) | 🟢 正常 | 今天 18:00 | 飞书 → user:main |

### 任务详情 - 竞品监控日报
- **ID**: `18bb2822-9006-45fa-ab8c-79929180696b`
- **上次执行**: 成功 (耗时 200s)
- **连续错误**: 0
- **投递状态**: ✅ 已送达

---

## 🧰 技能清单 (16 个)

### 🔧 自动化 & 浏览器
| 技能 | 说明 |
|------|------|
| `agent-browser` | Rust 头浏览器自动化 |
| `browser-use` | Playwright 浏览器自动化 |
| `playwright` | 浏览器测试/数据提取 |

### 🔍 搜索 & 研究
| 技能 | 说明 |
|------|------|
| `searxng` | 隐私搜索引擎 (优先使用) |
| `multi-search-engine` | 17 个搜索引擎聚合 |

### 📝 文档 & 创作
| 技能 | 说明 |
|------|------|
| `skill-creator` | 技能创作工具 |
| `summarize` | 内容摘要 |
| `ui-ux-design` | UI/UX 设计辅助 |

### 🤖 代理增强
| 技能 | 说明 |
|------|------|
| `memory` | 无限记忆存储 |
| `proactive-agent` | 主动代理模式 |
| `self-improving-agent` | 自我改进 |
| `nopua` | 反 PUA 驱动 |
| `skill-vetter` | 安全检查 |

### 🛠️ 工具 & 集成
| 技能 | 说明 |
|------|------|
| `github` | GitHub 集成 |
| `healthcheck` | 系统健康检查 |
| `find-skills` | 技能发现 |

### 📈 金融 (已禁用)
| 技能 | 说明 |
|------|------|
| `stock-analysis` | 股票分析 (已移除) |

---

## 🧠 记忆系统

### 记忆文件
| 文件 | 大小 | 最后修改 |
|------|------|----------|
| `memory/2026-03-16.md` | 3.6KB | 14:36 |
| `memory/2026-03-14.md` | 2.5KB | 3 月 14 日 |
| `memory/2026-03-13-telegram-integration.md` | 1.8KB | 3 月 13 日 |
| `memory/salesmartly-context.md` | 1.1KB | 3 月 13 日 |

### 长期记忆
- **MEMORY.md**: ✅ 已激活 (233 字节)
- **内容**: 技能偏好、用户笔记

### 今日关键事件 (2026-03-16)
1. ✅ OpenClaw 升级 2026.3.3 → 2026.3.13
2. ✅ 清理代理 (stock-analysis, moneycome)
3. ✅ 安装 NoPUA 技能
4. ✅ PRD 分析 - 新版客户列表

---

## 🤖 代理配置

### 活跃代理
| 代理 | 目录 | 状态 |
|------|------|------|
| `main` | `/home/admin/.openclaw/agents/main/` | 🟢 活跃 |

### 已移除代理
| 代理 | 移除时间 | 原因 |
|------|----------|------|
| `stock-analysis` | 11:21 | 简化配置 |
| `moneycome` | 12:00 | 简化配置 |

---

## 📱 飞书集成

| 配置项 | 值 |
|--------|-----|
| App ID | `cli_a93e4f2bb5385bb5` |
| 模式 | 模式 2 (requireMention: false) |
| 投递目标 | `user:main` |
| 配对状态 | ⏳ 待完成 |

---

## 🔗 快速链接

| 链接 | 说明 |
|------|------|
| [Dashboard](http://172.17.63.86:12238/77e67a43/) | OpenClaw 控制面板 |
| [MEMORY.md](./MEMORY.md) | 长期记忆 |
| [今日记忆](./memory/2026-03-16.md) | 今日日志 |
| [AGENTS.md](./AGENTS.md) | 代理配置指南 |

---

## 📝 待办事项

- [ ] 完成飞书配对/授权
- [ ] 配置 Teambition 需求分析定时任务
- [ ] 安装剩余技能 (skill-creator, using-superpowers 等)

---

*此面板由 StormClaw 自动生成 | 刷新请重新运行命令*
