#gunicorn
def render_template(template_name = 'index.html'):
        return "Hello World"

def app(environ, start_response):
        data = "Hello World!"
        data = data.encode("utf-8")
        #data = render_template()
        start_response(
            f"200 OK", [
                ("Content-type", "text/plain"), # for the HTML style to work effectively the text style has to be HTML not plain
                ("Content-length", str(len("data")))
            ]
        )
        return iter([data])