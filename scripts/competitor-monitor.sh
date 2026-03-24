#!/bin/bash
# 竞品监控日报脚本
# 每天 18:00 执行，检查竞品官网和博客更新

DATE=$(date +%Y-%m-%d)
REPORT_FILE="/home/admin/.openclaw/workspace/competitor-reports/$DATE.md"
BASELINE_FILE="/home/admin/.openclaw/workspace/competitor-baseline.json"

mkdir -p /home/admin/.openclaw/workspace/competitor-reports

# 初始化报告
cat > "$REPORT_FILE" << EOF
# 📊 竞品监控日报 - $DATE

**监控技能**: browser + web_fetch
**监控时间**: ${DATE} 18:00 (Asia/Shanghai)

---

EOF

# 竞品列表
declare -A COMPETITORS=(
    ["Intercom"]="https://www.intercom.com/blog/"
    ["Respond.io"]="https://respond.io/blog/"
    ["SleekFlow"]="https://sleekflow.io/blog/"
    ["Pancake"]="https://pancake.chat/blog/"
    ["Tidio"]="https://www.tidio.com/blog/"
    ["ManyChat"]="https://www.manychat.com/blog"
    ["Mixdesk"]="https://mixdesk.com/blog/"
    ["OKKICRM"]="https://www.okkicrm.com/blog/"
)

echo "## 🔍 竞品更新检查" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# 检查每个竞品
for name in "${!COMPETITORS[@]}"; do
    url="${COMPETITORS[$name]}"
    echo "### $name" >> "$REPORT_FILE"
    echo "- 博客地址：$url" >> "$REPORT_FILE"
    echo "- 检查状态：待检查" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
done

echo "---" >> "$REPORT_FILE"
echo "**注**: 详细检查通过 browser 技能执行，此为占位报告。" >> "$REPORT_FILE"

echo "报告已生成：$REPORT_FILE"
