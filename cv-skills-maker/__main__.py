"""Entry point for cv_skill_maker."""

"""
cv-skills-maker base module.

This is the principal module of the cv-skills-maker project.
here you print final result.
"""

NAME = "cv-skills-maker"

from generate_cv_text import generate_cv_text
from generate_portfolio_text import generate_portfolio_text


def main():
    return None


# Print the functions
print(generate_portfolio_text())
print(generate_cv_text())

if __name__ == "__main__":
    main()
