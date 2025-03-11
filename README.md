# 🚀 FastAPI Side Hustles & Money Quotes API

A simple **FastAPI** application that provides random **side hustle ideas** and **money-related quotes** through API endpoints.

## 🌟 Features

✅ **Get a random side hustle idea** 💼  
✅ **Get a random money-related quote** 💰  
✅ **Secure API with an API key** 🔑  
✅ **Fast & lightweight with FastAPI** ⚡  
✅ **Easy to deploy and integrate** 🌍  

---

## 🛠️ Installation & Setup

Follow these steps to run the API on your local machine:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/codewithshabbir/simple-api-python
cd simple-api-python
```

### 2️⃣ Install Dependencies
```bash
pip install fastapi uvicorn
```

### 3️⃣ Run the API
```bash
uvicorn main:app --reload
```

---

## 📡 API Endpoints

### 🔹 Get a Random Side Hustle
**Endpoint:**
```
GET /side-husstles?apiKey=123456789
```
**Response:**
```json
{
  "side-husstles": "Freelancing (Upwork, Fiverr, Toptal)"
}
```

### 🔹 Get a Random Money Quote
**Endpoint:**
```
GET /money-quotes?apiKey=123456789
```
**Response:**
```json
{
  "money-quotes": "Don’t work for money, make money work for you. – Robert Kiyosaki"
}
```

---

## 🌍 Live Demo
Check out the live version of this API:  
🔗 **[Live API](https://simple-api-codewithshabbir.streamlit.app/)**

---

## 👨‍💻 Developer
Made with ❤️ by **[Muhammad Shabbir](https://codewithshabbir.vercel.app/)**

📌 **GitHub:** [@codewithshabbir](https://github.com/codewithshabbir)  
📌 **Portfolio:** [codewithshabbir.vercel.app](https://codewithshabbir.vercel.app/)

---

## 📜 License
This project is open-source and available under the **MIT License**.