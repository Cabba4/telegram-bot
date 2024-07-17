import traceback
from telegram.ext import ContextTypes
from telegram import Update
from Translator import t  # Assuming this is your translation module
import mysql.connector

from models.JobAd import JobAd

# get job data from the database
def get_job_data_from_database():
    try:
        return JobAd.getAll()

    except mysql.connector.Error as err:
        traceback.print_exc()
        raise

# job listing handler
async def job_list_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        language = "en"
        list_jobs_message = t("list jobs message", language) + "\n"

        job_list = get_job_data_from_database()

        if job_list:
            message = list_jobs_message 
            for job in job_list:
                message += job.__str__() + "\n"

            await update.message.reply_markdown(message)
        else:

            await update.message.reply_markdown(list_jobs_message + t("no jobs found"))

    except Exception as e:
        traceback.print_exc()
        error_message = t("error", language)
    await update.message.reply_markdown(error_message)
