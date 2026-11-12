import os
import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("API_ID")
APP_KEY = os.getenv("API_KEY")

BASE_URL = "https://api.adzuna.com/v1/api/jobs/us/search/"

def get_jobs(search_term,location,pages = 5):
    all_jobs = []
    for page in range(1,pages+1):
        url = BASE_URL + str(page)

        params = {
            "app_id": APP_ID,
            "app_key": APP_KEY,
            "results_per_page": 50,
            "what": search_term,
            "where": location,
            "content-type": "application/json"
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            print("Error getting jobs")
            print(response.status_code)
            print(response.json())

        data = response.json()
        jobs = data.get("results",[])

        if not jobs:
            break

        all_jobs.extend(jobs)

    return all_jobs


if __name__ == "__main__":
    jobs = get_jobs("software engineer", "Gainesville")

    print("Total jobs retrieved:", len(jobs))
    print("First job title:", jobs[0].get("title") if jobs else "No jobs found")