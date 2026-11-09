# California Life Insurance — Study Exam Lab

A complete **offline** local web app: **10 exams × 75 questions = 750 practice-question appearances**, each with multiple-choice answers and immediate explanatory feedback.

## Run on your laptop (Mac / Windows / Linux)

1. Unzip the download.
2. Open `california-life-exam-app/index.html` in Chrome, Edge, Safari, or Firefox by double-clicking it.
3. Pick Exam 1 and select an answer. The correct answer and explanation appear immediately. Click **Next question** to proceed.
4. Your answers are automatically stored in this browser's `localStorage`, so you can close the tab and resume later from the same browser and local file location.

No installation, Python, server, login, internet connection or API key is required. The two runtime files are `index.html` and `questions.js`.

Optional local server: open a terminal in the unzipped folder and run `python3 -m http.server 8000`, then visit `http://localhost:8000`.

## Features

- 10 complete exams, 75 questions each
- Study mode: **correct answer and explanation revealed as soon as you answer**
- Scores, topical performance, missed-answer review, all-answer review
- Question navigator and keyboard shortcuts (**1–4** to answer; arrow keys to move)
- Saved progress (local browser), resume, retake, JSON export
- Mobile-friendly responsive layout

## Important scope disclosure

This package contains **185 individually authored core questions**. To provide 10 full 75-question practice tests, topics are intentionally revisited with varied contextual lead-ins, shuffled options and different exam ordering. There are **750 separate question slots**, **not 750 independent underlying concepts**. This is helpful for spaced repetition but should not be confused with 750 substantively different questions. The questions are original study material, *not* actual or previously used PSI questions.

Most questions teach stable general principles. California-specific legal rules can change and some provisions depend on contract wording. For the current regulatory requirements, use the official CDI resources below. This app does not replace an approved prelicensing ethics course.

## Official references

- [California Department of Insurance — licensing examination objectives](https://www.insurance.ca.gov/0200-industry/0030-seek-pre-lic/psi-prelic-ed-obj.cfm)
- [October 28, 2026 PSI candidate information bulletin](https://www.insurance.ca.gov/0200-industry/0020-apply-license/0100-indiv-resident/upload/PSI-Candidate-Information-Bulletin-English-10-28-2026.pdf): Life = **75 questions, 105 minutes, 60% passing score**.
- [CDI Life license applicant procedures](https://www.insurance.ca.gov/0200-industry/0050-renew-license/0200-requirements/Life/app-proc-ind-res.cfm): review required 12 hours on ethics and California Insurance Code.

## Modify questions

- Edit the `DATA` rows in `build.py` (format `category|question|correct|wrong|wrong|wrong|explanation`).
- Run `python3 build.py` to regenerate `questions.js` and `questions.json`.
- The app itself reads `questions.js`; `questions.json` is provided for inspection and reuse.
