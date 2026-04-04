# Task Management Application

A simple REST API built with **FastAPI** for managing tasks.

## Project Structure

- `main.py`: Entry point for the FastAPI application. Sets up database connections and includes route definitions.
- `src/`: Core application logic.
  - `task/`: Task-related models, routers, and logic.
  - `user/`: User-related modules and management logic.
  - `utils/`: Utilities like database connection (`db.py`).
- `.env`: Environment variables (do not commit this).
- `requirement.txt`: Project dependencies.

## Setup Instructions

1. **Activate the virtual environment**:
   ```bash
   venv\Scripts\activate
   ```

2. **Install dependencies**:
   Ensure all dependencies are installed using the `requirement.txt` file:
   ```bash
   pip install -r requirement.txt
   ```

3. **Configure Environment Variables**:
   Update your `.env` file with the required variables (e.g., Database connection string).

4. **Run the Application**:
   Start the FastAPI development server using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```
   
5. **API Documentation**:
   Once running, you can view the fully interactive Swagger documentation at:
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)