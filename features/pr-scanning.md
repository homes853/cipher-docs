# PR Scanning

Cipher automatically scans every pull request for security vulnerabilities and posts findings directly on the PR as a comment.

## How It Works

When a pull request is opened, updated, or reopened, Cipher:

1. Receives a webhook event from GitHub
2. Fetches the list of changed files
3. Scans each scannable file through the SAST pipeline (Claude AI + Semgrep)
4. Posts a findings comment on the PR
5. Sets a commit status (pass/fail) visible on the PR checks bar

## Requirements

- GitHub App installed with the repo enabled for scanning in **Integrations**
- Repo toggled **ON** (SCANNING) — repos set to EXCLUDED are skipped entirely

## Commit Status

| Status | Meaning |
|--------|---------|
| ⏳ Pending | Scan is in progress |
| ✅ Success | No critical or high findings |
| ❌ Failure | One or more critical or high findings detected |
| ⚠️ Error | Scan encountered an internal error |

## PR Comment Format

Each scan posts a summary table followed by individual findings:

```
🛡️ Cipher Security Scan
Found N issue(s) across the changed files.

Severity     Count
🔴 Critical   N
🟠 High       N
🟡 Medium     N
🟢 Low/Info   N
```

Each finding includes:
- **Severity** and vulnerability type
- **File path and line number**
- **Description** — what it is, how an attacker exploits it, blast radius
- **Fix** — copy-paste ready code change using actual variable names from your code

## Supported File Types

Cipher scans the following file types on PRs:

`.py` `.js` `.ts` `.jsx` `.tsx` `.go` `.java` `.rb` `.php` `.cs` `.cpp` `.c` `.rs` `.swift` `.kt` `.tf` `.yaml` `.yml` `.json` `.env` `.sh` `.bash`

Markdown, images, and other non-code files are skipped automatically.

## Vulnerability Categories

- SQL / NoSQL / command injection
- Authentication bypasses and broken session management
- Path traversal and arbitrary file read
- XSS (reflected, stored, DOM-based)
- SSRF and open redirects
- Insecure deserialization
- Hardcoded secrets and credentials
- Weak cryptography
- Infrastructure misconfigurations (Terraform, Kubernetes, YAML)

## Excluding a Repo

To stop Cipher from scanning PRs on a specific repo, go to **Integrations**, find the repo, and toggle it **OFF**. The repo will show as `EXCLUDED` and all webhook events from it will be ignored.
