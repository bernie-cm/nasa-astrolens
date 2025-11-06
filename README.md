# AstroLens APOD Web App with NASA API integration

Built a **FastAPI** backend and **React** frontend to fetch and display NASA's Astronomy Picture of the Day for any date, using NASA's public APOD API.

## Technologies
- Backend: FastAPI, Python
- Frontend: React
- External API: NASA APOD API

## Setup Instructions

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```
