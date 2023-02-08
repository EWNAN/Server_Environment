#gunicorn
def render_template(template_name = 'index.html', context={}):
    html_str = ""
    with open(template_name, 'r') as f:
        html_str = f.read()
        html_str = html_str.format(**context)
        return html_str


def home(environ):
    return render_template(
        template_name= "index.html",
        context= {}
    )

def Contact_us(environ):
    return render_template(
        template_name= "contact.html",
        context= {}
    )    

def app(environ, start_response):
        path = environ.get("PATH_INFO")
        if path.endswith("/"):
            path = path[:-1]
        if path == "/":
            data = home(environ)
        elif path == "/contact":
            data = Contact_us(environ)    
        else:
            data = render_template(template_name = '404.html', path=path)
        #for k, v in environ.items():
       #     print(k,v)
       # data = "Hello World!!!!!"
       # data = render_template()
        data = data.encode("utf-8")
        
        start_response(
            f"200 OK", [
                ("Content-type", "text/HTML"), # for the HTML style to work effectively the text style has to be HTML not plain
                ("Content-length", str(len(data)))
            ]
        )
        return iter([data])