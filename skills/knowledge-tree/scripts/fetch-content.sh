#!/usr/bin/env bash
#
# 知识内容抓取脚本
# 支持：微信推文、通用网页
#

set -euo pipefail

URL="$1"

if [[ -z "$URL" ]]; then
    echo "❌ 请提供 URL 链接"
    exit 1
fi

# 检测链接类型
if [[ "$URL" == *"mp.weixin.qq.com"* ]]; then
    echo "📱 检测到微信推文..."
elif [[ "$URL" == *"xiaohongshu.com"* ]] || [[ "$URL" == *"xhslink.com"* ]]; then
    echo "📕 检测到小红书链接（可能需要截图）..."
else
    echo "🌐 检测到通用网页..."
fi

# 使用 web_fetch 抓取内容
# 注意：实际执行由 OpenClaw 工具完成
echo "✅ 链接已提交，正在抓取内容..."
echo ""
echo "URL: $URL"
