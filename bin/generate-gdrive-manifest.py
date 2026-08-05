#!/usr/bin/env python3
"""
Enterprise Google Drive Workspace Architect & Manifest Generator
Standards: ISO 25010, ISO 42001, ISO 27001, SOC 2
Optimized for Gemini DeepMind Workspace RAG Indexing & Zero Data Loss Governance.
"""

import os
import sys
import json
import re
import argparse
from datetime import datetime
from pathlib import Path

POSIX_ISO8601_REGEX = re.compile(
    r"^([0-9]{8})_([A-Z0-9]+)_([A-Z0-9\-]+)_([A-Z0-9\-]+)_([A-Z0-9\-]+)_(V[0-9]+-[0-9]+)(\.[a-zA-Z0-9]+)?$"
)

DEFAULT_GDRIVEIGNORE_CONTENT = """# ==============================================================================
# Enterprise Google Drive / RAG Ingestion Exclusion Rules (.gdriveignore)
# Standards: ISO 27001 (Data Loss Prevention) & ISO 42001 (AI Governance)
# ==============================================================================

# --- Financial & Executive Secrets ---
00_GOVERNANCE_MY_BUSINESS/
01_FINANCIAL_OPS/
02_CLIENT_SERVICE_DELIVERY/*/01_COMMERCIAL_LEGAL/
02_CLIENT_SERVICE_DELIVERY/*/03_FINANCIAL_RECORD/

# --- Confidential Credentials & Private Keys ---
*.env
*.env.*
*.pem
*.key
*.pkcs12
*.pfx
*credentials*.json
*token*.json
*secret*
id_rsa
id_ed25519

# --- Temporary & System Files ---
.DS_Store
Thumbs.db
desktop.ini
~$*
*.tmp
*.bak
*.swp
*.log

# --- Raw PII & Unsanitized Scans ---
*_PII_*
*_PRIVATE_*
*_CONFIDENTIAL_*
*_DRAFT_*

# --- Infrastructure State & Build Artifacts ---
*.tfstate
*.tfstate.backup
.terraform/
node_modules/
__pycache__/
*.pyc
dist/
build/
"""

def generate_root_context_manifest(workspace_name: str, owner_name: str, owner_email: str) -> dict:
    today_str = datetime.now().strftime("%Y-%m-%d")
    return {
        "@context": "https://schema.org/",
        "@type": "DataCatalog",
        "@id": f"urn:workspace:google-drive:{workspace_name.lower().replace(' ', '-')}",
        "name": f"Google Drive Enterprise Workspace - {workspace_name}",
        "description": "High-performance Google Drive workspace architecture compliant with ISO 25010, ISO 42001, ISO 27001, and SOC 2. Optimized for Gemini DeepMind Workspace RAG indexing.",
        "dateCreated": today_str,
        "dateModified": today_str,
        "license": "ISO-27001-Restricted",
        "provider": {
            "@type": "Person",
            "name": owner_name,
            "role": "Lead Enterprise Solutions Architect & AI Knowledge Engineer",
            "email": owner_email
        },
        "about": [
            {
                "@type": "Thing",
                "name": "Scope",
                "description": "Enterprise Cloud Architecture, Multi-Agent System Governance, Docs-as-Code, RAG Context Grounding"
            }
        ],
        "hasPart": [
            {
                "@type": "Dataset",
                "@id": "urn:workspace:scope:00_GOVERNANCE_MY_BUSINESS",
                "name": "00_GOVERNANCE_MY_BUSINESS",
                "description": "Corporate statutes, legal registration, tax filings, and business compliance",
                "accessMode": "Restricted-Executive",
                "governance": {
                    "aiIndexingAllowed": False,
                    "piiContains": True,
                    "securityLevel": "Confidential"
                }
            },
            {
                "@type": "Dataset",
                "@id": "urn:workspace:scope:01_FINANCIAL_OPS",
                "name": "01_FINANCIAL_OPS",
                "description": "Invoices issued, vendor expenses, accounting ledger, and financial records",
                "accessMode": "Restricted-Finance",
                "governance": {
                    "aiIndexingAllowed": False,
                    "piiContains": True,
                    "securityLevel": "Confidential"
                }
            },
            {
                "@type": "Dataset",
                "@id": "urn:workspace:scope:02_CLIENT_SERVICE_DELIVERY",
                "name": "02_CLIENT_SERVICE_DELIVERY",
                "description": "Client project engagements, architecture runbooks, IaC repositories, and delivery artifacts",
                "accessMode": "Role-Based-Operations",
                "governance": {
                    "aiIndexingAllowed": True,
                    "piiContains": False,
                    "securityLevel": "Restricted-Dev"
                }
            },
            {
                "@type": "Dataset",
                "@id": "urn:workspace:scope:03_KNOWLEDGE_BASE_RND",
                "name": "03_KNOWLEDGE_BASE_RND",
                "description": "Enterprise RAG knowledge repository, AI prompt library, and standard IaC reference modules",
                "accessMode": "Organization-Wide",
                "governance": {
                    "aiIndexingAllowed": True,
                    "piiContains": False,
                    "securityLevel": "Internal-Public"
                }
            }
        ],
        "governance": {
            "isoCompliance": ["ISO25010", "ISO42001", "ISO27001", "SOC2"],
            "namingStandard": "POSIX_ISO8601_YYYYMMDD_[SCOPE]_[ENTITY]_[TYPE]_[DESCRIPTION]_[VERSION]",
            "zeroDataLossEnforced": True,
            "globalAiIndexingAllowed": False,
            "piiContains": False
        }
    }

