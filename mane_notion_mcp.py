#!/usr/bin/env python3
"""
Mane Notion Connector via MCP
Enables Mane to read/write to Notion EIDRA Hub using Manus MCP
"""

import os
import json
import subprocess
from typing import Dict, List, Optional, Any
from datetime import datetime

class NotionMCP:
    """Connect Mane to Notion via MCP"""
    
    def __init__(self):
        self.server_name = "notion"
        print("✅ Notion MCP connector initialized")
    
    def _execute_mcp(self, tool_name: str, args: Dict[str, Any]) -> Dict:
        """Execute MCP command"""
        try:
            args_json = json.dumps(args)
            cmd = f"manus-mcp-cli tool call {tool_name} --server {self.server_name} --input '{args_json}'"
            
            result = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                # Try to parse JSON output
                try:
                    data = json.loads(result.stdout) if result.stdout.strip() else {}
                except:
                    data = {"raw_output": result.stdout}
                
                return {
                    "success": True,
                    "output": result.stdout,
                    "data": data
                }
            else:
                return {
                    "success": False,
                    "error": result.stderr or "MCP command failed",
                    "stdout": result.stdout
                }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def search(self, query: str, query_type: str = "internal", limit: int = 10) -> Dict:
        """Search Notion workspace"""
        return self._execute_mcp("search", {
            "query": query,
            "query_type": query_type
        })
    
    def fetch(self, page_id: str) -> Dict:
        """Fetch Notion page or database content"""
        return self._execute_mcp("fetch", {
            "id": page_id
        })
    
    def create_page(self, title: str, content: str = "", parent_page_id: str = None, parent_data_source_id: str = None) -> Dict:
        """Create new Notion page"""
        page_data = {
            "properties": {"title": title}
        }
        
        if content:
            page_data["content"] = content
        
        args = {"pages": [page_data]}
        
        # Add parent if specified
        if parent_page_id:
            args["parent"] = {"page_id": parent_page_id}
        elif parent_data_source_id:
            args["parent"] = {"data_source_id": parent_data_source_id}
        
        return self._execute_mcp("notion-create-pages", args)
    
    def update_page(self, page_id: str, content: str) -> Dict:
        """Update Notion page content"""
        return self._execute_mcp("notion-update-page", {
            "page_id": page_id,
            "content": content
        })
    
    def create_database_page(self, data_source_id: str, properties: Dict) -> Dict:
        """Create page in Notion database"""
        return self._execute_mcp("notion-create-pages", {
            "parent": {"data_source_id": data_source_id},
            "pages": [{"properties": properties}]
        })
    
    def get_users(self) -> Dict:
        """Get list of Notion users"""
        return self._execute_mcp("notion-get-users", {})
    
    def get_teams(self) -> Dict:
        """Get list of Notion teams"""
        return self._execute_mcp("notion-get-teams", {})
    
    # Convenience methods for EIDRA Triad
    
    def search_eidra(self) -> Dict:
        """Search for EIDRA-related pages"""
        return self.search("EIDRA")
    
    def write_memory_entry(self, title: str, content: str, tags: List[str] = None, parent_id: str = None) -> Dict:
        """Write a memory entry to Notion"""
        # Format content with tags
        formatted_content = content
        if tags:
            formatted_content = f"**Tags**: {', '.join(tags)}\n\n{formatted_content}"
        
        return self.create_page(
            title=f"Memory: {title}",
            content=formatted_content,
            parent_page_id=parent_id
        )
    
    def sync_daily_log(self, log_content: str, parent_id: str = None) -> Dict:
        """Sync daily log to Notion"""
        title = f"Daily Log - {datetime.now().strftime('%Y-%m-%d')}"
        return self.create_page(
            title=title,
            content=log_content,
            parent_page_id=parent_id
        )
    
    def save_project_doc(self, project_name: str, documentation: str, parent_id: str = None) -> Dict:
        """Save project documentation to Notion"""
        return self.create_page(
            title=f"Project: {project_name}",
            content=documentation,
            parent_page_id=parent_id
        )


if __name__ == "__main__":
    connector = NotionMCP()
    print("\n🧪 Testing Notion MCP connector...")
    
    # Test search
    print("\n🔍 Searching for EIDRA...")
    result = connector.search("EIDRA")
    print(json.dumps(result, indent=2))
    
    # Test getting users
    print("\n👥 Getting users...")
    result = connector.get_users()
    print(json.dumps(result, indent=2))

