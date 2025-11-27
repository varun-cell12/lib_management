# Library Management System – Project Statement

## Problem Statement
Small libraries and individual book owners often manage their collections manually using notebooks or scattered files.  
This makes it difficult to quickly add, update, search, or remove records when the number of books grows.  
There is a need for a simple, menu‑driven application that can maintain book details in a structured digital format.

## Scope of the Project
The project focuses on a command‑line Library Management System built using Python and CSV file storage.  
It supports basic book record management but does not cover advanced features like member management, issue/return tracking, or fines.  
The system is intended for small‑scale use where a lightweight solution without a full database is sufficient.

## Target Users
- Students who want a simple project to learn file handling and modular programming in Python.  
- Teachers who need a small demonstration tool for CRUD operations using CSV files.  
- Individuals or small personal libraries needing a basic catalog of books.

## High‑Level Features
1. **Add Book**  
   - Allows the user to add a new book record with ID, name, author, price, and number of copies.  

2. **Modify Book**  
   - Locates a book by its ID, shows current details, and lets the user update the information.  

3. **Delete Book**  
   - Locates a book by its ID and removes it from the CSV file after confirmation.  

4. **Search Book**  
   - Searches for a book by ID and displays its details if found, otherwise shows “Record not found”.  

5. **List All Books**  
   - Displays all existing book records from the CSV file in a simple text format.

These five features form the main functional modules and satisfy the requirement of having at least three major functional modules with a clear input/output structure and logical workflow.
