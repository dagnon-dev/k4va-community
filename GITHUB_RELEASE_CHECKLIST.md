# GitHub Release Checklist

This document prepares the repository for publication. No remote repository was created, no GitHub authentication was used and nothing was pushed.

## Repository metadata

- Repository name: `k4va-community`
- Description: Open-source API Governance & Production Readiness analyzer for OpenAPI contracts.
- Website: https://www.k4va.com
- Suggested topics: `openapi`, `api-governance`, `api-security`, `api-design`, `devsecops`, `production-readiness`, `rest-api`, `open-source`, `python`
- Default branch: `main`

## Recommended GitHub settings

- Enable Issues.
- Enable Discussions if community discussion is desired.
- Enable Private Vulnerability Reporting when available.
- Enable Dependabot alerts.
- Enable Secret Scanning when available for the repository and plan.
- Add branch protection for `main` after initial publication.

## Before publication

- Confirm the MPL-2.0 decision and preserve the complete `LICENSE` text.
- Review `COMMUNITY_EXTRACTION_PLAN.md` and `OPEN_SOURCE_AUDIT.md`.
- Run the release venv installation and all tests.
- Build and run the Docker image if a Docker daemon is available.
- Review the first release commit manually.

## Publication boundary

This preparation contains no remote URL, GitHub token, release configuration, package publishing configuration or deployment workflow.
