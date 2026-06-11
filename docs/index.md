# OctoAcme Project Management Docs

This repository contains OctoAcme project management guidance and a Copilot Spaces exercise focused on scaling organizational knowledge.

## What is included

- `docs/`: Project management process documentation for OctoAcme
- `.github/steps/`: Guided step content for the Copilot Spaces exercise
- `.github/workflows/`: Automation that powers the step-by-step exercise experience
- `.github/ISSUE_TEMPLATE/`: Issue template for adding or updating process documentation
- `.devcontainer/`: VS Code container settings for working in this repo

## Docs navigation

- [`octoacme-project-management-overview.md`](octoacme-project-management-overview.md): High-level project management framework, roles, and artifacts
- [`octoacme-project-initiation.md`](octoacme-project-initiation.md): How to start projects, define scope, and align stakeholders
- [`octoacme-project-planning.md`](octoacme-project-planning.md): Planning activities, backlog management, and release alignment
- [`octoacme-execution-and-tracking.md`](octoacme-execution-and-tracking.md): Execution practices, progress tracking, and iteration management
- [`octoacme-risks-and-communication.md`](octoacme-risks-and-communication.md): Risk identification, escalation, and communication cadence
- [`octoacme-release-and-deployment.md`](octoacme-release-and-deployment.md): Release planning, deployment readiness, and validation
- [`octoacme-retrospective-and-continuous-improvement.md`](octoacme-retrospective-and-continuous-improvement.md): Retrospectives, learnings, and improvement actions
- [`octoacme-roles-and-personas.md`](octoacme-roles-and-personas.md): Role summaries and responsibilities for project teams

## How to use these docs

1. Start with `octoacme-project-management-overview.md` to understand the overall process and key artifacts.
2. Read the initiation, planning, execution, risk, release, and retrospective docs in the order of a project lifecycle.
3. Refer to `octoacme-roles-and-personas.md` when you need role-oriented guidance or want to tailor process content for different stakeholders.
4. Use the `.github/ISSUE_TEMPLATE/add-update-content-to-process-docs.yml` template to request changes, additions, or clarifications in the docs.

## Copilot Spaces guidance

When you add this repository to a Copilot Space, include the following source paths:

- `docs/`
- `.github/ISSUE_TEMPLATE/`

Doing this makes Copilot aware of the process documentation and issue templates, so it can answer questions and generate improvement suggestions from the right context.

## Additional Repository Assets

### Issue Templates
- Located in `.github/ISSUE_TEMPLATE/`
- Used for proposing improvements to process documents
- Helps standardize feedback and documentation updates
- Direct link: [.github/ISSUE_TEMPLATE/add-update-content-to-process-docs.yml](.github/ISSUE_TEMPLATE/add-update-content-to-process-docs.yml)

### GitHub Workflows
- Located in `.github/workflows/`
- Automate exercise steps and guide users through the learning flow
- Useful for understanding how the exercise is structured internally

### Guided Exercise Steps
- Located in `.github/steps/`
- Contains the step content that the exercise workflows post to repository issues

### Copilot Chat placeholder folders
- `.github/prompts/`, `.github/instructions/`, and `.github/chatmodes/` are included as placeholders to satisfy the devcontainer configuration. Add real Copilot prompt/instruction/mode files here when you have them to enable richer local Copilot Chat behavior.

## Repository structure (quick reference)

- `docs/` — process documentation files and `index.md` navigation
- `.github/steps/` — guided exercise step content shown to learners
- `.github/workflows/` — automation powering the step flow
- `.github/ISSUE_TEMPLATE/` — issue templates for proposing doc changes
- `.devcontainer/` — VS Code devcontainer configuration for contributors
