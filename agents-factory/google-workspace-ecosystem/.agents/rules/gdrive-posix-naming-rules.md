# Google Drive POSIX & ISO 8601 Naming & Governance Rules

> [!CRITICAL]
> All files and project engagement subfolders within Google Drive MUST strictly follow the 6-token deterministic POSIX & ISO 8601 standard and the Universal Antigravity Governance policies.

## 1. Naming Format

```text
YYYYMMDD_[SCOPE]_[ENTITY]_[TYPE]_[DESCRIPTION]_[VERSION]
```

- **`YYYYMMDD`**: 8-digit ISO 8601 date timestamp representing the **TRUE original creation or presentation date** extracted from native Google Drive API RFC 3339 `createdTime` metadata (e.g., `20241212`, `20250703`). Do NOT use the reorganization execution date.
- **`[SCOPE]`**: Business domain (e.g., `GOV`, `FIN`, `COMM`, `ARCH`, `IAC`, `AI`, `TRN`, `REP`, `KNB`).
- **`[ENTITY]`**: Target client, company, or internal unit (e.g., `ACME-CORP`, `LA-LUPA-NEWS`, `GENESIS-LEGAL`).
- **`[TYPE]`**: Document or artifact type (e.g., `SPEC`, `CODE`, `PROMPT`, `MANUAL`, `STATUS`, `REC`, `NDA`, `SOW`, `PRES`, `RATE`, `INV`, `VAL`, `BUDGET`).
- **`[DESCRIPTION]`**: Clear, concise hyphen-separated description (e.g., `AWS-LANDING-ZONE`, `DIGITAL-TRANSFORMATION-PROPOSAL`).
- **`[VERSION]`**: Version tag using `V` and hyphenated major-minor (e.g., `V1-0`, `V2-1`).

## 2. Character & Separator Constraints

1. **Underscores `_`**: Used strictly as token field delimiters (must be exactly 5 underscores separating the 6 tokens).
2. **Hyphens `-`**: Used strictly for multi-word compounds within a single token (e.g., `AWS-MIGRATION`).
3. **No Spaces or Non-ASCII**: Spaces, special characters, accented characters, and non-ASCII symbols are strictly prohibited.
4. **Canonical Root Namespaces**: Root folders MUST remain static and numbered (e.g., `00_GOVERNANCE_MY_BUSINESS`, `01_FINANCIAL_OPS`, `02_CLIENT_SERVICE_DELIVERY`, `03_KNOWLEDGE_BASE_RND`).

## 3. Selective Renaming & Integrity Preservation Policy

1. **Service Delivery Documents**: Proposals, SOWs, contracts, audits, technical specs, and status reports provided by Solutions Architects / Consultants MUST be renamed using POSIX ISO 8601.
2. **Internal Client Assets & Academies**: Internal company folders, client proprietary training assets, portfolio PDFs, and specialized RAG agent folders (e.g., `Genesis`, `skills_genesis`) MUST retain their **100% original file names and internal folder structures** to preserve corporate identity and prevent broken internal links.
3. **Shared Files Protection**: Shared files owned by third parties (or with view-only access) must retain their access routes without forcing unauthorized folder moves.

## 4. Human-in-the-Loop (HITL) Documentation Requirement

At the base of every key node branch (`02_CLIENT_SERVICE_DELIVERY`, client roots, engagement roots), a lightweight `README.md` markdown file MUST be created/maintained providing:
- High-level purpose and standards compliance.
- Complete ASCII directory tree structure.
- Description of each subfolder, RBAC access mode, and Gemini RAG indexing flags.

## 5. Regex Validation Pattern

```regex
^([0-9]{8})_([A-Z0-9]+)_([A-Z0-9\-]+)_([A-Z0-9\-]+)_([A-Z0-9\-]+)_(V[0-9]+-[0-9]+)(\.[a-zA-Z0-9]+)?$
```
