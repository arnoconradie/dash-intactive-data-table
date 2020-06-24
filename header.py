import dash_html_components as html
import dash_core_components as dcc


def Header():
    return html.Div([
        get_logo(),
        get_header(),
        html.Br([]),
        get_menu()
    ])

def get_logo():
    logo = html.Div([
        html.Div([
            html.Img(src= 'https://i.pinimg.com/564x/4a/bc/38/4abc38758eba60d6712bd86dd1542697.jpg', height='101', width='141')
        ])

    ], className="row gs-header")

    return logo

def get_header():
    header = html.Div([
        html.Div([
             html.H5(
                 'House Start Performance Marketing Report'
             )
        ] , className="twelve columns padded")
    ], className="row gs-header gs-text-header")
    return header

def get_menu():
    menu = html.Div([
        dcc.Link('Overview - Birst', href='/cc-travel-report/overview-birst/', className="tab first"),

        dcc.Link('Overview - GA   ', href= '/cc-travel-report/overview-ga/', className="tab first"),

        dcc.Link('Paid Search   ', href= 'cc-travel-report/paid-search/', className="tab first"),

        dcc.Link('Display   ', href= '/cc-travel-report/display/', className="tab first"),

        dcc.Link('Publishing   ', href= '/cc-travel-report/publishing/', className="tab first"),

        dcc.Link('Metasearch and Travel Ads   ', href='/cc-travel-report/metasearch-and-travel-ads/', className="tab first"),
    ], className="row ")

    return menu