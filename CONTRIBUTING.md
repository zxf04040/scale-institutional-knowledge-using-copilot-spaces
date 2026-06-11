# Contributing to OctoAcme Process Documentation

Thank you for helping improve OctoAcme project management guidance. This repository is designed to be a shared source of truth for process docs and Copilot Spaces exercises.

## Which docs to update

- Update files under `docs/` when you want to improve or add project management guidance.
- Use the existing naming convention: `octoacme-<topic>.md`.
- Keep content focused on project management process, roles, or artifacts.

Recommended editing flow:
1. Review `docs/index.md` for navigation and current doc coverage.
2. Open the doc that matches your topic.
3. Add a new section, clarify wording, or improve examples.
4. Submit a pull request with a clear description of the change.

## How to use the issue template

Use the built-in issue template to request updates or add new process content:

1. In GitHub, click **New issue**.
2. Select the issue template: **Add Content to Project Management Process Docs**.
3. Fill in the template fields:
   - **Which process document do you want to update?**: choose the relevant doc, or select `<new document>` if you are proposing a new file.
   - **Summary of New Content**: describe the change or addition.
   - **Why is this update needed?**: explain the gap, feedback, or improvement.
   - **Suggested Content (optional)**: paste proposed text, checklist items, or example language.
   - **Acceptance Criteria**: select the relevant checkboxes.

This template is located at [.github/ISSUE_TEMPLATE/add-update-content-to-process-docs.yml](.github/ISSUE_TEMPLATE/add-update-content-to-process-docs.yml).

### Pull requests

When you open a pull request, use the PR template at `.github/PULL_REQUEST_TEMPLATE.md` and ensure you:

- Link the issue (when relevant).
- Update `docs/index.md` when adding a new `docs/` file.
- Update the issue template dropdown if you want the new doc to be selectable.

Direct links:

- Code of Conduct: [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- Security policy: [SECURITY.md](SECURITY.md)
- PR template: [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md)

## How to add a new process doc

If you want to add a new process document, follow these steps:

1. Create a new Markdown file in `docs/` with a descriptive name, for example `octoacme-change-management.md`.
2. Add a short introduction, scope, and clear sections for the new process.
3. Update `docs/index.md` with a new link and summary for the new document.
4. Optionally update the issue template dropdown if you want the new doc to appear there.
   - Edit `.github/ISSUE_TEMPLATE/add-update-content-to-process-docs.yml` and add the new doc to the `options` list.
5. Open a pull request and describe the reason for the new doc.

## Copilot Spaces context setup

When you add this repository to a Copilot Space, attach these source folders:

- `docs/`
- `.github/ISSUE_TEMPLATE/`

This ensures Copilot can reference the process guidance and issue template content when answering questions or drafting updates.

## Contribution Acceptance Criteria (Microsoft DevOps Level)

All contributions must meet these enterprise-grade standards before acceptance:

### Documentation Quality
- [ ] Content is clear, concise, and free of typos and grammatical errors
- [ ] New docs follow the established template and naming convention (`octoacme-<topic>.md`)
- [ ] All sections have descriptive headers and meaningful examples
- [ ] Cross-references to related docs are included where applicable
- [ ] Markdown formatting is consistent with existing documentation

### Process Alignment
- [ ] Content aligns with OctoAcme project lifecycle (initiation → planning → execution → release → retrospective)
- [ ] Process steps are testable and actionable by team members of all levels
- [ ] Checklists and templates are complete and avoid ambiguity
- [ ] Dependencies and handoff points between roles are clearly documented

### Automation & Integration
- [ ] Issue template is updated if a new process doc is added
- [ ] `docs/index.md` is updated with links and summaries for new content
- [ ] Workflow automation triggers correctly (YAML syntax validated)
- [ ] Scripts (if added) follow Python best practices and include error handling

### Code & Configuration Standards
- [ ] All YAML/JSON files validate against schema and are free of errors
- [ ] Python scripts include docstrings and handle exceptions gracefully
- [ ] Shell scripts use proper quoting and error checking
- [ ] Secrets and sensitive contact info are never hardcoded (use placeholders or environment variables)

### Testing & Validation
- [ ] Content has been tested with Copilot Spaces (if applicable)
- [ ] Links in documentation are verified and functional
- [ ] Examples provided in docs are accurate and reproducible
- [ ] The PR template has been completed with all sections filled

### Security & Compliance
- [ ] No credentials, API keys, or internal URLs are exposed
- [ ] SECURITY.md contact is updated with real information (or placeholder clearly marked)
- [ ] CODE_OF_CONDUCT is referenced and enforced
- [ ] Contributor has signed off on compliance with organizational policies

### Governance & Review
- [ ] PR is linked to a relevant issue (use "Refs #" syntax)
- [ ] Commit messages follow conventional commit style (`chore:`, `feat:`, `fix:`, etc.)
- [ ] PR description explains the *why* behind changes, not just the *what*
- [ ] At least one maintainer review and approval is required before merge
- [ ] CI/CD checks (workflow validation, linting) pass before merge

### Performance & Operations
- [ ] Automation workflows complete in < 2 minutes (no excessive delays)
- [ ] Issue template and process docs scale to support 100+ team members
- [ ] Documentation is indexed and searchable via Copilot Spaces
- [ ] Fallback mechanisms (e.g., branch protection handling) work correctly

## Repository structure

- `README.md`: Practical guide to what is included in this repository.
- `docs/index.md`: Navigation for the process docs.
- `docs/*.md`: Process documents for OctoAcme.
- `.github/steps/`: Guided exercise content for Copilot Spaces.
- `.github/workflows/`: Workflows that power the step exercise.
- `.github/ISSUE_TEMPLATE/`: Issue template for process-doc improvements.
- `.devcontainer/`: VS Code dev container settings.
