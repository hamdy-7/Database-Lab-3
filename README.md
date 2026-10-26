# Lab 3 - Database Systems

This repository contains the full solution for Lab 3, including DDL/DML scripts for Company and Library databases, along with a Flask Web Application for managing the Library system with image upload bonus features.

## Project Structure
- `problem1_DDL.sql` - Schema for Company Database
- `problem1_DML.sql` - Data insertion for Company Database
- `problem1_Answers.txt` - Written answers for Problem 1 tasks
- `problem2_DDL.sql` - Schema for Library Database (Author & Book)
- `problem2_DML.sql` - Data insertion for Library Database
- `website/` - Flask Web Application
  - `app.py` - Main Application logic
  - `.env` - Environment Configuration
  - `requirements.txt` - Python Dependencies
  - `templates/` - HTML Templates
  - `static/uploads/` - Image Uploads Storage

## How to Run the Website
1. Execute `problem2_DDL.sql` and `problem2_DML.sql` in MySQL / DBeaver.
2. Navigate to the website folder:
   ```bash
   cd website