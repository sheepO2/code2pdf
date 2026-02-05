import tempfile
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from pdf_utils import build_pdf

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request},
    )


def decode_file(raw: bytes) -> str:
    for enc in ("utf-8", "gbk", "gb2312", "utf-16"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            pass
    return raw.decode("utf-8", errors="replace")


@app.post("/convert")
async def convert(files: list[UploadFile] = File(...)):
    collected = []

    for f in files:
        raw = await f.read()
        collected.append((f.filename, decode_file(raw)))

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    build_pdf(collected, tmp.name)

    return FileResponse(
        tmp.name,
        media_type="application/pdf",
        filename="merged_code.pdf",
    )
