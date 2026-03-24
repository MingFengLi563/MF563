#!/usr/bin/env python3
"""
Figma 原型分析器
分析原型结构，对比同类产品，生成修改建议
"""

import json
from typing import Dict, List, Any, Optional
from figma_client import FigmaClient, load_config


class FigmaAnalyzer:
    def __init__(self, client: FigmaClient):
        self.client = client
    
    def extract_page_structure(self, file_data: Dict) -> List[Dict]:
        """提取页面结构信息"""
        pages = []
        document = file_data.get("document", {})
        
        def traverse(node: Dict, depth: int = 0):
            if node.get("type") == "CANVAS":
                page_info = {
                    "id": node.get("id"),
                    "name": node.get("name"),
                    "type": "page",
                    "depth": depth,
                    "children": [],
                    "component_count": 0,
                    "frame_count": 0,
                    "text_elements": []
                }
                
                for child in node.get("children", []):
                    child_info = traverse(child, depth + 1)
                    if child_info:
                        page_info["children"].append(child_info)
                        if child_info.get("type") == "COMPONENT":
                            page_info["component_count"] += 1
                        elif child_info.get("type") == "FRAME":
                            page_info["frame_count"] += 1
                        if child_info.get("type") == "TEXT":
                            page_info["text_elements"].append({
                                "content": child_info.get("characters", ""),
                                "style": child_info.get("style", {})
                            })
                
                pages.append(page_info)
                return page_info
            elif node.get("children"):
                for child in node.get("children", []):
                    traverse(child, depth + 1)
            
            return {
                "id": node.get("id"),
                "name": node.get("name"),
                "type": node.get("type"),
                "depth": depth
            }
        
        traverse(document)
        return pages
    
    def analyze_page(self, page_info: Dict) -> Dict:
        """分析单个页面的功能完整性"""
        analysis = {
            "page_name": page_info.get("name"),
            "frame_count": page_info.get("frame_count", 0),
            "component_count": page_info.get("component_count", 0),
            "text_element_count": len(page_info.get("text_elements", [])),
            "potential_issues": [],
            "suggestions": []
        }
        
        # 检查常见问题
        if analysis["frame_count"] == 0:
            analysis["potential_issues"].append("页面中没有 Frame，可能缺少内容布局")
        
        if analysis["text_element_count"] < 3:
            analysis["potential_issues"].append("文案元素较少，可能缺少说明文字或标签")
        
        # 提取文案关键词
        text_contents = [t.get("content", "") for t in page_info.get("text_elements", [])]
        all_text = " ".join(text_contents).lower()
        
        # 常见功能元素检查
        common_elements = {
            "搜索": ["搜索", "search", "查找"],
            "筛选": ["筛选", "filter", "排序"],
            "分页": ["分页", "page", "下一页", "上一页"],
            "操作按钮": ["确定", "取消", "保存", "删除", "编辑", "添加"],
            "导航": ["首页", "返回", "菜单", "导航"]
        }
        
        for element, keywords in common_elements.items():
            found = any(kw in all_text for kw in keywords)
            if not found:
                analysis["suggestions"].append(f"考虑添加 {element} 功能元素")
        
        return analysis
    
    def generate_comparison_report(self, page_analysis: Dict, product_type: str) -> Dict:
        """生成同类产品对比报告（需要联网搜索）"""
        # 这部分需要调用 web_search，在技能中由 AI 主导
        return {
            "product_type": product_type,
            "analyzed_page": page_analysis.get("page_name"),
            "note": "此部分需要 AI 联网搜索同类产品功能，生成对比建议"
        }
    
    def full_analysis(self, file_id: str) -> Dict:
        """完整分析流程"""
        file_data = self.client.get_file(file_id)
        pages = self.extract_page_structure(file_data)
        
        report = {
            "file_name": file_data.get("name"),
            "file_id": file_id,
            "total_pages": len(pages),
            "pages": []
        }
        
        for page in pages:
            analysis = self.analyze_page(page)
            report["pages"].append(analysis)
        
        return report


def analyze_prototype(config_path: str, file_id: Optional[str] = None) -> Dict:
    """分析原型主函数"""
    config = load_config(config_path)
    client = FigmaClient(config["access_token"])
    analyzer = FigmaAnalyzer(client)
    
    target_file = file_id or config.get("default_file_id")
    if not target_file:
        raise ValueError("未指定文件 ID，请在配置中设置 default_file_id 或传入参数")
    
    return analyzer.full_analysis(target_file)


if __name__ == "__main__":
    import sys
    config_path = sys.argv[1] if len(sys.argv) > 1 else "config.json"
    file_id = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        result = analyze_prototype(config_path, file_id)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"❌ 分析失败：{e}")
        sys.exit(1)
