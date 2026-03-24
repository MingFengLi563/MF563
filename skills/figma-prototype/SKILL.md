# Figma 原型助手技能

**私有技能** - 仅供当前用户使用

## 功能概述

本技能帮助产品经理通过 Figma API 实现原型的**读取、分析、复制和修改**，核心原则是**只读原文件，修改走副本**。

## 核心能力

### 1. 读取原型 (`read_prototype`)
- 读取 Figma 文件的页面结构、框架、组件
- 提取文案、样式、布局信息
- 输出结构化分析报告

### 2. 分析建议 (`analyze_and_suggest`)
- 分析当前原型的功能完整性
- 联网搜索同类产品的功能设计
- 生成补充和修改建议报告

### 3. 复制页面 (`duplicate_page`)
- 复制指定页面创建新版本
- 命名格式：`原页面名 - AI 建议 v1`
- 不影响原始页面内容

### 4. 修改副本 (`modify_copy`)
- 在副本上应用修改建议
- 支持修改：文案、颜色、组件属性、布局
- 可批量应用或逐项确认

## 配置方式

在 `~/.openclaw/workspace/skills/figma-prototype/config.json` 中配置：

```json
{
  "access_token": "figd_xxx_your_personal_access_token",
  "team_id": "123456789",
  "project_id": "987654321",
  "default_file_id": "111222333444"
}
```

### 获取 Figma Personal Access Token

1. 打开 Figma → 点击右上角头像 → **Account settings**
2. 滚动到 **Personal access tokens** 区域
3. 点击 **Create new token**
4. 输入描述（如 "StormClaw Assistant"）
5. 设置过期时间（建议 90 天）
6. 设置权限范围：
   - `files:read` - 读取文件内容
   - `files:write` - 创建/修改文件
   - `projects:read` - 读取项目
7. 复制生成的 Token（只显示一次！）

### 获取 Team/Project/File ID

- **Team ID**: 访问团队页面，URL 格式 `figma.com/files/team/123456789/...`
- **Project ID**: 访问项目页面，URL 格式 `figma.com/files/123456789/987654321/...`
- **File ID**: 访问文件页面，URL 格式 `figma.com/file/111222333444/...`

## 使用示例

### 示例 1：读取并分析原型
```
读取 Figma 文件 111222333444 的首页，分析功能完整性
```

### 示例 2：获取修改建议
```
分析这个登录页面的原型，对比市面主流产品，给出优化建议
```

### 示例 3：复制并修改
```
复制"用户列表页"，应用建议：增加搜索框和筛选条件
```

## 安全原则

1. **只读原文件** - 永不直接修改用户的原始页面
2. **副本命名清晰** - 所有修改都在 "AI 建议 vX" 副本中进行
3. **操作可追溯** - 每次修改记录日志
4. **配置本地存储** - Token 仅保存在本地 config.json

## 依赖

- Python 3.8+
- requests 库
- Figma REST API

## 故障排查

| 问题 | 解决方案 |
|------|----------|
| 403 Forbidden | 检查 Token 权限是否包含 files:write |
| 404 Not Found | 检查 File ID 是否正确，确认有访问权限 |
| Rate Limited | Figma API 限流，等待 1 分钟后重试 |
