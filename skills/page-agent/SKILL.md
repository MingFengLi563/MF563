# PageAgent 技能 - 网页 GUI 自动化

> 集成阿里巴巴开源的 page-agent，实现自然语言控制网页界面

## 技能说明

**page-agent** 是一个运行在浏览器页面内的 JavaScript GUI Agent，可以通过自然语言控制网页界面。

### 核心特性

- ✅ **无需浏览器扩展** - 纯 JavaScript 实现，直接在页面内运行
- ✅ **文本 DOM 操作** - 不需要截图或多模态 LLM
- ✅ **自带 LLM** - 支持自定义模型（通义千问等）
- ✅ **可选 Chrome 扩展** - 支持多页面任务
- ✅ **MCP Server** - 可从外部控制浏览器

### 使用场景

- SaaS AI Copilot - 快速在产品中集成 AI 助手
- 智能表单填写 - 将复杂操作简化为一句话
- 无障碍访问 - 通过自然语言操作任何网页应用
- 多页面 Agent - 跨标签页自动化任务

## 安装方式

### 方式一：CDN 快速集成（推荐用于测试）

```html
<script src="https://cdn.jsdelivr.net/npm/page-agent@1.7.0/dist/iife/page-agent.demo.js" crossorigin="true"></script>
```

> ⚠️ 注意：CDN 版本使用免费测试 LLM API，仅限技术评估

### 方式二：NPM 安装（生产环境）

```bash
npm install page-agent
```

```javascript
import { PageAgent } from 'page-agent'

const agent = new PageAgent({
    model: 'qwen3.5-plus',
    baseURL: 'https://dashscope.aliyuncs.com/compatible-mode/v1',
    apiKey: 'YOUR_API_KEY',
    language: 'zh-CN',
})

await agent.execute('点击登录按钮')
```

## OpenClaw 集成方案

### 方案一：Browser Tool 增强

在 OpenClaw 的 browser 工具中集成 page-agent，实现自然语言网页操作：

```javascript
// 在 browser 工具中注入 page-agent
const script = document.createElement('script');
script.src = 'https://cdn.jsdelivr.net/npm/page-agent@1.7.0/dist/iife/page-agent.demo.js';
script.crossOrigin = 'true';
document.head.appendChild(script);

// 等待加载完成后初始化
script.onload = async () => {
    const agent = new PageAgent({
        model: 'qwen3.5-plus',
        baseURL: 'https://dashscope.aliyuncs.com/compatible-mode/v1',
        apiKey: process.env.DASHSCOPE_API_KEY,
        language: 'zh-CN',
    });
    
    // 暴露给 OpenClaw 调用
    window.pageAgent = agent;
};
```

### 方案二：Canvas 集成

通过 Canvas 工具在网页上下文中执行 page-agent：

```javascript
// 使用 canvas eval 注入并执行
await canvas({
    action: 'eval',
    javaScript: `
        // 注入 page-agent
        const script = document.createElement('script');
        script.src = 'https://cdn.jsdelivr.net/npm/page-agent@1.7.0/dist/iife/page-agent.demo.js';
        document.head.appendChild(script);
        
        // 等待并执行命令
        await new Promise(resolve => {
            script.onload = async () => {
                const agent = new PageAgent({
                    model: 'qwen3.5-plus',
                    baseURL: 'https://dashscope.aliyuncs.com/compatible-mode/v1',
                    apiKey: '${process.env.DASHSCOPE_API_KEY}',
                    language: 'zh-CN',
                });
                
                const result = await agent.execute('${command}');
                resolve(JSON.stringify(result));
            };
        });
    `
});
```

### 方案三：独立 Skill

创建专用的 page-agent skill，提供以下命令：

```markdown
## 命令

- `page-agent execute <指令>` - 执行网页操作指令
- `page-agent navigate <URL>` - 导航到指定页面并执行
- `page-agent status` - 查看 Agent 状态

## 示例

- `page-agent execute 点击登录按钮`
- `page-agent execute 填写表单：用户名 admin，密码 123456`
- `page-agent navigate https://example.com 然后 点击注册`
```

## API 参考

### PageAgent 构造函数

```javascript
const agent = new PageAgent({
    model: string,           // 模型名称，如 'qwen3.5-plus'
    baseURL: string,         // API 基础 URL
    apiKey: string,          // API 密钥
    language: string,        // 语言，如 'zh-CN' 或 'en-US'
    maxSteps?: number,       // 最大执行步骤（可选）
    timeout?: number,        // 超时时间（可选）
});
```

### 主要方法

| 方法 | 说明 | 示例 |
|------|------|------|
| `execute(command)` | 执行自然语言指令 | `await agent.execute('点击登录按钮')` |
| `navigate(url)` | 导航到指定 URL | `await agent.navigate('https://example.com')` |
| `getStatus()` | 获取 Agent 状态 | `await agent.getStatus()` |
| `reset()` | 重置 Agent 状态 | `await agent.reset()` |

### 返回结果

```javascript
{
    success: boolean,      // 是否成功
    result: any,           // 执行结果
    steps: number,         // 执行步数
    duration: number,      // 耗时（毫秒）
    error?: string         // 错误信息（如果有）
}
```

## 配置示例

### openclaw.json 配置

```json
{
  "tools": {
    "page-agent": {
      "enabled": true,
      "config": {
        "model": "qwen3.5-plus",
        "baseURL": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "apiKey": "$env:DASHSCOPE_API_KEY",
        "language": "zh-CN",
        "maxSteps": 10,
        "timeout": 30000
      }
    }
  }
}
```

## 注意事项

1. **API 密钥安全** - 不要将 API 密钥硬编码在代码中，使用环境变量
2. **CDN 限制** - 免费测试 API 仅限技术评估，生产环境请使用自己的 API
3. **跨域问题** - 确保目标页面允许跨域脚本注入
4. **性能考虑** - 复杂操作可能耗时较长，建议设置合理的超时时间
5. **错误处理** - 始终捕获并处理可能的错误

## 相关资源

- 📖 [官方文档](https://alibaba.github.io/page-agent/docs/introduction/overview)
- 🚀 [在线 Demo](https://alibaba.github.io/page-agent/)
- 🐙 [GitHub 仓库](https://github.com/alibaba/page-agent)
- 💬 [HackerNews 讨论](https://news.ycombinator.com/item?id=47264138)

## 版本信息

- 当前版本：1.7.0
- 许可证：MIT
- 最后更新：2026-04-02
