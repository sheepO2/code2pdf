# Code2PDF (Convert Source Code to PDF)

A lightweight web-based tool that converts source code files into PDF documents
with a single click.

---

## Features

- **Code → PDF**: Upload or paste source code files and generate PDFs instantly
- **Monospaced font**: Optimized for reading source code
- **CJK-friendly**: Built-in CJK font support for Chinese and Japanese content
- **Web interface**: Works directly in the browser
- **Lightweight**: No database, no authentication, minimal dependencies

---

## Supported File Types

This tool supports **plain-text source files**, including but not limited to:

- Programming languages:  
  `.py`, `.js`, `.ts`, `.java`, `.c`, `.cpp`, `.go`, `.rs`, `.php`

- Markup and configuration files:  
  `.html`, `.css`, `.json`, `.yaml`, `.toml`, `.ini`

- Documentation and scripts:  
  `.md`, `.txt`, `.sql`, `.sh`, `.bat`

> Binary files (such as images, PDFs, and Office documents) are intentionally not supported.

---

## Project Structure
~~~
code2pdf/
├── app.py # Web application entry point
├── pdf_utils.py # Core PDF generation logic
├── templates/
│ └── index.html # Frontend page
├── static/ # Static assets
├── fonts/ # Monospaced fonts with CJK support
│ ├── DejaVuSansMono.ttf
└── └── NotoSansMonoCJKsc-Regular.otf
~~~

---

## Running the Server

```bash
cd code2pdf
uvicorn app:app
```

```
http://127.0.0.1:8000
```
---

### Usage

1. Open the web page

2. Upload source code files

3. Click **Generate PDF**

4. Download the generated PDF
---

## Tech Stack

* Python

* Flask (or other lightweight web framework)

* ReportLab (PDF generation)

* HTML / CSS
---

## Notes

* This project does **not include security hardening**

* Intended for local or internal network use

* Syntax highlighting is not included by design

## Use Cases

* Student assignments or lab reports

* Code review attachments

* Code samples for resumes or portfolios