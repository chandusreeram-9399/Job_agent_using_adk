from google.adk.agents import Agent
from typing import Dict, List, Optional
import datetime

# Sample job database
JOB_DATABASE = {
    "software_engineer": {
        "title": "Software Engineer",
        "department": "Engineering",
        "location": "New York",
        "status": "Open",
        "posted_date": "2024-03-01",
        "requirements": [
            "Bachelor's degree in Computer Science",
            "3+ years of experience in Python",
            "Experience with cloud technologies"
        ]
    },
    "product_manager": {
        "title": "Product Manager",
        "department": "Product",
        "location": "San Francisco",
        "status": "Open",
        "posted_date": "2024-03-15",
        "requirements": [
            "5+ years of product management experience",
            "Strong analytical skills",
            "Experience with agile methodologies"
        ]
    },
    "data_scientist": {
        "title": "Data Scientist",
        "department": "Data Science",
        "location": "Remote",
        "status": "Open",
        "posted_date": "2024-03-10",
        "requirements": [
            "Master's degree in Data Science",
            "2+ years of experience in machine learning",
            "Proficiency in Python and SQL"
        ]
    }
}

def get_job_openings(department: Optional[str] = None, location: Optional[str] = None, job_title: Optional[str] = None) -> Dict:
    """Retrieves job openings based on department, location, and job title filters.
    
    Args:
        department (Optional[str]): Filter by department. Defaults to None.
        location (Optional[str]): Filter by location. Defaults to None.
        job_title (Optional[str]): Filter by job title. Defaults to None.
        
    Returns:
        Dict: List of matching job openings and their details.
    """
    matching_jobs = []
    
    for job_id, job_info in JOB_DATABASE.items():
        if job_info["status"] == "Open":
            # Check department if specified
            if department and job_info["department"].lower() != department.lower():
                continue
            # Check location if specified
            if location and job_info["location"].lower() != location.lower():
                continue
            # Check job title if specified
            if job_title and job_info["title"].lower() != job_title.lower():
                continue
            matching_jobs.append(job_info)
    
    return {
        "status": "success",
        "count": len(matching_jobs),
        "jobs": matching_jobs
    }

def get_job_details(job_title: str) -> Dict:
    """Retrieves detailed information about a specific job.
    
    Args:
        job_title (str): The title of the job to get details for.
        
    Returns:
        Dict: Detailed information about the job or error message.
    """
    for job_id, job_info in JOB_DATABASE.items():
        if job_info["title"].lower() == job_title.lower():
            return {
                "status": "success",
                "job_details": job_info
            }
    
    return {
        "status": "error",
        "error_message": f"No job found with title '{job_title}'"
    }

def check_application_status(application_id: str) -> Dict:
    """Checks the status of a job application.
    
    Args:
        application_id (str): The ID of the application to check.
        
    Returns:
        Dict: Application status information.
    """
    # This is a mock implementation
    return {
        "status": "success",
        "application_status": "Under Review",
        "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

root_agent = Agent(
    name="job_info_agent",
    model="gemini-2.0-flash",  # Updated to valid model name
    description=(
        "Agent to provide information about job openings, vacancies, "
        "and application status in the company."
    ),
    instruction=(
        "You are a helpful HR assistant who can provide information about "
        "job openings, vacancies, and application status. You can help users "
        "find suitable positions, check job requirements, and track their "
        "application status. You support both text and voice interactions."
    ),
    tools=[get_job_openings, get_job_details, check_application_status],
) 