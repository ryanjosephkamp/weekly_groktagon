# Debugging the Daily Source Collection Workflow

## Manual Dispatch

Use the repository Actions tab to run the daily source collection workflow manually when a test run is needed outside the scheduled time.

## What to Inspect

- Confirm the workflow ran at the intended target week.
- Review the job summary for source count, target week, and artifact name.
- Download and inspect the workflow artifact after the first run before relying on automation for the pilot.
- Confirm no raw output was committed to the repository.

## Common Failure Areas

- Source configuration cannot be parsed.
- A configured URL fails repeatedly.
- Dependency installation fails.
- Artifact upload fails.

## Safety Expectations

The workflow should upload raw collection output as a workflow artifact using the default GitHub artifact retention policy. It should not include a commit step for raw output or generated manifests.

## References

- `planning/PROJECT.md`
- `planning/implementation-plan.md`
- `planning/gpt-5.5-setup-plan.md`
