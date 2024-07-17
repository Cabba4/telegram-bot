import requests
import json
import mysql.connector
from datetime import datetime, timedelta

# Database connection
mydb = mysql.connector.connect(
    host='localhost',
    user='sql',
    password='sqlpass',
    database='user_infodb'
)
mycursor = mydb.cursor()

# Fetching the data from the given API link
url = 'https://apigw.jobteaser.com/jobteaser.job_ad.v2alpha/JobAdService/SearchJobAds'
header = {
    "query": "",
    "page_size": 20,
    "page_token": "0",
    "sponsored_results_max": 2,
    "career_center_study_levels": [
        1,
        2,
        3,
        4,
        5
    ],
    "locations": [
        "Finland::Pirkanmaa::Tampere::Tampere"
    ],
    "locales": [
        "en",
        "fi"
    ],
    "contract_types": [
        "job",
        "cdd",
        "cdi",
        "part_time",
        "stage",
        "company_inside",
        "internship",
        "thesis",
        "thesis"
    ],
    "curriculum_ids": [
        "f5d66eac-700a-41c8-9943-6604e9b103d8"
    ],
    "radius_km": 200
}
json_data = requests.post(url, json=header).content
parsed_data = json.loads(json_data)
job_ad_id = []
title = []
description = []
contract_type = []
location = []
company_id = []
company_name = []
company_logo_url = []
work_experience = []
position_category = []


# Timestamp for 30 days ago
thirty_days_ago = datetime.now() - timedelta(days=30)

# Logic
# Delete job ads older than 30 days from the database
delete_old_jobs_query = """
DELETE FROM job_ads
WHERE created_at < %s
"""
mycursor.execute(delete_old_jobs_query, (thirty_days_ago,))

for job in parsed_data["job_ads"]:
    if "company" in job and "id" in job["company"]:    
        job_ad_id.append(job["id"])
        title.append(job["title"])
        description.append(job["description"])
        contract_type.append(job["contract"]["type"])
        location.append(job["location"]["country"])
        company_id.append(job["company"]["id"])
        company_name.append(job["company"]["name"])
        company_logo_url.append(job["company"]["logo_url"])
        work_experience.append(job["work_experience"])
        position_category.append(job["position_category"])

for i in range(len(job_ad_id)):
    # Check if the company with the same ID already exists
    check_company_sql = "SELECT * FROM companies WHERE id = %s"
    check_company_values = (company_id[i],)
    mycursor.execute(check_company_sql, check_company_values)
    existing_company = mycursor.fetchone()

    if existing_company:
        # Update the existing company with new data
        update_company_sql = "UPDATE companies SET name = %s, logo_url = %s WHERE id = %s"
        update_company_values = (company_name[i], company_logo_url[i], company_id[i])
        mycursor.execute(update_company_sql, update_company_values)
    else:
        # Insert new company
        insert_company_sql = "INSERT INTO companies(id, name, logo_url) VALUES (%s, %s, %s)"
        insert_company_values = (company_id[i], company_name[i], company_logo_url[i])
        mycursor.execute(insert_company_sql, insert_company_values)

    # Check if the job ad with the same ID already exists
    check_job_ad_sql = "SELECT * FROM job_ads WHERE id = %s"
    check_job_ad_values = (job_ad_id[i],)
    mycursor.execute(check_job_ad_sql, check_job_ad_values)
    existing_job_ad = mycursor.fetchone()

    if existing_job_ad:
        # Update the existing job ad with new data
        update_job_ad_sql = """
            UPDATE job_ads
            SET title = %s, description = %s, contract_type = %s, location = %s, company_id = %s, work_experience = %s
            WHERE id = %s
        """
        update_job_ad_values = (
            title[i], description[i], contract_type[i], location[i], company_id[i], work_experience[i], job_ad_id[i]
        )
        mycursor.execute(update_job_ad_sql, update_job_ad_values)
    else:
        # Insert new job ad
        insert_job_ad_sql = """
            INSERT INTO job_ads(id, title, description, contract_type, location, company_id, work_experience)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        insert_job_ad_values = (
            job_ad_id[i], title[i], description[i], contract_type[i], location[i], company_id[i], work_experience[i]
        )
        mycursor.execute(insert_job_ad_sql, insert_job_ad_values)

    # Check if the category with the same job_ad_id already exists
    check_category_sql = "SELECT * FROM categories WHERE job_ad_id = %s"
    check_category_values = (job_ad_id[i],)
    mycursor.execute(check_category_sql, check_category_values)
    existing_category = mycursor.fetchone()

    if not existing_category:
        # Insert new category
        insert_category_sql = "INSERT INTO categories(job_ad_id, category) VALUES (%s, %s)"
        insert_category_values = (job_ad_id[i], position_category[i])
        mycursor.execute(insert_category_sql, insert_category_values)

# Committing the queries and closing the database connection
mydb.commit()
mydb.close()
