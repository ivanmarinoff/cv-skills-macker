import random
from hiring_criteria import HiringCriteria


# Sample text for CV
def generate_cv_text():
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


class CVText(HiringCriteria):
    ...
