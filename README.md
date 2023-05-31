# My Python Library

Easy PYPDF allows you to generate reports with customizable titles, headers, and sections. The library accepts data in a specific format, as shown below.

## Data Format

The data for the library should be provided as a Python dictionary with the following structure:

```python
data = {
    'report': {...},
    'header': {...},
    'section': {...}
}
```

### Report Configuration

| Key               | Type  | Description                                                                                                                                 | Default | Required |
|-------------------|-------|---------------------------------------------------------------------------------------------------------------------------------------------|---------|----------|
| title             | str   | The title of the report.                                                                                                                    |         | Yes      |
| font              | str   | The font used for the title. Options: Courier, Times, Arial, Symbol, ZapfDingbats.                                                          | Courier | No       |
| font_size         | int   | The font size of the title.                                                                                                                 | 22      | No       |
| font_color        | tuple | The font color of the title, provided as (R, G, B).                                                                                         | (0, 0, 0) | No       |
| style             | str   | The style of the title. Accepted values: "B", "I", "U", "BU", "UB", "BI", "IB", "IU", "UI", "BIU", "BUI", "IBU", "IUB", "UBI", "UIB". | B       | No       |
| show_report_title | bool  | A flag to show or hide the title.                                                                                                           | True    | No       |

### Header Configuration

| Key          | Type  | Description                                                                                                                        | Default      | Required |
|--------------|-------|------------------------------------------------------------------------------------------------------------------------------------|--------------|----------|
| title_list   | list  | A list of strings containing the header titles.                                                                                    |              | Yes      |
| value_list   | list  | A list of strings containing the header values.                                                                                    |              | Yes      |
| font         | str   | The font used for the header. Options: Courier, Times, Arial, Symbol, ZapfDingbats.                                               | Courier      | No       |
| font_size    | int   | The font size of the header.                                                                                                       | 12           | No       |
| font_color   | tuple | The font color of the header, provided as (R, G, B).                                                                               | (0, 255, 0)  | No       |
| style        | str   | The style of the header. Accepted values: "B", "I", "U", "BU", "UB", "BI", "IB", "IU", "UI", "BIU", "BUI", "IBU", "IUB", "UBI", "UIB". | B            | No       |
| show_header  | bool  | A flag to show or hide the header.                                                                                                 | True         | No       |

### Section Configuration

| Key              | Type  | Description                                                                                                                        | Default      | Required |
|------------------|-------|------------------------------------------------------------------------------------------------------------------------------------|--------------|----------|
| section_content  | list  | A list of dictionaries containing the section titles and content.                                                                  |              | Yes      |
| title_font       | str   | The font used for the section titles. Options: Courier, Times, Arial, Symbol, ZapfDingbats.                                       | Courier      | No       |
| title_font_size  | int   | The font size of the section titles.                                                                                               | 12           | No       |
| title_font_color | tuple | The font color of the section titles, provided as (R, G, B).                                                                       | (0, 255, 0)  | No       |
| title_style      | str   | The style of the section titles. Accepted values: "B", "I", "U", "BU", "UB", "BI", "IB", "IU", "UI", "BIU", "BUI", "IBU", "IUB", "UBI", "UIB". | B            | No       |
| content_font     | str   | The font used for the section content. Options: Courier, Times, Arial, Symbol, ZapfDingbats.                                       | Courier      | No       |
| content_font_size | int   | The font size of the section content.                                                                                              | 12           | No       |
| content_font_color | tuple | The font color of the section content, provided as (R, G, B).                                                                      | (0, 255, 0)  | No       |
| content_style    | str   | The style of the section content. Accepted values: "B", "I", "U", "BU", "UB", "BI", "IB", "IU", "UI", "BIU", "BUI", "IBU", "IUB", "UBI", "UIB". | B            | No       |
| content_indent   | bool  | A flag to enable or disable indentation for the section content.                                                                   | True         | No       |

## Example

```python
data = {
    'report': {
        'title': 'Hello World',
        'font': 'Courier',
        'font_size': 22,
        'font_color': (0, 0, 0),
        'style': 'B',
        'show_report_title': True,
    },
    'header': {
        'title_list': ["Student Name", "Roll No", "Date"],
        'value_list': ["Alson Prasai", "123456", "2015-05-05"],
        'font': 'Courier',
        'font_size': 12,
        'font_color': (0, 255, 0),
        'style': 'B',
        'show_header': True,
    },
    'section': {
        'section_content': [{
            'title_name_1': 'Title 1',
            'content_1': "Value 1",
            'title_name_2': 'Title 2',
            'content_2': "Value 2",
        }],
        'title_font': 'Courier',
        'title_font_size': 12,
        'title_font_color': (0, 255, 0),
        'title_style': 'B',
        'content_font': 'Courier',
        'content_font_size': 12,
        'content_font_color': (0, 255, 0),
        'content_style': 'B',
        'content_indent': True,
    }
}
```

Provide the `data` dictionary to the library to generate the report with the desired configuration.