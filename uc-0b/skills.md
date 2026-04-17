# skills.md

skills:
  - name: retrieve_policy
    description: Loads a policy text file and parses it into a structured list of numbered sections.
    input: File path to a .txt policy document (e.g., policy_hr_leave.txt).
    output: A list of structured objects, each containing a clause number and its verbatim text content.
    error_handling: Returns a "File Not Found" error if the path is invalid or a "Parse Error" if the document format lacks clear numbering.

  - name: summarize_policy
    description: Generates a concise summary of the policy that preserves all specific conditions and core obligations.
    input: A list of structured policy sections.
    output: A summary document where every numbered clause is present and all multi-condition approvals are preserved exactly.
    error_handling: Quotes clauses verbatim and flags them for manual review if they are too complex to summarize without risk of meaning loss.
