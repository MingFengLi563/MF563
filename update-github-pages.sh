#!/bin/bash
# Mission Control 自动更新脚本

cd /home/admin/.openclaw/workspace/github-pages

# 更新文件
cp ../mission-control.html index.html

# 检查是否有变化
if git diff --quiet index.html; then
    echo "ℹ️  无变化，跳过更新"
    exit 0
fi

# 提交并推送
git add index.html
git commit -m "Auto-update: $(date +%Y-%m-%d %H:%M)"
git push origin gh-pages

echo "✅ 已更新并推送到 GitHub Pages"
echo "🌐 访问：https://mingfengli563.github.io/MF563/"
