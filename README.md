# 🍬 Sweet Shop Management System

A full-stack web application for managing the inventory of a sweet shop, built with **Python**, **Flask**, and a dynamic web front-end. This project was developed following a **Test-Driven Development (TDD)** methodology.

---

## ✨ Features

- **Full CRUD Functionality:** Add, edit, and delete sweets from the inventory.
- **Inventory Management:** Purchase and restock sweets, with stock levels automatically updated.
- **Interactive UI:** A clean, modern, and responsive user interface built with Bootstrap.
- **Dynamic Modals:** Add and edit sweets without leaving the page using interactive modals.


---

## Webpage  

<img width="1024" height="535" alt="image" src="https://github.com/user-attachments/assets/a22ce3a5-3930-420a-a812-5a0eb59ef1a3" />

---


## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, Bootstrap 5, JavaScript
- **Testing:** Pytest

---

## 📂 Project Structure

```
/sweet-shop-management/
|
|-- sweet_shop/
|   |-- __init__.py
|   |-- shop.py         # Core business logic for the shop
|   `-- sweet.py        # Data class for a Sweet object
|
|-- tests/
|   `-- test_sweet_shop.py # Unit tests for the shop logic
|
|-- templates/
|   `-- index.html      # Main HTML template for the web app
|
|-- static/
|   `-- sweet_background.png # Background image
|
|-- app.py              # Flask application server
|
`-- README.md           # This file
```

---

## 🚀 Setup and Installation

Follow these steps to get the application running on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/sweet-shop-management.git
cd sweet-shop-management
```

### 2. Create and Activate a Virtual Environment

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install Flask pytest
```

### 4. Run the Application

```bash
python app.py
```

The application will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000) in your web browser.

---

## 🧪 Running Tests

This project was built using Test-Driven Development. To run the full suite of unit tests, use:

```bash
pytest
```

---

## 💡 Future Improvements

- **Database Integration:** Replace the in-memory dictionary with a persistent database like SQLite or PostgreSQL.
- **User Authentication:** Add user accounts and login functionality.
- **Advanced Search & Filtering:** Implement the search and filter features in the UI.
- **API Endpoints:** Create a RESTful API to allow other applications to interact with the inventory.

---
