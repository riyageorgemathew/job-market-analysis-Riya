import os
import requests
from dotenv import load_dotenv

load_dotenv()

app_id = os.getenv("API_ID")
app_key = os.getenv("API_KEY")

base_url = "https://api.adzuna.com/v1/api/jobs/us/search/"

#what we r asking from the adzuna
params = {
    "app_id": app_id,
    "app_key": app_key,
    "results_per_page": 50,
    "what": "software engineer",
    "where": "Gainesville",
    "content-type": "application/json"
    # asks info in json format
}

#list to store whats in adzuna
all_jobs = []

for page in range(1, 6):
    url = base_url + str(page) #goes through the page

    response = requests.get(url, params=params) # sends the request

    if response.status_code == 200: # if successful
        data = response.json() # get in json
        jobs = data.get("results", []) # extract listings
        all_jobs.extend(jobs) #adds to main list

        print(f"Page {page}: Retrieved {len(jobs)} jobs")

    else:
        print("Error:", response.status_code)
        print(response.text) #error details
        #break

print(f"\nTotal jobs retrieved: {len(all_jobs)}")

for job in all_jobs:
    print("\nTitle:", job.get("title"))
    print("Company:", job.get("company", {}).get("display_name"))
    print("Location:", job.get("location", {}).get("display_name"))
    print("Date posted:", job.get("created"))
    print("Salary:", job.get("salary_min"), "-", job.get("salary_max"))
    print("Category:", job.get("category", {}).get("label"))
    print("Description:", job.get("description"))
    print("Job URL:", job.get("redirect_url"))
    print("-" * 50)
