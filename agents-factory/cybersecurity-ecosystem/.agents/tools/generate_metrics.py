import os
import json
import re

def generate_metrics():
    repo_root = os.path.join(os.path.dirname(__file__), "..")
    index_path = os.path.join(repo_root, "index.json")
    readme_path = os.path.join(repo_root, "README.md")
    
    with open(index_path, "r", encoding="utf-8") as f:
        index_data = json.load(f)
    
    total_skills = index_data.get("total_skills", 0)
    version = index_data.get("version", "1.1.0")
    
    # Read the README
    with open(readme_path, "r", encoding="utf-8") as f:
        readme_text = f.read()
    
    # Replace badges dynamically using regex
    # Assuming there's a badge like ![Skills](https://img.shields.io/badge/Skills-817-blue)
    readme_text = re.sub(
        r"!\[Skills\]\(https://img\.shields\.io/badge/Skills-\d+-blue\)",
        f"![Skills](https://img.shields.io/badge/Skills-{total_skills}-blue)",
        readme_text
    )
    
    readme_text = re.sub(
        r"!\[Version\]\(https://img\.shields\.io/badge/Version-v[\d\.]+-green\)",
        f"![Version](https://img.shields.io/badge/Version-v{version}-green)",
        readme_text
    )
    
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_text)
    
    print(f"Metrics generated and README updated. Total Skills: {total_skills}, Version: {version}")

if __name__ == "__main__":
    generate_metrics()
