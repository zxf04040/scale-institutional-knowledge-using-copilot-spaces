# Scale institutional knowledge using Copilot Spaces

[![Exercise workflow status](https://github.com/zxf04040/scale-institutional-knowledge-using-copilot-spaces/actions/workflows/0-start-exercise.yml/badge.svg)](https://github.com/zxf04040/scale-institutional-knowledge-using-copilot-spaces/actions/workflows/0-start-exercise.yml) [![Issue template sync workflow status](https://github.com/zxf04040/scale-institutional-knowledge-using-copilot-spaces/actions/workflows/update-issue-template.yml/badge.svg)](https://github.com/zxf04040/scale-institutional-knowledge-using-copilot-spaces/actions/workflows/update-issue-template.yml)

This repository is a Copilot Spaces exercise and process documentation hub for OctoAcme project management.

## What’s included in this repository

- `docs/`: Project management process documents for OctoAcme
- `docs/index.md`: Navigation guide for the process docs
- `.github/steps/`: Step content for the guided Copilot Spaces exercise
- `.github/workflows/`: GitHub Actions workflows that power the exercise flow
- `.github/ISSUE_TEMPLATE/`: Issue template for updating or adding process docs
- `CODE_OF_CONDUCT.md`: Contributor expectations and community standards
- `SECURITY.md`: Security reporting and responsible disclosure guidance
- `.devcontainer/`: VS Code dev container settings for fast onboarding and Copilot Chat support
- `CONTRIBUTING.md`: Instructions for updating docs and contributing new process content

## Which docs to read first

1. `docs/index.md` — start here for an overview and links to all process documents.
2. `docs/octoacme-project-management-overview.md` — high-level project lifecycle, roles, and artifacts.
3. `docs/octoacme-project-initiation.md` — how to start a project and align stakeholders.
4. `docs/octoacme-project-planning.md` — planning, backlog, estimates, and DoD.
5. `docs/octoacme-execution-and-tracking.md` — execution methods and progress tracking.
6. `docs/octoacme-risks-and-communication.md` — risk management and communication cadence.
7. `docs/octoacme-release-and-deployment.md` — release planning and deployment readiness.
8. `docs/octoacme-retrospective-and-continuous-improvement.md` — lessons learned and continuous improvement.
9. `docs/octoacme-roles-and-personas.md` — role definitions and responsibilities.

## Overview of exercise steps

The exercise is organized into a step-by-step experience using GitHub workflows:

- `.github/steps/1-step.md` — create and prime the Copilot Space
- `.github/steps/2-step.md` — refresh the exercise and continue with content review
- `.github/steps/3-step.md` — finalize the exercise and reflect on improvements
- `.github/steps/x-review.md` — review guidance for the completed exercise

The workflows in `.github/workflows/` support this progression and help the repository behave like an interactive exercise.

## How to use the issue template

Use the template `Add Content to Project Management Process Docs` to request documentation updates:

- Open a new issue in GitHub
- Select the **Add Content to Project Management Process Docs** template
- Choose the relevant doc from the dropdown or select `<new document>` for a new process file
- Describe the update, why it is needed, and optionally paste suggested content
- Use the acceptance criteria checkboxes to confirm alignment and quality

The template file is located at [.github/ISSUE_TEMPLATE/add-update-content-to-process-docs.yml](.github/ISSUE_TEMPLATE/add-update-content-to-process-docs.yml).

## Copilot Spaces context setup

When you add this repository to a Copilot Space, attach the following source folders:

- `docs/`
- `.github/ISSUE_TEMPLATE/`

This ensures Copilot can index the process documentation and issue template content.

## Devcontainer support

This repo includes `.devcontainer/devcontainer.json` for VS Code. It references support folders for Copilot Chat files:

- `.github/prompts/`
- `.github/instructions/`
- `.github/chatmodes/`

Those folders are included so the container configuration remains valid.

---

## License

This repository is licensed under the MIT License.
