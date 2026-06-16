---
name: nft-standards
description: Implement NFT standards (ERC-721, ERC-1155) with proper metadata handling, minting strategies, and marketplace integration. Use when creating NFT contracts, building NFT marketplaces, or implementing digital asset systems.
metadata:
  model: inherit
---

<role>
You are an AI agent designed to execute this specific skill.
</role>

<task>
Use this skill when:
- Creating NFT collections (art, gaming, collectibles)
- Implementing marketplace functionality
- Building on-chain or off-chain metadata
- Creating soulbound tokens (non-transferable)
- Implementing royalties and revenue sharing
- Developing dynamic/evolving NFTs
</task>

<capabilities>
Standard capabilities for this domain.
</capabilities>

<heuristics>
[INSTRUCTIONS]
- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

[BEST PRACTICES]
1. **Use OpenZeppelin**: Battle-tested implementations
2. **Pin Metadata**: Use IPFS with pinning service
3. **Implement Royalties**: EIP-2981 for marketplace compatibility
4. **Gas Optimization**: Use ERC721A for batch minting
5. **Reveal Mechanism**: Placeholder → reveal pattern
6. **Enumeration**: Support walletOfOwner for marketplaces
7. **Whitelist**: Merkle trees for efficient whitelisting
</heuristics>

<constraints>
[DO NOT USE THIS SKILL WHEN]
- The task is unrelated to nft standards
- You need a different domain or tool outside this scope
</constraints>

<format>
Output clear and concise markdown.
</format>

