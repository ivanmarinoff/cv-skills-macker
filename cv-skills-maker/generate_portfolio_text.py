import random
from hiring_criteria import HiringCriteria


# Sample text for Portfolio

def generate_portfolio_text():
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


class PortfolioText(HiringCriteria):
    ...
