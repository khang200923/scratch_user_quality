import json
import os
from dotenv import load_dotenv
import numpy as np
from openai import OpenAI
from pydantic import BaseModel
import requests
from scipy.stats import pareto

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()

project_quality_check = get("project-quality-check.md")

class ScratchProjectQuality(BaseModel):
    process: list[list[str | float]]

def scratch_project_quality(project) -> float:
    """Returns the quality of a Scratch project, in hours."""
    title = project['title']
    description = project['description']
    instructions = project['instructions']
    views = project['stats']['views']
    loves = project['stats']['loves']
    favorites = project['stats']['favorites']
    remixes = project['stats']['remixes']

    response = client.beta.chat.completions.parse(
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {"role": "system", "content": project_quality_check.format(title=title, description=description, instructions=instructions, views=views, loves=loves, favorites=favorites, remixes=remixes)}
        ],
        response_format=ScratchProjectQuality,
        temperature=0
    ).choices[0].message.content
    response = json.loads(response)
    quality = sum(time for _, time in response["process"]) / 60
    print(f"\"{title}\": {quality:.2f} hours")
    return quality

def scratch_user_quality(user: str, accuracy: int = 10) -> float:
    try:
        request = requests.get(f'https://api.scratch.mit.edu/users/{user}/projects', timeout=5)
        request.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching projects for user {user}: {e}")
        return 0.0

    projects = request.json()
    num_projects = len(projects)
    if accuracy > num_projects:
        top_score = sum(scratch_project_quality(project) for project in projects)
        return top_score
    top_projects = sorted(projects, key=lambda p: int(p['stats']['views']), reverse=True)[:accuracy]
    top_score = sum(scratch_project_quality(project) for project in top_projects)
    return top_score / (1 - pareto.cdf(num_projects, 1.16, scale=accuracy))

def main():
    while True:
        user = input(">> ")
        if user.lower() == 'exit':
            break
        quality = scratch_user_quality(user)
        print(f"@{user}: {quality:.2f} hours")

if __name__ == "__main__":
    main()
