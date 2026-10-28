# Project workflow

GitHub repository: https://github.com/robertstephenq/powerball-atlas

The user requested on October 28, 2026 that completed changes made to this project in ChatGPT/Codex also be committed and pushed to this GitHub repository.

- After completing a task that changes project files, run the relevant checks, keep README setup/usage instructions current, commit the intended changes, and push them to this repository. Verify the resulting commit on GitHub and include its link in the final response. Do not make empty commits for read-only tasks.
- Inspect the remote branch and preserve intervening GitHub changes. Use ordinary fast-forward pushes or the connected GitHub tools with an expected branch-head SHA. Never force-push, overwrite unrelated work, or change repository visibility.
- Keep existing hosting/source remotes intact. For a Sites checkout, the Sites source repository and this GitHub repository are separate destinations; keep the project files synchronized without replacing the Sites origin. Follow the existing Sites workflow when publishing website changes.
- Upload source, authored assets, and necessary configuration; exclude credentials, environment secrets, dependency directories, caches, runtime account data, student submissions, automation projects/schedules, the Grading agent, and dashboards. Do not restore grading-service API keys from local coursework copies.
- If authentication, network access, merge conflicts, or required approvals prevent a push, preserve the completed work and report the precise blocker; do not claim synchronization succeeded.
