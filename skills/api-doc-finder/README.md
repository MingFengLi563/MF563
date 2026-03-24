# 🔍 api-doc-finder - API 文档搜索助手

## 技能简介

帮助非技术背景的产品经理快速找到官方 API 文档，整理接口清单、参数说明、认证方式，输出结构化摘要。

## 使用场景

- 设计产品功能时需要调用第三方接口
- 评估技术方案可行性
- 快速了解某个平台的 API 能力
- 整理接口文档给开发团队

## 使用方法

直接描述你的需求，例如：

```
帮我找 Meta WhatsApp 发送消息的 API 文档
```

```
查一下钉钉机器人 webhook 接口怎么用
```

```
Google Calendar API 有哪些接口可以创建事件
```

```
微信开放平台获取用户信息的接口参数是什么
```

## 输出内容

每个 API 文档摘要包含：

| 模块 | 内容 |
|------|------|
| 📌 文档来源 | 官方链接、版本、更新日期 |
| 🔐 认证方式 | OAuth/API Key/Token，获取方式 |
| 📋 接口清单 | 接口列表、方法、路径、功能 |
| 📥 请求参数 | 必填/可选字段、类型说明 |
| 📤 返回参数 | 返回字段说明 |
| ⚠️ 限流规则 | 频率、配额限制 |
| 🚦 接口状态 | 公开/需审批/已废弃 |
| 💡 产品建议 | 可行性评估、注意事项 |

## 支持的平台

- Meta (Facebook/WhatsApp/Instagram)
- Google (Gmail/Calendar/Drive/Sheets)
- 微信 (公众号/小程序/企业微信)
- 钉钉
- Slack
- Telegram
- 其他主流平台 API

## 示例输出

```markdown
# Meta WhatsApp Business API 文档摘要

## 📌 文档来源
- **官方文档**: https://developers.facebook.com/docs/whatsapp/cloud-api
- **API 版本**: v17.0
- **最后更新**: 2026-03-15

## 🔐 认证方式
- **类型**: Bearer Token (Cloud API)
- **获取方式**: Meta Developers 控制台创建应用
- **有效期**: 永久（需定期刷新）

## 📋 核心接口清单

| 接口名称 | 方法 | 路径 | 功能 | 权限要求 |
|----------|------|------|------|----------|
| 发送消息 | POST | /v17.0/{phone-number-id}/messages | 发送文本/图片/模板消息 | whatsapp:messages:send |

## 📥 请求参数示例

### 发送文本消息
```json
{
  "messaging_product": "whatsapp",
  "to": "用户手机号",
  "type": "text",
  "text": {
    "body": "消息内容"
  }
}
```

## ⚠️ 限流规则
- **频率**: 80 次/秒
- **配额**: 按电话号等级（1K/天起步）

## 🚦 接口状态
- ✅ 公开可用（需 Meta 商务验证）

## 💡 产品建议
- 首次使用需完成商务验证（1-3 工作日）
- 模板消息需预先审核
- 免费额度：1000 条/月
```

## 注意事项

1. **文档时效性** — API 可能更新，以官方最新文档为准
2. **认证门槛** — 部分平台需商务验证或付费
3. **限流差异** — 不同账户等级限流不同
4. **区域限制** — 部分 API 有地域限制

## 相关技能

- **api-feasibility-test** — 测试接口可用性，返回实际数据
- **searxng** — 联网搜索
- **browser-use** — 浏览器自动化（截图）

## 版本

- v1.0.0 — 初始版本

## 作者

Created for FRANCo - SalesMartly Product Manager