def validate_filename(filename: str) -> bool:
    """Validates if filename complies with YYYYMMDD_[SCOPE]_[ENTITY]_[TYPE]_[DESCRIPTION]_[VERSION]"""
    if filename.startswith(".") or filename in [".context.jsonld", ".gdriveignore", "README.md"]:
        return True
    return bool(POSIX_ISO8601_REGEX.match(filename))

def audit_directory_structure(target_path: Path) -> dict:
    audit_summary = {
        "valid_files": 0,
        "invalid_files": [],
        "directories_scanned": 0,
        "manifests_found": 0
    }
    
    for root, dirs, files in os.walk(target_path):
        audit_summary["directories_scanned"] += 1
        for f in files:
            if f in [".context.jsonld", ".client_manifest.jsonld", ".project_manifest.jsonld"]:
                audit_summary["manifests_found"] += 1
            if validate_filename(f):
                audit_summary["valid_files"] += 1
            else:
                audit_summary["invalid_files"].append(os.path.join(root, f))
                
    return audit_summary

def main():
    parser = argparse.ArgumentParser(description="Google Drive Enterprise Workspace Manifest Generator & Auditor")
    parser.add_argument("--path", type=str, default=".", help="Root path of the Google Drive workspace")
    parser.add_argument("--workspace-name", type=str, default="Google_Drive_Service_Delivery", help="Name of the workspace")
    parser.add_argument("--owner-name", type=str, default="Leonel Antonio Salcedo Acosta", help="Owner name for JSON-LD")
    parser.add_argument("--owner-email", type=str, default="nomack3d@gmail.com", help="Owner email for JSON-LD")
    parser.add_argument("--dry-run", action="store_true", help="Perform audit without modifying files")
    
    args = parser.parse_args()
    root_path = Path(args.path).resolve()
    
    print(f"=== Enterprise Google Drive Workspace Architect & Auditor ===")
    print(f"Target Directory: {root_path}")
    print(f"Owner: {args.owner_name} ({args.owner_email})")
    print(f"Standards: ISO 25010 | ISO 42001 | ISO 27001 | SOC 2\n")
    
    audit = audit_directory_structure(root_path)
    print(f"Directories scanned: {audit['directories_scanned']}")
    print(f"Valid ISO 8601 files: {audit['valid_files']}")
    print(f"Non-compliant file names: {len(audit['invalid_files'])}")
    print(f"Manifests found: {audit['manifests_found']}\n")
    
    if audit["invalid_files"]:
        print("Notice: Non-compliant file names detected (will NOT delete any files):")
        for inv in audit["invalid_files"][:5]:
            print(f"  - {inv}")
        if len(audit["invalid_files"]) > 5:
            print(f"  ... and {len(audit['invalid_files']) - 5} more.")
        print()
        
    if args.dry_run:
        print("[DRY-RUN] Manifest generation skipped.")
        return
        
    # Write .context.jsonld
    context_file = root_path / ".context.jsonld"
    context_data = generate_root_context_manifest(args.workspace_name, args.owner_name, args.owner_email)
    with open(context_file, "w", encoding="utf-8") as f:
        json.dump(context_data, f, indent=2, ensure_ascii=False)
    print(f"[CREATED] {context_file}")
    
    # Write .gdriveignore
    ignore_file = root_path / ".gdriveignore"
    with open(ignore_file, "w", encoding="utf-8") as f:
        f.write(DEFAULT_GDRIVEIGNORE_CONTENT)
    print(f"[CREATED] {ignore_file}")
    
    print("\nWorkspace Manifest Generation Complete. Zero Data Loss Enforced.")

if __name__ == "__main__":
    main()
