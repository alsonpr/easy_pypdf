from pdf_generator import generate_report


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
            'title_name_1': 'Product',
            'content_1': "Widget",
            'title_name_2': 'Sales',
            'content_2': "$10,000",
        },{
            'title_name_1': 'Product',
            'content_1': "Gadget",
            'title_name_2': 'Sales',
            'content_2': "$7,500",
        },{
            'title_name_1': 'Product',
            'content_1': "Doohickey",
            'title_name_2': 'Sales',
            'content_2': "$5,000",
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
