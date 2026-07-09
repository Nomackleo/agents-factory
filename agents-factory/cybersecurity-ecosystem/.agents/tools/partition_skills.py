import os
import shutil
import json

def partition_skills():
    repo_root = os.path.join(os.path.dirname(__file__), "..")
    skills_dir = os.path.join(repo_root, "skills")
    index_path = os.path.join(repo_root, "index.json")
    
    with open(index_path, "r", encoding="utf-8") as f:
        index_data = json.load(f)
    
    moved_count = 0
    for skill in index_data.get("skills", []):
        skill_name = skill.get("name")
        if not skill_name:
            continue
        
        # Determine target folder. Using a heuristic or sub-domain mapping.
        # For simplicity, we can just group by alphabetical or broad categories based on keywords.
        # Since 'subdomain' is not present in index.json, we parse SKILL.md.
        
        old_path = os.path.join(skills_dir, skill_name)
        if not os.path.exists(old_path):
            continue
            
        skill_md = os.path.join(old_path, "SKILL.md")
        subdomain = "uncategorized"
        
        if os.path.exists(skill_md):
            with open(skill_md, "r", encoding="utf-8") as f:
                content = f.read()
                
            if "subdomain:" in content:
                subdomain = content.split("subdomain:")[1].split("\n")[0].strip().strip('"').strip("'")
        
        target_dir = os.path.join(skills_dir, subdomain)
        os.makedirs(target_dir, exist_ok=True)
        
        new_path = os.path.join(target_dir, skill_name)
        
        if old_path != new_path:
            shutil.move(old_path, new_path)
            moved_count += 1
            
    print(f"Partitioned {moved_count} skills into subdomain folders.")

if __name__ == "__main__":
    partition_skills()
