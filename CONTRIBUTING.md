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

## Repository structure

- `README.md`: Practical guide to what is included in this repository.
- `docs/index.md`: Navigation for the process docs.
- `docs/*.md`: Process documents for OctoAcme.
- `.github/steps/`: Guided exercise content for Copilot Spaces.
- `.github/workflows/`: Workflows that power the step exercise.
- `.github/ISSUE_TEMPLATE/`: Issue template for process-doc improvements.
- `.devcontainer/`: VS Code dev container settings.
