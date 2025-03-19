"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Join the soccer team and compete in matches",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 22,
        "participants": ["liam@mergington.edu", "noah@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Join the basketball team and compete in games",
        "schedule": "Wednesdays and Fridays, 3:00 PM - 4:30 PM",
        "max_participants": 15,
        "participants": ["james@mergington.edu", "benjamin@mergington.edu"]
    },
    "Tennis Club": {
        "description": "Learn and play tennis matches",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 10,
        "participants": ["amelia@mergington.edu", "harper@mergington.edu"]
    },
    "Swimming Team": {
        "description": "Join the swimming team and compete in swim meets",
        "schedule": "Tuesdays and Thursdays, 3:00 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["lucas@mergington.edu", "mason@mergington.edu"]
    },
    "Art Club": {
        "description": "Explore various forms of visual arts",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["ella@mergington.edu", "avery@mergington.edu"]
    },
    "Drama Club": {
        "description": "Participate in theater productions and acting workshops",
        "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": ["scarlett@mergington.edu", "grace@mergington.edu"]
    },
    "Math Club": {
        "description": "Solve challenging math problems and compete in math contests",
        "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
        "max_participants": 25,
        "participants": ["ethan@mergington.edu", "alexander@mergington.edu"]
    },
    "Debate Team": {
        "description": "Develop argumentation skills and compete in debates",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["henry@mergington.edu", "jackson@mergington.edu"]
    }
}
        


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    # Validate student is not already signed
    for activity in activities.values():
        if email in activity["participants"]:
            raise HTTPException(status_code=400, detail="Student is already signed up for an activity")
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specificy activity
    activity = activities[activity_name]

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
