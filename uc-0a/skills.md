# skills.md
# INSTRUCTIONS: Generate a draft by prompting AI, then manually refine this file.
# Delete these comments before committing.

skills:
  - name: classify_complaint
    description: Analyzes a single complaint description to determine its category, priority, and justification reason.
    input: row (dictionary containing complaint description)
    output: A dictionary with category, priority, reason, and an ambiguity flag.
    error_handling: If the description is empty or missing, return category 'Other' and flag 'NEEDS_REVIEW'.

  - name: batch_classify
    description: Processes an entire CSV file of complaints and writes the results to an output CSV.
    input: input_file (string), output_file (string)
    output: None (writes to file).
    error_handling: Fail if the input file is not found or if the output path is unwritable.


