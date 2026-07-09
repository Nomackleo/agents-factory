import os
import shutil
import re

def convert_and_move():
    source_skills_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "skills"))
    ecosystem_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "agents-factory", "cybersecurity-ecosystem"))
    target_skills_dir = os.path.join(ecosystem_dir, ".agents", "skills")
    
    os.makedirs(target_skills_dir, exist_ok=True)
    
    moved_count = 0
    
    for root, dirs, files in os.walk(source_skills_dir):
        if "SKILL.md" in files:
            skill_md = os.path.join(root, "SKILL.md")
            
            # Read content
            with open(skill_md, "r", encoding="utf-8") as f:
                content = f.read()
                
            # Parse frontmatter vs body
            if not content.startswith("---"):
                continue
            
            end_fm = content.find("---", 3)
            if end_fm == -1:
                continue
                
            frontmatter = content[:end_fm+3]
            body = content[end_fm+3:].strip()
            
            # Convert body to Neo-CRISPE
            crispe_body = f"""
<instruction>
{body}
</instruction>

<knowledge>
<!-- PENDING: Alimentación de ISO standards, playbooks y referencias ATT&CK/D3FEND -->
</knowledge>

<examples>
<!-- PENDING: Ejemplos de ejecución y comandos -->
</examples>
"""
            new_content = frontmatter + "\n" + crispe_body + "\n"
            
            # Calculate target path
            rel_path = os.path.relpath(root, source_skills_dir)
            target_dir = os.path.join(target_skills_dir, rel_path)
            os.makedirs(target_dir, exist_ok=True)
            
            target_skill_md = os.path.join(target_dir, "SKILL.md")
            
            with open(target_skill_md, "w", encoding="utf-8") as f:
                f.write(new_content)
                
            moved_count += 1

    print(f"Migrated and converted {moved_count} skills to Neo-CRISPE in {target_skills_dir}")

if __name__ == "__main__":
    convert_and_move()
