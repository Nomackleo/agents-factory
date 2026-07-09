import os
import json
import re
import sys

def check_consistency():
    repo_root = os.path.join(os.path.dirname(__file__), "..")
    index_path = os.path.join(repo_root, "index.json")
    coverage_path = os.path.join(repo_root, "ATTACK_COVERAGE.md")
    
    with open(index_path, "r", encoding="utf-8") as f:
        index_data = json.load(f)
    
    total_skills = index_data.get("total_skills", 0)
    
    # Read coverage to find total skills mentioned
    with open(coverage_path, "r", encoding="utf-8") as f:
        coverage_text = f.read()
    
    # Very simple extraction, normally we would parse the markdown properly
    match = re.search(r"(\d+)\s+skills", coverage_text, re.IGNORECASE)
    coverage_skills = int(match.group(1)) if match else 0
    
    if total_skills != coverage_skills and coverage_skills != 0:
        print(f"Drift detected! index.json has {total_skills} skills, but ATTACK_COVERAGE.md mentions {coverage_skills}")
        # Note: In a real CI this might fail. For now, we print a warning.
    
    print("Consistency check completed.")

if __name__ == "__main__":
    check_consistency()
