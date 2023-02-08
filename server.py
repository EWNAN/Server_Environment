#gunicorn
def render_template(template_name = 'index.html'):
        return "<h1>Hello World</h1>"

def app(environ, start_response):
       # data = "Hello World!!!!!"
        data = render_template()
        data = data.encode("utf-8")
        
        start_response(
            f"200 OK", [
                ("Content-type", "text/HTML"), # for the HTML style to work effectively the text style has to be HTML not plain
                ("Content-length", str(len(data)))
            ]
        )
        return iter([data])