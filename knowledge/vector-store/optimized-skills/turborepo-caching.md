---
name: turborepo-caching
description: Configure Turborepo for efficient monorepo builds with local and remote caching. Use when setting up Turborepo, optimizing build pipelines, or implementing distributed caching.
metadata:
  model: inherit
---

<role>
You are an AI agent designed to execute this specific skill.
</role>

<task>
Use this skill when:
- Setting up new Turborepo projects
- Configuring build pipelines
- Implementing remote caching
- Optimizing CI/CD performance
- Migrating from other monorepo tools
- Debugging cache misses
</task>

<capabilities>

</capabilities>

<heuristics>
[INSTRUCTIONS]
- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

[BEST PRACTICES]
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- The task is unrelated to turborepo caching
- You need a different domain or tool outside this scope
</constraints>

<format>
[TEMPLATES]


[TEMPLATE 1: TURBO.JSON CONFIGURATION]
```json
{
  "$schema": "https://turbo.build/schema.json",
  "globalDependencies": [
    ".env",
    ".env.local"
  ],
  "globalEnv": [
    "NODE_ENV",
    "VERCEL_URL"
  ],
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": [
        "dist/**",
        ".next/**",
        "!.next/cache/**"
      ],
      "env": [
        "API_URL",
        "NEXT_PUBLIC_*"
      ]
    },
    "test": {
      "dependsOn": ["build"],
      "outputs": ["coverage/**"],
      "inputs": [
        "src/**/*.tsx",
        "src/**/*.ts",
        "test/**/*.ts"
      ]
    },
    "lint": {
      "outputs": [],
      "cache": true
    },
    "typecheck": {
      "dependsOn": ["^build"],
      "outputs": []
    },
    "dev": {
      "cache": false,
      "persistent": true
    },
    "clean": {
      "cache": false
    }
  }
}
```

[TEMPLATE 2: PACKAGE-SPECIFIC PIPELINE]
```json
// apps/web/turbo.json
{
  "$schema": "https://turbo.build/schema.json",
  "extends": ["//"],
  "pipeline": {
    "build": {
      "outputs": [".next/**", "!.next/cache/**"],
      "env": [
        "NEXT_PUBLIC_API_URL",
        "NEXT_PUBLIC_ANALYTICS_ID"
      ]
    },
    "test": {
      "outputs": ["coverage/**"],
      "inputs": [
        "src/**",
        "tests/**",
        "jest.config.js"
      ]
    }
  }
}
```

[TEMPLATE 3: REMOTE CACHING WITH VERCEL]
```bash

[TEMPLATE 4: SELF-HOSTED REMOTE CACHE]
```typescript
// Custom remote cache server (Express)
import express from 'express';
import { createReadStream, createWriteStream } from 'fs';
import { mkdir } from 'fs/promises';
import { join } from 'path';

const app = express();
const CACHE_DIR = './cache';

// Get artifact
app.get('/v8/artifacts/:hash', async (req, res) => {
  const { hash } = req.params;
  const team = req.query.teamId || 'default';
  const filePath = join(CACHE_DIR, team, hash);

  try {
    const stream = createReadStream(filePath);
    stream.pipe(res);
  } catch {
    res.status(404).send('Not found');
  }
});

// Put artifact
app.put('/v8/artifacts/:hash', async (req, res) => {
  const { hash } = req.params;
  const team = req.query.teamId || 'default';
  const dir = join(CACHE_DIR, team);
  const filePath = join(dir, hash);

  await mkdir(dir, { recursive: true });

  const stream = createWriteStream(filePath);
  req.pipe(stream);

  stream.on('finish', () => {
    res.json({ urls: [`${req.protocol}://${req.get('host')}/v8/artifacts/${hash}`] });
  });
});

// Check artifact exists
app.head('/v8/artifacts/:hash', async (req, res) => {
  const { hash } = req.params;
  const team = req.query.teamId || 'default';
  const filePath = join(CACHE_DIR, team, hash);

  try {
    await fs.access(filePath);
    res.status(200).end();
  } catch {
    res.status(404).end();
  }
});

app.listen(3000);
```

```json
// turbo.json for self-hosted cache
{
  "remoteCache": {
    "signature": false
  }
}
```

```bash

[TEMPLATE 5: FILTERING AND SCOPING]
```bash

[TEMPLATE 6: ADVANCED PIPELINE CONFIGURATION]
```json
{
  "$schema": "https://turbo.build/schema.json",
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**"],
      "inputs": [
        "$TURBO_DEFAULT$",
        "!**/*.md",
        "!**/*.test.*"
      ]
    },
    "test": {
      "dependsOn": ["^build"],
      "outputs": ["coverage/**"],
      "inputs": [
        "src/**",
        "tests/**",
        "*.config.*"
      ],
      "env": ["CI", "NODE_ENV"]
    },
    "test:e2e": {
      "dependsOn": ["build"],
      "outputs": [],
      "cache": false
    },
    "deploy": {
      "dependsOn": ["build", "test", "lint"],
      "outputs": [],
      "cache": false
    },
    "db:generate": {
      "cache": false
    },
    "db:push": {
      "cache": false,
      "dependsOn": ["db:generate"]
    },
    "@myorg/web#build": {
      "dependsOn": ["^build", "@myorg/db#db:generate"],
      "outputs": [".next/**"],
      "env": ["NEXT_PUBLIC_*"]
    }
  }
}
```

[TEMPLATE 7: ROOT PACKAGE.JSON SETUP]
```json
{
  "name": "my-turborepo",
  "private": true,
  "workspaces": [
    "apps/*",
    "packages/*"
  ],
  "scripts": {
    "build": "turbo build",
    "dev": "turbo dev",
    "lint": "turbo lint",
    "test": "turbo test",
    "clean": "turbo clean && rm -rf node_modules",
    "format": "prettier --write \"**/*.{ts,tsx,md}\"",
    "changeset": "changeset",
    "version-packages": "changeset version",
    "release": "turbo build --filter=./packages/* && changeset publish"
  },
  "devDependencies": {
    "turbo": "^1.10.0",
    "prettier": "^3.0.0",
    "@changesets/cli": "^2.26.0"
  },
  "packageManager": "npm@10.0.0"
}
```
</format>

