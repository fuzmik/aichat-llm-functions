#!/usr/bin/env python3

# <!--
# @describe Generates a user story based on a feature description.
# @option <feature_description> A natural language description of the feature.
# -->

import sys
import json

def run(feature_description: str) -> str:
    """
    Generates a user story based on a natural language feature description.
    """
    # In a real scenario, this would involve a more sophisticated LLM call
    # to generate a detailed user story. For this tool, we'll provide a structured placeholder.

    title = f"Implement {feature_description.split(' ', 3)[-1].replace('\n', ' ')}"
    persona = "user"
    something = f"to {feature_description.lower()}"
    purpose = "to achieve a specific outcome."
    acceptance_criteria = [
        "The feature works as described.",
        "It is integrated seamlessly with existing functionality.",
        "Relevant documentation is updated."
    ]

    story = f"""
## User Story <number>: {title}

**As a** {persona},
**I want** {something}
**So that** {purpose}

**Acceptance Criteria:**

"""
    for i, criteria in enumerate(acceptance_criteria):
        story += f"{i + 1}. {criteria}\n"

    return story

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: write_user_story.py <feature_description>")
        sys.exit(1)

    feature_description = sys.argv[1]
    user_story = run(feature_description)
    print(user_story)
