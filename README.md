# California Life Insurance Exam Prep — All Levels

A static, offline-capable study site combining the **three previously created versions** of the California Life-only insurance mock exams into a single GitHub repository.

## Overview

| Directory | Difficulty label | Based on | Exams | Questions per exam |
|---|---|---|---:|---:|
| `beginner/` | Beginner | Version 1 | 10 | 75 |
| `intermediate/` | Intermediate | Version 2 | 10 | 75 |
| `advanced/` | Advanced | Version 3 | 10 | 75 |

Total: **30 exam sets / 2,250 question placements**. The original question banks are preserved. The difficulty labels are intended progression, not independently validated PSI exam difficulty ratings. Some concepts and question patterns recur, particularly across versions.

## Run locally

Unzip the repository and double-click the **root** `index.html` to choose a level. No install, web server, package manager, API keys, or network connection is required for the quizzes.

## Publish using GitHub Pages

1. Create a new public GitHub repository, e.g. `california-life-exam-prep`.
2. Upload **all contents of this folder** to the repository root (including `index.html`, `.nojekyll`, and the three level directories), or use Git:

   ```bash
   git init
   git add .
   git commit -m "Add California life exam prep levels"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/california-life-exam-prep.git
   git push -u origin main
   ```

3. In the repository, open **Settings → Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch** and select **main / (root)**. Save.
5. Once deployed, open `https://YOUR_USERNAME.github.io/california-life-exam-prep/`.

Alternatively, you can use GitHub Desktop or the GitHub web uploader rather than terminal commands.

## Save data and switching from an old app

Each level retains its original localStorage key:

- Beginner: `ca-life-study-v1`
- Intermediate: `ca-life-study-v2-unique`
- Advanced: `ca-life-study-v3-scenarios`

These are scoped to the browser **origin**, not your GitHub account. Old progress from a local `file://` URL does **not** automatically transfer to the GitHub Pages website. Each level saves separately under the same GitHub Pages origin, avoiding cross-level answer collisions. Clearing site data or switching browsers may remove progress. The current app does not have built-in cross-device sync.

## Structure

```text
index.html                    # Landing page with difficulty selection
.nojekyll                     # Let GitHub Pages serve static files directly
beginner/index.html
beginner/questions.js
beginner/questions.json
intermediate/index.html
intermediate/questions.js
intermediate/questions.json
advanced/index.html
advanced/questions.js
advanced/questions.json
```

## Important

- All questions are **unofficial practice content**, not PSI's confidential exam questions.
- The 750 questions in a version are not necessarily 750 independent insurance concepts; several are transformed/related questions.
- Verify current exam timing, blueprint, and legal requirements with the [California Department of Insurance](https://www.insurance.ca.gov/) and PSI.
- This is a client-side static app; answers remain on your computer/in your browser unless you explicitly export or share data.
