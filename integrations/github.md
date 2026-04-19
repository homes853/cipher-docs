# GitHub Integration

Cipher integrates with GitHub as a GitHub App, giving it access to your repositories and pull requests without requiring a personal access token.

## Installation

1. Go to **Integrations** in the Cipher sidebar
2. Click **Install GitHub App →**
3. Choose your GitHub account or organization
4. Select which repositories Cipher can access (specific repos or all)
5. Authorize the OAuth request on the next screen
6. You'll be redirected back to `cipher-ai.app/integrations` automatically

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
