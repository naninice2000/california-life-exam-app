# California Life Insurance Exam Prep — aligned repository

This preserves the **existing GitHub Pages application structure and level interfaces**, but installs the revised question banks from `california-life-prep-revised-github.zip` in `beginner/`, `intermediate/`, and `advanced/`.

## Deploy

Copy the **contents** of this directory into the root of the existing GitHub repository and push to `main`. GitHub Pages continues to deploy the static files. **No Python invocation or build step is necessary.**

## Contents

- `index.html`: original landing page, unchanged
- `beginner/index.html`, `intermediate/index.html`, `advanced/index.html`: original quiz UI, changed only to use new browser progress storage keys
- Each level's `questions.json`: byte-for-byte identical to the revised question bank
- Each level's `questions.js`: same JSON questions, re-encoded as `window.EXAMS` for compatibility with the existing quiz UI
- Root `questions.json` and `questions.js`: original legacy files, **not used by the landing page** and left untouched
- `build.py`: optional, safe JSON-to-JS conversion utility; does not create questions or change root files

## Progress

Previous attempts remain under their earlier browser localStorage keys. This update uses separate new keys to prevent old answers from attaching to new questions. Browser progress does not sync across devices.

## Limitations

This is **not** a new independently reviewed bank of 2,250 distinct insurance concepts. Some questions reuse skills or scenario patterns. Validation of counts and structure is not equivalent to legal, editorial, or exam-difficulty review. These questions are unofficial practice, not actual PSI questions.
