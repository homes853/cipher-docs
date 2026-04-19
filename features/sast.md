# SAST — Static Application Security Testing

Cipher's SAST engine scans your source code for vulnerabilities, secrets, and dependency issues using a three-layer pipeline.

## How It Works

Every file goes through three scanners in sequence:

1. **Secrets Scanner** — detects hardcoded API keys, tokens, passwords, and credentials using pattern matching
2. **Semgrep** — open-source SAST rules for common vulnerability patterns (SQLi, XSS, insecure configs, etc.)
3. **Claude AI** — deep semantic analysis on files flagged HIGH or CRITICAL by Semgrep, providing context-aware findings and remediation advice

## Scan Triggers

| Trigger | When |
|---------|------|
| `github_pr` | A pull request is opened or updated |
| `scheduled` | Daily or weekly full-repo scan |
| `manual` | "Run Scans Now" button |
| `install` | Initial scan when GitHub App is installed |

## Scan Runs

The **Scan Runs** tab shows all scans with:
- Repo and commit SHA
- Finding counts by severity (Critical / High / Medium / Low)
- Trigger type and date
- Files scanned

## Schedules

Set up recurring scans under the **Schedules** tab:
1. Click **+ Add First Repo**
2. Select a repo and frequency (daily or weekly)
3. Cipher will scan automatically at 02:00 UTC

## Severity Levels

| Level | Meaning |
|-------|---------|
| CRITICAL | Exploitable vulnerability requiring immediate action |
| HIGH | Significant risk, fix before next release |
| MEDIUM | Should be addressed but lower urgency |
| LOW | Best practice violation or informational |

## Pass Rate

The pass rate on the dashboard = percentage of scans with no CRITICAL or HIGH findings.
