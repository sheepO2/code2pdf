# Code2PDF（代码文件转PDF格式）

一个**把代码一键转成 PDF** 的轻量级 Web 工具。

---

## 功能特性

*  **代码 → PDF**：支持直接粘贴或上传代码文件
*  **等宽字体**：专为代码阅读优化
*  **中英文友好**：内置 CJK 字体，中文不乱码
*  **Web 界面**：打开浏览器就能用
*  **轻量**：无数据库、无鉴权、无多余依赖  
---

##  支持的文件类型

本工具支持 **纯文本类型的源码文件**，包括但不限于：

- 编程语言：  
  `.py`, `.js`, `.ts`, `.java`, `.c`, `.cpp`, `.go`, `.rs`, `.php`

- 标记与配置文件：  
  `.html`, `.css`, `.json`, `.yaml`, `.toml`, `.ini`

- 文档与脚本：  
  `.md`, `.txt`, `.sql`, `.sh`, `.bat`

> 出于设计考虑，二进制文件（如图片、PDF、Office 文档）不在支持范围内。

---


##  项目结构

```
code2pdf/
├── app.py              # Web 应用入口
├── pdf_utils.py        # PDF 生成核心逻辑
├── templates/
│   └── index.html      # 前端页面
├── static/             # 静态资源
├── fonts/              # 等宽字体（含中日韩支持）
│     ├── DejaVuSansMono.ttf
└──   └── NotoSansMonoCJKsc-Regular.otf
```

### 启动服务

```bash

cd code2pdf
uvicorn app:app

```

启动后在浏览器访问：

```
http://127.0.0.1:8000
```

---

##  使用说明

1. 打开网页
2. 上传代码文件
3. 点击 **Generate PDF**
4. 下载生成的 PDF
---

##  技术栈

* Python
* Flask（或轻量 Web 框架）
* ReportLab（PDF 生成）
* HTML / CSS

---

##  注意事项

* 本项目 **不做安全防护**，默认用于本地或内网
* 不建议直接暴露到公网
* 当前更偏向代码展示，不做语法高亮

---

##  适用场景

* 学生作业 / 实验报告
* 代码评审附件
* 简历项目代码展示
