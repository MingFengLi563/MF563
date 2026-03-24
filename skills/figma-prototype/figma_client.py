#!/usr/bin/env python3
"""
Figma API Client
封装 Figma REST API 核心操作
"""

import requests
import json
from typing import Optional, Dict, List, Any

class FigmaClient:
    def __init__(self, access_token: str):
        self.base_url = "https://api.figma.com/v1"
        self.headers = {
            "X-Figma-Token": access_token,
            "Content-Type": "application/json"
        }
    
    def get_file(self, file_id: str) -> Dict:
        """获取文件完整结构"""
        url = f"{self.base_url}/files/{file_id}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_file_nodes(self, file_id: str, ids: List[str]) -> Dict:
        """获取指定节点详情"""
        url = f"{self.base_url}/files/{file_id}/nodes"
        params = {"ids": ",".join(ids)}
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_images(self, file_id: str, node_ids: List[str], scale: int = 1) -> Dict:
        """获取节点预览图 URL"""
        url = f"{self.base_url}/images/{file_id}"
        params = {
            "ids": ",".join(node_ids),
            "scale": str(scale),
            "format": "png"
        }
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
    
    def post_file(self, name: str, team_id: str) -> Dict:
        """创建新文件"""
        url = f"{self.base_url}/teams/{team_id}/files"
        data = {"name": name}
        response = requests.post(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()
    
    def post_file_duplicate(self, file_id: str, name: str, team_id: str) -> Dict:
        """复制整个文件"""
        url = f"{self.base_url}/files/{file_id}/duplicate"
        data = {"name": name, "team_id": team_id}
        response = requests.post(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()
    
    def patch_component(self, file_id: str, node_id: str, changes: Dict) -> Dict:
        """修改节点属性（有限支持）"""
        # 注意：Figma API 对修改操作支持有限
        # 主要通过创建新文件/复制来实现"修改"
        url = f"{self.base_url}/files/{file_id}/components"
        # 实际修改需要通过创建变体或复制实现
        raise NotImplementedError("直接修改节点需要更复杂的操作，建议使用复制 + 新文件方式")
    
    def get_comments(self, file_id: str) -> Dict:
        """获取文件评论"""
        url = f"{self.base_url}/files/{file_id}/comments"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def post_comment(self, file_id: str, message: str, node_id: Optional[str] = None) -> Dict:
        """添加评论"""
        url = f"{self.base_url}/files/{file_id}/comments"
        data = {"message": message}
        if node_id:
            data["node_id"] = node_id
        response = requests.post(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()
    
    def get_project_files(self, project_id: str) -> Dict:
        """获取项目下所有文件"""
        url = f"{self.base_url}/projects/{project_id}/files"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_me(self) -> Dict:
        """获取当前用户信息"""
        url = f"{self.base_url}/me"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()


def load_config(config_path: str) -> Dict:
    """加载配置文件"""
    with open(config_path, 'r') as f:
        return json.load(f)


def create_client(config_path: str) -> FigmaClient:
    """从配置创建客户端"""
    config = load_config(config_path)
    if not config.get("access_token"):
        raise ValueError("配置文件中缺少 access_token，请先配置 Figma Personal Access Token")
    return FigmaClient(config["access_token"])


if __name__ == "__main__":
    # 测试连接
    import sys
    if len(sys.argv) > 1:
        config_path = sys.argv[1]
    else:
        config_path = "config.json"
    
    try:
        client = create_client(config_path)
        user = client.get_me()
        print(f"✅ 连接成功！当前用户：{user.get('handle', 'Unknown')}")
    except Exception as e:
        print(f"❌ 连接失败：{e}")
        sys.exit(1)
