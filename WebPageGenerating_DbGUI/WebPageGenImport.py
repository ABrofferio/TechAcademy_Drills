import webbrowser

def open_page(name, background, font, size, title, message, userInput):
    website = open("PyDrill_Webpage.html", "w")
    text = """<html>
    <head>
    <title>
    {}
    </title>
    </head>
    <body style = "background-color: {};"
    "font-style: {};"
    "font-size{};" >
    <h1>
    {}
    </h1>
    {}
    <footer>
    {}
    </footer>
    </body>
    </html>""" .format(name, background, font, size, title, message, userInput)
    website.write(text)
    website.close()
def run_webpage():
    filename = 'file: /Users/aja/GitHub/TechAcademy_Drills/WebPageGenerating_DbGUI/PyDrill_Webpage.html'
    webbrowser.open_new_tab(filename)


