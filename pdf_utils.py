from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

# 注册内置中文字体（不需要任何字体文件）
pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))

PAGE_WIDTH, PAGE_HEIGHT = A4

LEFT_MARGIN = 40
TOP_MARGIN = 40
BOTTOM_MARGIN = 40

FONT_NAME = "STSong-Light"
FONT_SIZE = 9
LINE_HEIGHT = FONT_SIZE + 4


def build_pdf(files: list[tuple[str, str]], output_path: str):
    """
    files: [(filename, file_content), ...]
    """
    c = canvas.Canvas(output_path, pagesize=A4)
    c.setFont(FONT_NAME, FONT_SIZE)

    y = PAGE_HEIGHT - TOP_MARGIN

    for filename, content in files:
        # 文件标题
        c.drawString(LEFT_MARGIN, y, f"=== {filename} ===")
        y -= LINE_HEIGHT * 2

        for line in content.splitlines():
            if y < BOTTOM_MARGIN:
                c.showPage()
                c.setFont(FONT_NAME, FONT_SIZE)
                y = PAGE_HEIGHT - TOP_MARGIN

            # 直接写，不做任何 ASCII 过滤
            c.drawString(LEFT_MARGIN, y, line)
            y -= LINE_HEIGHT

        # 每个文件强制换页
        c.showPage()
        c.setFont(FONT_NAME, FONT_SIZE)
        y = PAGE_HEIGHT - TOP_MARGIN

    c.save()
