# Session: 2026-03-20 02:05:45 UTC

- **Session Key**: agent:main:main
- **Session ID**: 0ee572f0-eefd-4309-bc87-6a9a53d95e1a
- **Source**: webchat

## Conversation Summary

user: Sender (untrusted metadata):
```json
{
  "label": "openclaw-control-ui",
  "id": "openclaw-control-ui"
}
```

[Fri 2026-03-20 09:57 GMT+8] 有没有什么技能可以自己去主流社媒平台或者知识库平台，收集我想要的信息？
assistant: 根据你的需求，目前 OpenClaw 生态中有几类技能可以帮你从网络平台收集信息：

## 🔍 搜索类技能

| 技能 | 能力 | 特点 |
|------|------|------|
| **searxng** | 隐私搜索、图片、新闻 | 本地部署，无 API 依赖 |
| **multi-search-engine** | 17 个搜索引擎 (8 国内 +9 全球) | 支持高级搜索语法、时间过滤 |

## 🌐 浏览器自动化技能

| 技能 | 能力 | 适用场景 |
|------|------|----------|
| **browser-use** | 导航、点击、填表、截图、数据提取 | 通用网页自动化 |
| **Playwright** | 完整的浏览器自动化 (MCP) | 复杂交互、JS 渲染页面 |
| **agent-browser** | Rust 无头浏览器 | 快速截图、结构化命令 |

## ⚠️ 关于社交媒体平台

**重要限制：** 主流社媒平台 (微信、微博、抖音、小红书、Twitter 等) 通常有：
- 登录验证
- 反爬虫机制
- API 访问限制

**可行方案：**
1. **公开内容** → 用浏览器自动化技能 + 搜索技能
2. **RSS/公开 API** → 可写脚本定时抓取
3. **需要登录的内容** → 需要配置浏览器 Cookie/Session，有封号风险

## 💡 建议

你想收集什么类型的信息？比如：
- 竞品动态监控？
- 行业资讯聚合？
- 特定关键词追踪？

告诉我具体场景，我可以帮你：
1. 安装合适的技能
2. 设计自动化方案
3. 评估可行性和风险
