from pdf_generator import generate_report

content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris in culpa qui officia deserunt mollit anim id est laborum."
data = {
    'report': {
        'title': 'Sales Report',
        'font': 'Arial',
        'font_size': 24,
        'font_color': (50, 50, 50),
        'style': 'B',
        'show_report_title': True,
    },
    'header': {
        'title_list': ["Salesperson", "Region", "Date"],
        'value_list': ["John Doe", "North America", "2023-05-07"],
        'font': 'Arial',
        'font_size': 14,
        'font_color': (0, 0, 255),
        'style': 'B',
        'show_header': True,
    },
    'section': {
        'section_content': [{
            'title_name_1': 'Product 1',
            'content_1': content,
            'title_name_2': 'Product 2',
            'content_2': content,
        },{
            'title_name_1': 'Product 3',
            'content_1': content,
            'title_name_2': 'Product 4',
            'content_2': content,
        },{
            'title_name_1': 'Product 5',
            'content_1': content,
            'title_name_2': 'Product 6',
            'content_2': content,
        }],
        'title_font': 'Arial',
        'title_font_size': 16,
        'title_font_color': (0, 128, 0),
        'title_style': 'B',
        'content_font': 'Arial',
        'content_font_size': 14,
        'content_font_color': (128, 0, 0),
        'content_style': 'B',
        'content_indent': True,
    }
}
generate_report(data, 'report')
