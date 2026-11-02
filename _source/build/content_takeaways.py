# -*- coding: utf-8 -*-
"""Take-aways for participants: cheat sheet, safe-use card, take-home guide. Hints and habits, never answers."""

CHEAT = [
    {"ph": "Part 1", "pt": "The framework", "sub": "Every agent has three parts. Get these right and the tool matters much less.",
     "items": [("Input", "What it reads each time", "Name the file, the fields and the format.", "The KYC pack as one PDF."),
               ("Instruction", "How it does the job", "Role, steps, rules, what to do when unsure, output.", "Check Section 2 of the policy. Flag expiry within 60 days."),
               ("Output", "What a reviewer gets", "A fixed format a person can check in two minutes.", "Required document | Status | Evidence | Note")],
     "sum": "The agent does the first pass. You sign the file."},
    {"ph": "Part 2", "pt": "Five parts of a strong instruction", "sub": "Each part removes one way the agent can guess.",
     "items": [("Role", "Who it is", "Name the job and who it serves.", "You are a client onboarding assistant at the firm."),
               ("Steps", "In order", "Number them. One action per step.", "1. List every document. 2. Compare with Section 2."),
               ("Rules", "The limits", "Sources it may use, thresholds, what it must never do.", "Use only this pack and the policy."),
               ("If unsure", "No guessing", "Tell it what to write when the answer is not there.", "Write Not found. Never guess a date."),
               ("Output", "The format", "Columns or sections, in order, and a last line.", "A table, then one decision line.")]},
    {"ph": "Part 3", "pt": "Test before you trust", "sub": "Write the expected answer before you run each test.",
     "items": [("Normal", "Everything is there", "Does it say so, without inventing problems?", ""),
               ("Missing data", "One item is not there", "Does it write Not found, or does it fill the gap?", ""),
               ("Trap", "Looks fine, breaks a rule", "Does it catch the near miss?", "")],
     "sum": "When the answer is wrong, fix the instruction, not the answer. Then run all three tests again."},
    {"ph": "Part 4", "pt": "Find the task", "sub": "Four questions. Four yes answers: automate. Two or three: assist. One or none: keep it human.",
     "items": [("1", "Does it repeat?", "Weekly or more.", ""), ("2", "Are the rules written down?", "A policy, a memo, a checklist.", ""),
               ("3", "Is the input digital?", "A file, a table, an email.", ""), ("4", "Can a reviewer check it in 2 minutes?", "A table, not an essay.", "")]},
    {"ph": "Part 5", "pt": "The workflow skeleton", "sub": "Trigger → Read → AI → Decide → Output. The human check sits after Decide.",
     "items": [("Trigger", "On form submission", "Also: email, a new file in a folder, a schedule.", ""),
               ("Read", "Extract from File", "Extract From PDF or From XLSX. Add Aggregate for many rows.", ""),
               ("AI", "Basic LLM Chain", "With the Anthropic Chat Model and a Structured Output Parser.", ""),
               ("Decide", "IF", "Reads one field, for example status.", ""),
               ("Output", "Data table, Form Ending", "A row for the reviewer, a line back to the sender.", "")]},
]

EXPRESSIONS = [
    ("{{ $json.text }}", "A field from the step just before."),
    ("{{ $json['Client name'] }}", "A field whose name has a space."),
    ("{{ $('On form submission').item.json['Client name'] }}", "A field from a named step further back."),
    ("{{ $json.output.status }}", "A named field from the Structured Output Parser."),
    ("{{ $now.toFormat('dd LLL yyyy') }}", "Today's date, for example 15 Nov 2026."),
]

SAFE = {
    "intro": "Sort the data before you paste it. The firm's IT and risk policy decides what is allowed. This card is a starting point, not the policy.",
    "cards": [
        ("g", "Green: fine with an approved tool", "No client or personal data.",
         ["The fictional practice files from this workshop", "Public information, for example a published annual report",
          "The firm's blank templates and checklists", "Your own notes with no client names"]),
        ("a", "Amber: only with care", "Only in the firm-approved account, with the minimum data, and a person checks the output.",
         ["A client's trial balance or ledger extract", "Draft management letter wording, with no names",
          "Client documents the firm's policy allows in that tool"]),
        ("r", "Red: never", "Do not paste, upload or connect.",
         ["ID copies, passport scans and personal ID numbers", "Bank account numbers, card numbers and passwords",
          "Any client file in a personal AI account", "Anything the client or the policy marks confidential and not allowed"]),
    ],
    "before": ["Is this tool approved by the firm for this data?", "Do I need all of this data, or only part of it?",
               "Who checks the output before anyone uses it?"],
    "rules": ["AI output is a first pass, not audit evidence. Trace three values to the source.",
              "Keep the instruction version and the test log.",
              "A person makes every acceptance decision and every audit judgment."],
}

GUIDE = [
    ("Week 1 · Day 1", "Pick one task", ["Use the four questions on your own task list.", "Choose a task with written rules and a digital input.",
                                         "Ask your manager: which tool and which data are approved for it?"]),
    ("Week 1 · Day 2", "Write the Agent Card", ["Fill every line: input, instruction, output, three tests.",
                                                "Ask a colleague: could a new joiner run this card?"]),
    ("Week 1 · Day 3", "Build version 1", ["Build it in the firm-approved Claude account.",
                                           "Start with practice or public data. Use real files only if the policy allows it."]),
    ("Week 1 · Days 4 and 5", "Test and fix", ["Run the three tests. Write the expected answer first.",
                                               "Fix the instruction, not the answer. Keep a test log."]),
    ("Week 2", "Pilot with a reviewer", ["Run it on real cases next to the normal process.",
                                         "A reviewer checks every output. Note the minutes before and after.",
                                         "At the end of the week, decide: keep, change or stop."]),
    ("After the pilot", "Make it a workflow", ["Ask IT to connect the trigger and the output to the firm's systems.",
                                               "Agree five things first: owner, test set, review rule, data rule and log."]),
]
STOP = ["The agent guesses even after you fix the instruction.", "Reviewers need more time to check it than to do the task.",
        "The task needs data the policy does not allow in the tool."]
