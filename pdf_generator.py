from fpdf import FPDF


def set_default_report_value(report):
    report.setdefault('font', 'times')
    report.setdefault('font_size', 14)
    report.setdefault('font_color', (0, 0, 0))
    report.setdefault('style', 'B')
    report.setdefault('show_report_title', False)


def set_default_header_value(report):
    report.setdefault('font', 'Courier')
    report.setdefault('font_size', 12)
    report.setdefault('font_color', (0, 0, 0))
    report.setdefault('style', 'B')
    report.setdefault('show_header', False)


def set_default_section(section):
    section.setdefault('title_font', 'Courier')
    section.setdefault('content_font', 'Courier')
    section.setdefault('title_font_size', 12)
    section.setdefault('content_font_size', 12)
    section.setdefault('title_font_color', (255, 93, 93))
    section.setdefault('content_font_color', (0, 0, 0))
    section.setdefault('title_style', 'B')
    section.setdefault('content_style', '')
    section.setdefault('content_indent', True)


def _generate_report(data,file_name):
    # Create the PDF object
    pdf = FPDF()
    pdf.add_page()
    pdf.set_draw_color(0, 0, 0)
    pdf.set_fill_color(255, 255, 255)

    report = data.get("report")
    header = data.get("header")
    section = data.get("section", {})

    if report:
        set_default_report_value(report)
    if header:
        set_default_header_value(header)
    if section:
        set_default_section(section)

    section_lst = section.get("section_content", [])
    print(report)
    # Add the Report Title
    if report and report["show_report_title"]:
        pdf.set_font(report["font"], report["style"], report["font_size"])
        pdf.set_text_color(*report["font_color"])
        pdf.cell(0, 10, report["title"], 0, 1, "C")
        pdf.cell(0, 10, "", 0, 1, "L")  # add a blank line

    # Add header information
    if header and header["show_header"]:
        pdf.set_font(header["font"], header["style"], header["font_size"])
        pdf.set_text_color(*header["font_color"])

        for title, value in zip(header["title_list"], header["value_list"]):
            pdf.cell(0, 10, f"{title} : {value}", 0, 1, "L")
            pdf.cell(0, 1, "", 0, 1, "L")

    title_font = section.get("title_font")
    title_font_size = section.get("title_font_size")
    title_color = section.get("title_font_color")
    title_style = section.get("title_style")

    content_font = section.get("content_font")
    content_font_size = section.get("content_font_size")
    content_color = section.get("content_font_color")
    content_style = section.get("content_style")
    indent_content = section.get("content_indent")

    for section in section_lst:
        for i in range(len(section)):
            title_name = section.get(f"title_name_{i + 1}", "")
            section_content = section.get(f"content_{i + 1}", "")

            if title_name.strip():
                pdf.set_font(title_font, title_style, title_font_size)
                pdf.set_text_color(*title_color)
                pdf.cell(0, 10, title_name, 0, 1, "L")

            if section_content.strip():
                pdf.set_draw_color(211, 211, 211)  # set border color to light gray
                pdf.set_text_color(*content_color)
                pdf.set_font(content_font, content_style, content_font_size)
                if indent_content:
                    pdf.cell(8)  # add left margin
                pdf.multi_cell(0, 10, section_content, 1, "L", True)

        pdf.cell(0, 2, "", 0, 1, "L")  # add a blank line between each test result
        pdf.set_draw_color(0, 0, 0)  # set border color to red

    file_name = f"{file_name}.pdf"
    pdf.output(file_name, "F")


def generate_report(data,file_name="report"):
    try:
        _generate_report(data,file_name)
        return True
    except Exception as e:
        print("Failed to generate report. Please check the input data", e)
        return False

