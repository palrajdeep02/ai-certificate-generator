AI powered Certificate Generator

Used technology: 
Frontend:
•	Streamlit – to create a simple and interactive UI for uploading CSVs, entering course details, and downloading certificates.
Backend:
•	Python – main programming language.
•	Pandas – for reading and handling CSV data (Name, Course, Date).
•	Pillow (PIL) – for loading the certificate template and adding text dynamically (Name, Course, Date).
•	ZipFile (from Python standard library) – to bundle all generated certificates into a downloadable ZIP file.
•	os, io – for file system handling and in-memory zip generation.


Key Features:
•	Upload a CSV with student names, course, and date.
•	Allows default values for course and date if not provided in CSV.
•	Automatically generates personalized PDF certificates for each user.
•	Bulk download of all certificates via a single ZIP file.
•	Basic Streamlit UI with logo and input options.
•	Clean, consistent certificate appearance using a PNG template and custom fonts.

Input CSV Format:
•	Columns supported: Name, Course, Date
•	If Course or Date is missing, the app uses the default values provided in the UI.

Output:
•	For each row in the CSV, a certificate PDF is generated using the template and placed inside the output/ folder.
•	All PDFs are compressed into a single downloadable certificates.zip.

Requirements:
•	streamlit
•	pandas
•	pillow

#To Access The App Click On The Link

https://palrajdeep02-ai-certificate-generator-app-owdfgc.streamlit.app/
