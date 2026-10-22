# Assignment 2 formative feedback

This feedback is organised by the relevant computing bootcamp criteria. Use it to decide what is already working, what you need to investigate, and what to revise before the cumulative submission.

The full criteria are in the [Computing Bootcamp assessment rubric](https://github.com/MulQuaBio/MQB/blob/main/content/rubrics/Computing_Bootcamp_Rubric.md).

## 1. Repository organisation and workflow discipline

- Your root README, `.gitignore`, cleaning script, test script and supplied data files are in the expected locations. The supplied CSV and metadata are unchanged, giving you a reproducible starting point.

## 2. Code completeness and functional correctness

- Your cleaner and tests run, but checks found differences in all three output tables: the clean table has one extra row, the issues table has one fewer row, and the oak summary has one extra species. Trace the first borderline row through validation and the accepted/rejected branch, then trace accepted oak rows into the summary. Re-run the workflow after each focused fix.

## 3. Code quality and style

- Your `main()` function gives the program a clear overall structure by connecting loading, processing, summarising and writing. Keep these stages distinct as you revise; use descriptive names and add short comments where the reason for a validation check or data-cleaning step is not obvious.

## 4. Documentation

- Your root README is in place. Make it useful to someone opening the repository for the first time: explain what the cleaner does, how to run the script and tests from the repository root, and which three files it creates. Test the instructions in a newly cloned copy of your repository (a separate folder created with `git clone`): enter that folder and run each README command exactly as written. If something fails, correct the command or add the missing step.

## 5. Version-control practice

- Since the previous formative feedback was added, the saved history contains 15 non-merge commits. Messages such as `Complete process_record() function`, `Add test script to repo`, and `Fix errors detected by test script` show a useful implementation–test–revision sequence.
- Keep this pattern for the final revisions. Before each commit, use `git diff --staged` to check that it contains one coherent, working change, then write a concise message that names that change and, where it is not obvious, why it was needed.

## 8. Basic error handling and input validation

- Your cleaning script ran and produced all three output files. Your separate test file also completed successfully; your test file includes assertion-style checks covering record validation, accepted/rejected partitioning and the oak summary. These are useful foundations, although successful execution does not show that every important case and result is correct.
- **Turn the diagnosis into a regression test.** Your existing tests cover relevant stages, but they did not expose the output differences. Add a focused assertion for the record or boundary rule you identify, checking both its validation result and its destination. If the summary has a separate issue, add a small summary case with a manually justified result. Run the separate test file and the full workflow again.
- Keep the raw input unchanged while revising the code. Check that every loaded record reaches the appropriate accepted or rejected collection, then inspect how accepted oak records contribute to the written summary.

## 9. Problem-solving approach and method implementation

- Your supplied raw CSV and metadata are unchanged. Your code shows a clear connected workflow: `main()` loads the rows, passes them through `process_records()` and `validate_record()`, receives `(clean_records, issues)`, summarises the cleaned records with `summarise_oaks()`, and writes the three outputs. This makes the main steps easy to locate.
- **Trace the path from validation to the outputs.** The output comparisons found differences in all three tables: the cleaned table has an extra row, the issues table has fewer rows than required, and the oak summary has an extra species row. These may share a cause, but the checks do not yet show one. Trace a borderline input record through `validate_record()` and the accepted/rejected branch, checking its treatment against the supplied metadata. Then trace accepted oak records into `summarise_oaks()`. This will help distinguish a validation problem from a separate summarisation problem.
- After correcting the logic, keep the smallest example that exposed each problem as an assertion-based regression test in `code/test_silwood_trees.py`. Check the relevant function return value and the affected output table, then briefly explain the corrected data flow in your root README.
