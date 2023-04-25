"""
cv-skills-maker base module.

This is the principal module of the remuneration project.
here you put your main classes and objects.
"""

NAME = "cv-skills-maker"

import random

hiring_criteria = ["experience", "skills", "education", "certifications", "awards"]


# Sample text for personal portfolio
def generate_portfolio_text(hiring_criteria):
    portfolio_text = "As a {0} professional with extensive experience in {1}, " \
                     "I have developed a broad skillset that includes {2}. My {3} and {4} have equipped me with the " \
                     "knowledge and expertise necessary to {5}. In my previous roles, I have consistently {6} and {" \
                     "7}, and I am confident that I can make a valuable contribution to any team."
    experience = random.choice(["seasoned", "experienced", "skilled"])
    skills = random.choice(["project management", "team leadership", "communication", "problem-solving"])
    education = random.choice(["Bachelor's degree", "Master's degree", "PhD"])
    certifications = random.choice(["PMP", "CISSP", "CCNA"])
    awards = random.choice(["Employee of the Year", "Best Team Player", "Outstanding Achievement"])
    actions = random.choice(["drive results", "develop strategies", "lead teams"])
    achievements = random.choice(
        ["exceeded targets", "delivered projects on time and under budget", "implemented process improvements"])

    return portfolio_text.format(experience, hiring_criteria, skills, education, certifications, actions, awards,
                                 achievements)


# Sample text for CV
def generate_cv_text(hiring_criteria):
    cv_text = "I am a {0} professional with {1} years of experience in {2}. My {3} and {4} have equipped me with a " \
              "deep understanding of {5} and the ability to {6}. Throughout my career, I have {7} and {8}, " \
              "and have been recognized with {9}."
    experience = random.choice(["seasoned", "experienced", "skilled"])
    years_of_experience = random.randint(1, 10)
    skills = random.choice(["project management", "team leadership", "communication", "problem-solving"])
    education = random.choice(["Bachelor's degree", "Master's degree", "PhD"])
    certifications = random.choice(["PMP", "CISSP", "CCNA"])
    understanding = random.choice(["best practices", "industry trends", "customer needs"])
    ability = random.choice(
        ["develop and execute strategies", "collaborate with cross-functional teams", "deliver high-quality results"])
    accomplishments = random.choice(
        ["exceeded targets", "delivered projects on time and under budget", "implemented process improvements"])
    recognition = random.choice(["Employee of the Year", "Best Team Player", "Outstanding Achievement"])

    return cv_text.format(experience, years_of_experience, hiring_criteria, education, certifications, understanding,
                          ability, skills, accomplishments, recognition)


# Test the functions
print(generate_portfolio_text("hiring criteria"))
print(generate_cv_text("hiring criteria"))




