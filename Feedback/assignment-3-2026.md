# Assignment 3 formative feedback

This feedback is organised using the [Computing Bootcamp rubric](https://mulquabio.github.io/MQB/rubrics/Computing_Bootcamp_Rubric.html). It does not award a mark; use it to decide what to revise and check before final submission.

## Criterion 1: Repository organisation & workflow discipline

- The required scripts, supplied data and root README are present, and the supplied inputs are unchanged. No generated results are tracked in your latest commit.
- Before final submission, **Make each route work without pre-existing output folders.** The fixed and generalised tree-height runs halted when writing into a missing `results/` directory. The generalised wrapper also tried to write into a missing `sandbox/` directory, then continued with checks on files that had not been created. This prevents the route from measurements to checked outputs from completing. Make the scripts create the directories they need before writing, and make the wrapper stop or clearly report an unsuccessful prerequisite. Test the fixed and generalised programs separately: test both routes separately. Add `results/` to `.gitignore`; its absence from Git is not itself a problem.

## Criterion 2: Code completeness & functional correctness

Before final submission, run the fixed tree-height route, the generalised route and the Pound Hill analysis separately; check the exact files each one creates.

## Criterion 3: Code quality & style

As you revise, keep names descriptive, use comments to explain decisions rather than restating code, and avoid repeating the same calculation in several places.

## Criterion 4: Documentation

- Your README explains the fixed tree-height and Pound Hill routes and records independent height checks. These are useful student-reported checks, although the normal runs did not reproduce the outputs.

## Criterion 5: Version-control practice

Commit each functional revision with a short message that says what changed; this makes your development easier to follow than one large final commit.

## Criterion 8: Basic error-handling & input validation

- Your tree-height source uses degrees-to-radians conversion and passes angle before distance. Both invalid-input runs stopped with useful distance-related errors and the expected no-output behaviour; this supports those particular cases, not validation generally.
- Before final submission, **Check the tree interface and boundary rules after repairing execution.** The function-interface test halted while sourcing the script because of the output-directory error; it did not establish a numerical interface defect. The required first input is angle in degrees and the second is horizontal distance, which your code already follows. Try the taught example call and compare it with a direct calculation. Also reconcile the distance condition with its error message: the condition rejects zero and permits 100, while the message describes the opposite endpoints. Compare both with the released requirements, then test the relevant boundaries.

## Criterion 9: Problem-solving approach & method implementation

- The Pound Hill source distinguishes species richness from abundance, calculates quadrat richness before plot means, and includes a cautious interpretation that avoids claiming causation. The generated values and figures still need checking.
- Before final submission, **Resolve the Pound Hill output paths.** The collected runs produced neither `results/pound_hill_plot_richness.csv` nor `results/pound_hill_plot_richness.pdf`. The code attempts the table write before plotting, but names the richness PDF `results/observations_by_site.pdf`. Compare the required paths with the filenames your script actually creates: a naming difference alone makes a required output appear missing. Once both files are generated, inspect the PDF's labels and values and check that your biological interpretation agrees with it. No newly generated PDF was available for visual review here.

## Criterion 10: Learning progression demonstration

Use this feedback as a revision checklist. Make the changes in small, descriptive commits, then add a short README note explaining what you changed and how you checked it. This will make your development from this formative checkpoint visible in the final portfolio.

## Priorities before final submission

- Run from the directory containing `code/`, `data/` and the root `README.md`, with generated folders initially absent. Rerun one ordinary and one invalid case for each tree-height route. Confirm that ordinary cases create the intended files and invalid cases report the intended problem without writing a result.
- Recheck one height independently, inspect output headers and row counts, and rerun to check replacement rather than duplication. Record what you actually observe.
- Extend the README with commands for the generalised script and wrapper, and align all output names and run instructions with the repaired code, including the Pound Hill source-header typo.
