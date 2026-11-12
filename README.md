# Job Market Analysis (Riya)
A project exploring job market trends.

## Project Structure
A common way to do any project is to first get input the processing followed by output .

input - web scraping using APIs.(An API (Application Programming Interface) is a way for one program to ask another
program for information. Another program here stands for webstites that collect data. you can ask for what u need and 
they will provide it.  )
    

## Goals
Make a website where people can look up a job and see the common jobs available currently and see the job market 
expectations and predictions for the future.

## Tech Stack
- **Python 3.10+**
- **pandas** — data manipulation



## Steps

1. Made a Git repository and cloned it.

2. Learned about the common structure used for software projects.

    - input -> processing -> output

3. Decided to use an API as the input source.

4. Chose Adzuna as the API source.(Mostly provides career information,jobs etc)
   - Created an account.
   - Received an API ID and API key.

5. Created an `.env` file to store the API ID and API key.

6. Created a `.gitignore` file and added `.env` so the credentials will not be shared when committed to Git.

7. Made file `adzuna_tesring.py` to test getting active listing from Adzuna

8. Made `api.py` to use the api for the project