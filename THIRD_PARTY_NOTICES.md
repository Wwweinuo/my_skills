# Third-Party Notices

This repository combines locally maintained skills with material derived from third-party projects. A license contained inside a skill directory overrides the repository-level `LICENSE` for that directory.

## Anthropic Agent Skills

The following directories were imported from the public [anthropics/skills](https://github.com/anthropics/skills) repository and may have been modified locally:

- `algorithmic-art`
- `brand-guidelines`
- `canvas-design`
- `claude-api`
- `doc-coauthoring`
- `docx`
- `frontend-design`
- `internal-comms`
- `mcp-builder`
- `pdf`
- `pptx`
- `skill-creator`
- `slack-gif-creator`
- `theme-factory`
- `web-artifacts-builder`
- `webapp-testing`
- `xlsx`

Most of these directories include an Apache License 2.0 file. Preserve the copyright and license notices when copying or modifying them. This checkout's `doc-coauthoring` directory does not include a license file, so its redistribution status is treated as unverified. Upstream also publishes a [third-party notices file](https://github.com/anthropics/skills/blob/main/THIRD_PARTY_NOTICES.md) covering dependencies and bundled assets; consult and preserve applicable notices when distributing those components.

### Restricted or unverified skills

The license files in `skills/docx`, `skills/pdf`, `skills/pptx`, and `skills/xlsx` state that these materials are source-available rather than open source and impose restrictions including restrictions on retaining, copying, creating derivative works, and distributing the materials.

Do not publish, fork, mirror, or redistribute those four directories unless you have confirmed that your agreement with Anthropic permits it. Also treat `doc-coauthoring` as non-redistributable until its license is verified. Their presence in a public upstream repository does not replace or relax applicable license terms.

## Locally added skills

Git history shows that these directories were added after the initial Anthropic Skills import:

- `feynman-technique` — covered by the repository-level Apache License 2.0 to the extent the repository owner holds the relevant rights.
- `teach` — covered by the repository-level Apache License 2.0 to the extent the repository owner holds the relevant rights.
- `karpathy-guidelines` — governed by its included `LICENSE.txt`.

This notice is an inventory, not legal advice. Verify the provenance of locally added material before public distribution.

## Humanizer

`skills/humanizer` is derived from [blader/humanizer](https://github.com/blader/humanizer), version 2.11.2 at commit `e2e92e7b4b8229253ed5c8e81dc65463fdeddda5`.

It is distributed under the MIT License. The copyright and permission notice are preserved in `skills/humanizer/LICENSE.txt`.
