import os
import json
from datetime import datetime

def build_index():
    repo_root = os.path.join(os.path.dirname(__file__), "..")
    skills_dir = os.path.join(repo_root, "skills")
    
    skills_list = []
    
    for root, dirs, files in os.walk(skills_dir):
        if "SKILL.md" in files:
            skill_md = os.path.join(root, "SKILL.md")
            with open(skill_md, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Simple parse
            name = ""
            desc = ""
            domain = ""
            if "name:" in content:
                name = content.split("name:")[1].split("\n")[0].strip().strip('"').strip("'")
            if "description:" in content:
                desc = content.split("description:")[1].split("\n")[0].strip().strip('"').strip("'")
            if "domain:" in content:
                domain = content.split("domain:")[1].split("\n")[0].strip().strip('"').strip("'")
            
            # Subpath from repo root
            rel_path = os.path.relpath(root, repo_root).replace("\\", "/")
            
            skills_list.append({
                "name": name,
                "description": desc,
                "domain": domain,
                "path": rel_path
            })
    
    index_data = {
        "version": "1.1.0",
        "generated_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "domain": "cybersecurity",
        "total_skills": len(skills_list),
        "skills": sorted(skills_list, key=lambda x: x["name"])
    }
    
    index_path = os.path.join(repo_root, "index.json")
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index_data, f, indent=0, separators=(',', ':')) # Minified like original
    
    print(f"Index built successfully with {len(skills_list)} skills.")

if __name__ == "__main__":
    build_index()
