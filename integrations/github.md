# GitHub Integration

Cipher integrates with GitHub as a GitHub App with OAuth authorization, giving it access to your repositories and pull requests.

## Installation

1. Go to **Integrations** in the Cipher sidebar
2. Click **Install GitHub App →**
3. Choose your GitHub account or organization
4. Select which repositories Cipher can access (or all repos)
5. Authorize the OAuth request on the next screen
6. You'll be redirected back to `cipher-ai.app/integrations` automatically

## Managing Repositories

The Integrations page shows **all repositories** in your GitHub account, not just ones already added to Cipher.

| Badge | Meaning |
|-------|---------|
| `SCANNING` | Repo is added and has scheduled scans enabled |
| `IDLE` | Repo is accessible to Cipher but scheduled scans are off |
| `NOT ADDED` | Repo is not yet accessible to Cipher |

**Toggling a repo:**
- If the repo shows `NOT ADDED` — toggling it ON grants Cipher access to that repo and enables weekly scheduled scans in one step. No need to visit GitHub settings.
- If the repo shows `IDLE` — toggling it ON enables weekly scheduled scans.
- If the repo shows `SCANNING` — toggling it OFF disables scheduled scans (Cipher retains access).

## What Cipher Gets Access To

- Read access to repository contents (for scanning)
- Read access to pull requests (to comment findings)
- Write access to pull request checks and comments (to post scan results)

## PR Scanning

When a pull request is opened or updated, Cipher:
1. Fetches the diff
2. Scans changed files through the SAST pipeline
3. Posts a comment with findings directly on the PR
4. Sets a commit status (pass/fail) based on severity

## Disconnecting

Click **Disconnect** on the Integrations page to unlink Cipher from your GitHub account. You can also uninstall the app directly from **github.com/settings/installations**.

## Troubleshooting

- **No PR comment posted**: Ensure the repo has scanning enabled in Cipher Integrations.
- **403 on webhook**: Verify the webhook secret matches `GITHUB_WEBHOOK_SECRET` in your backend env.
- **Scan not triggering**: Check that the PR action is `opened`, `synchronize`, or `reopened`.
