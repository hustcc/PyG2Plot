def write_utf8_file(file_name: str, html_content: str):
    with open(file_name, "w+", encoding="utf-8") as html_file:
        html_file.write(html_content)
