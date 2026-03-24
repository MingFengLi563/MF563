#!/usr/bin/env python3
"""
Figma 页面复制与修改工具
核心原则：不修改原页面，只创建副本进行修改
"""

import json
import requests
from typing import Dict, List, Optional, Any
from figma_client import FigmaClient, load_config


class FigmaCopier:
    def __init__(self, client: FigmaClient, config: Dict):
        self.client = client
        self.config = config
        self.team_id = config.get("team_id")
    
    def duplicate_file(self, source_file_id: str, new_name: str) -> Dict:
        """复制整个文件"""
        if not self.team_id:
            raise ValueError("配置中缺少 team_id，无法复制文件")
        
        return self.client.post_file_duplicate(source_file_id, new_name, self.team_id)
    
    def create_suggestion_copy(self, source_file_id: str, page_name: str, suggestion_summary: str) -> Dict:
        """创建建议副本"""
        # 清理名称中的非法字符
        safe_summary = suggestion_summary[:30].replace("/", "-").replace("\\", "-")
        new_name = f"{page_name} - AI 建议 {safe_summary}"
        
        return self.duplicate_file(source_file_id, new_name)
    
    def add_comment_to_original(self, file_id: str, node_id: Optional[str], message: str) -> Dict:
        """在原始文件添加评论（不修改设计）"""
        return self.client.post_comment(file_id, message, node_id)
    
    def export_page_preview(self, file_id: str, node_ids: List[str]) -> Dict:
        """导出页面预览图"""
        return self.client.get_images(file_id, node_ids, scale=2)
    
    def get_modification_plan(self, source_analysis: Dict, user_request: str) -> Dict:
        """生成修改计划（不执行，仅规划）"""
        return {
            "source_file": source_analysis.get("file_id"),
            "source_pages": [p.get("page_name") for p in source_analysis.get("pages", [])],
            "requested_changes": user_request,
            "plan": {
                "step1": "复制目标页面创建副本",
                "step2": "在副本上应用修改",
                "step3": "添加评论说明修改内容",
                "step4": "输出对比报告"
            },
            "note": "所有修改都在副本中进行，原始文件不受影响"
        }


def copy_and_modify(
    config_path: str,
    source_file_id: Optional[str],
    page_name: str,
    modification_request: str
) -> Dict:
    """复制并修改页面主函数"""
    config = load_config(config_path)
    client = FigmaClient(config["access_token"])
    copier = FigmaCopier(client, config)
    
    target_file = source_file_id or config.get("default_file_id")
    if not target_file:
        raise ValueError("未指定文件 ID")
    
    # 步骤 1: 获取原始文件信息
    file_data = client.get_file(target_file)
    
    # 步骤 2: 创建副本
    copy_result = copier.create_suggestion_copy(target_file, page_name, modification_request)
    new_file_id = copy_result.get("file", {}).get("key")
    new_file_url = copy_result.get("file", {}).get("url")
    
    # 步骤 3: 在原始文件添加评论
    comment_message = f"🦖 AI 已创建修改建议副本：{page_name} - AI 建议\n修改需求：{modification_request}\n新文件：{new_file_url}"
    copier.add_comment_to_original(target_file, None, comment_message)
    
    return {
        "status": "success",
        "original_file": target_file,
        "new_file_id": new_file_id,
        "new_file_url": new_file_url,
        "modification_request": modification_request,
        "next_steps": [
            "在新文件中查看 AI 建议的修改",
            "满意后可手动应用到原文件",
            "不满意可删除副本或提出新需求"
        ]
    }


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 4:
        print("用法：python copier.py <config_path> <file_id> <page_name> <modification_request>")
        sys.exit(1)
    
    config_path = sys.argv[1]
    file_id = sys.argv[2]
    page_name = sys.argv[3]
    modification_request = sys.argv[4] if len(sys.argv) > 4 else "通用优化"
    
    try:
        result = copy_and_modify(config_path, file_id, page_name, modification_request)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"❌ 操作失败：{e}")
        sys.exit(1)
