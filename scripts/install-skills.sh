#!/bin/bash

# 技能安装队列脚本
# 每 30 分钟执行一次，安装一个技能并通知飞书

SKILLS_DIR="/home/admin/.openclaw/workspace/skills"
QUEUE_FILE="/home/admin/.openclaw/workspace/skill-install-queue.json"
LOG_FILE="/home/admin/.openclaw/workspace/skill-install.log"

# 技能安装队列
SKILLS=(
    "feishu-bitable"
    "feishu-doc-manager"
    "feishu-messaging"
    "translate"
    "user-feedback-analyzer"
    "prd-generator"
    "competitor-tracker"
)

# 读取当前安装进度
if [ -f "$QUEUE_FILE" ]; then
    CURRENT_INDEX=$(cat "$QUEUE_FILE" | grep -o '"index":[0-9]*' | cut -d':' -f2)
    if [ -z "$CURRENT_INDEX" ]; then
        CURRENT_INDEX=0
    fi
else
    CURRENT_INDEX=0
    echo '{"index":0,"installed":[]}' > "$QUEUE_FILE"
fi

# 检查是否所有技能都已安装
if [ $CURRENT_INDEX -ge ${#SKILLS[@]} ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] 所有技能已安装完成！" >> "$LOG_FILE"
    exit 0
fi

# 获取当前要安装的技能
CURRENT_SKILL=${SKILLS[$CURRENT_INDEX]}

echo "[$(date '+%Y-%m-%d %H:%M:%S')] 开始安装：$CURRENT_SKILL (进度：$((CURRENT_INDEX + 1))/${#SKILLS[@]})" >> "$LOG_FILE"

# 切换到工作目录
cd /home/admin/.openclaw/workspace

# 尝试安装技能
OUTPUT=$(clawhub install "$CURRENT_SKILL" 2>&1)
EXIT_CODE=$?

# 记录日志
echo "$OUTPUT" >> "$LOG_FILE"

if [ $EXIT_CODE -eq 0 ]; then
    # 安装成功
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ✅ 安装成功：$CURRENT_SKILL" >> "$LOG_FILE"
    
    # 更新进度
    NEXT_INDEX=$((CURRENT_INDEX + 1))
    echo "{\"index\":$NEXT_INDEX,\"installed\":[\"$CURRENT_SKILL\"]}" > "$QUEUE_FILE"
    
    # 发送飞书通知
    cat << EOF
✅ 技能安装成功

**技能名称**: $CURRENT_SKILL
**安装进度**: $((NEXT_INDEX))/${#SKILLS[@]}
**安装时间**: $(date '+%Y-%m-%d %H:%M:%S')

剩余技能：
$(for i in $(seq $NEXT_INDEX $((${#SKILLS[@]} - 1))); do echo "- ${SKILLS[$i]}"; done)

下次安装将在 30 分钟后自动执行。
EOF
else
    # 安装失败
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ❌ 安装失败：$CURRENT_SKILL" >> "$LOG_FILE"
    echo "错误信息：$OUTPUT" >> "$LOG_FILE"
    
    # 发送飞书通知
    cat << EOF
⚠️ 技能安装失败

**技能名称**: $CURRENT_SKILL
**错误信息**: 速率限制或其他错误
**安装时间**: $(date '+%Y-%m-%d %H:%M:%S')

将在 30 分钟后重试。
EOF
fi
