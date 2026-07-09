import os
import json
import glob
import sys
import jsonschema

def parse_frontmatter(text):
    if not text.startswith("---"):
        return None
    end = text.find("---", 3)
    if end == -1:
        return None
    import yaml
    try:
        return yaml.safe_load(text[3:end])
    except Exception as e:
        print(f"YAML Parse error: {e}")
        return None

def validate_skills():
    schema_path = os.path.join(os.path.dirname(__file__), "skill_schema.json")
    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)
    
    skills_dir = os.path.join(os.path.dirname(__file__), "..", "skills")
    errors = 0
    for root, dirs, files in os.walk(skills_dir):
        if "SKILL.md" in files:
            skill_md = os.path.join(root, "SKILL.md")
            with open(skill_md, "r", encoding="utf-8") as f:
                content = f.read()
            fm = parse_frontmatter(content)
            if fm is None:
                print(f"Error: {skill_md} has invalid frontmatter")
                errors += 1
                continue
            try:
                jsonschema.validate(instance=fm, schema=schema)
            except jsonschema.exceptions.ValidationError as err:
                print(f"Schema Error in {skill_md}: {err.message}")
                errors += 1
    
    if errors > 0:
        print(f"Validation failed with {errors} errors.")
        sys.exit(1)
    print("All skills passed schema validation.")

if __name__ == "__main__":
    validate_skills()
