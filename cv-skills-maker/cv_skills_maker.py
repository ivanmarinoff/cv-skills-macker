"""
cv-skills-maker base module.

This is the principal module of the cv-skills-maker project.
here you put your main classes and objects.
"""

NAME = "cv-skills-maker"

import random

hiring_criteria = ["experience", "skills", "education", "certifications", "awards"]


def generate_portfolio_text(hiring_criteria):
    portfolio_text = " As a {0} professional with a passion for {1}, I possess strong {2} and {3}.\n My {4} and {5} " \
                     "have " \
                     "allowed me to develop a {6} approach to problem-solving, and I am able to {7} with " \
                     "cross-functional teams to {8}.\n In my previous roles, I have {9} and {10}, and I am excited to " \
                     "bring my skills and expertise to new challenges."
    experience = random.choice(["seasoned", "experienced", "skilled"])
    passion = random.choice(["innovation", "disruptive technologies", "sustainability"])
    skills = random.choice(["strategic planning", "people management", "conflict resolution"])
    analytical_skills = random.choice(["data analysis", "financial modeling", "market research"])
    education = random.choice(["Bachelor's degree", "Master's degree", "PhD"])
    certifications = random.choice(["PMP", "Six Sigma", "CFA"])
    approach = random.choice(["holistic", "data-driven", "customer-centric"])
    collaborate = random.choice(["lead", "partner", "facilitate"])
    teamwork = random.choice(
        ["drive results", "deliver projects on time and under budget", "implement process improvements"])
    achievements = random.choice(
        ["exceeded targets", "delivered projects on time and under budget", "implemented process improvements"])
    accomplishments = random.choice(
        ["exceeded targets", "received accolades from customers", "mentored junior team members"])

    return portfolio_text.format(experience, passion, skills, analytical_skills, education, certifications, approach,
                                 collaborate, teamwork, achievements, accomplishments)


# Sample text for CV
def generate_cv_text(hiring_criteria):
    cv_text = " I am a {0} professional with {1} years of experience in {2}.\n My {3} and {4} have enabled me to " \
              "develop a deep understanding of {5} and the ability to {6}.\n Throughout my career, I have {7} and {8}, " \
              "and have been recognized with {9} for my contributions to the {10} team."
    experience = random.choice(["seasoned", "experienced", "skilled"])
    years_of_experience = random.randint(5, 15)
    skills = random.choice(["strategic planning", "people management", "conflict resolution"])
    analytical_skills = random.choice(["data analysis", "financial modeling", "market research"])
    education = random.choice(["Bachelor's degree", "Master's degree", "PhD"])
    certifications = random.choice(["PMP", "Six Sigma", "CFA"])
    understanding = random.choice(["best practices", "industry trends", "customer needs"])
    ability = random.choice(
        ["develop and execute strategies", "collaborate with cross-functional teams", "deliver high-quality results"])
    accomplishments = random.choice(
        ["exceeded targets", "received accolades from customers", "mentored junior team members"])
    recognition = random.choice(["Employee of the Year", "Outstanding Achievement", "Team Player of the Quarter"])
    team = random.choice(["sales", "product development", "finance"])

    return cv_text.format(experience, years_of_experience, skills, education, certifications, understanding,
                          ability, accomplishments, analytical_skills, recognition, team)


# Test the functions
print(generate_portfolio_text(hiring_criteria))
print(generate_cv_text(hiring_criteria))


def main():
    if __name__ == "__main__":
        main()
