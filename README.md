# 🎓 AI-Powered Certificate Generator

This project is a **Streamlit-based web app** that generates personalized **course completion certificates** in bulk using data from a CSV file. It automatically overlays names, course titles, and completion dates onto a certificate template and allows users to download all certificates in a ZIP file.

---

## 🚀 Live App

👉 [Click here to use the app](https://palrajdeep02-ai-certificate-generator-app-owdfgc.streamlit.app/)

---

## 🛠️ Technologies Used

### 🔹 Frontend
- **Streamlit** – for building a simple and interactive web UI

### 🔹 Backend
- **Python** – core programming logic
- **Pandas** – reading and handling CSV data
- **Pillow (PIL)** – editing the certificate image and adding text
- **ZipFile (Standard Library)** – bundling generated PDFs into a ZIP
- **os, io** – file handling and in-memory file generation

---

## ✨ Key Features

- 📥 Upload a CSV file containing student `Name`, `Course`, and `Date`
- ✏️ Use default course/date values if not present in the CSV
- 📄 Automatically generate personalized **PDF certificates**
- 📦 Download all certificates in a single **ZIP file**
- 🖼️ Uses a PNG template and custom fonts for clean styling
- 🧭 Lightweight Streamlit UI with optional branding (logo)

---

## 📑 Input CSV Format

The uploaded `.csv` file should have these columns:


- If `Course` or `Date` is empty, the app will use the default values entered in the form.

---

## 📤 Output

- Each row in the CSV results in a personalized **PDF certificate**
- All PDFs are saved into the `/output` folder and zipped into `certificates.zip`
- Users can download the ZIP directly from the app

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
