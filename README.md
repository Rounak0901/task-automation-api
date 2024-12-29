# Task Scheduling API

This project provides a simple API for scheduling and managing tasks. It's built using FastAPI, SQLAlchemy, and APScheduler.

## Features

- **Create, update, and delete tasks:** Easily manage your tasks through the API.
- **Schedule tasks using cron expressions:** Define flexible schedules for
 your tasks.
- **View task status and last run time:** Monitor the execution of your tasks.
- **Data validation and serialization:** Uses Pydantic for data integrity.
- **Built with FastAPI:** Enjoy a modern, fast, and well-documented API framework.
- **Persistent storage with SQLAlchemy:** Store task data in a relational database.
- **Scheduled execution with APScheduler:** Ensure tasks run at specified intervals.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- SQLAlchemy
- APScheduler
- Pydantic

## Installation

1. **Clone the repository:**

2. **Install dependencies:**

3. **Customize your Project IDX environment (optional):**
   You can tailor your development environment by editing the `.idx/dev.nix` file. This allows you to install additional tools, IDE extensions, and set environment variables.
   Learn more: [Customize your IDX environment](https://developers.google.com/idx/guides/customize-idx-env)

## Usage

1. **Start the server:**
bash uvicorn main:app --reload

2. **Access the API documentation:**
   Open your web browser and navigate to:

http://localhost:8000/docs

You'll find interactive API documentation powered by Swagger UI, allowing you to explore and test the API endpoints.


