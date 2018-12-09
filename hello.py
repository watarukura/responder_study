import responder

api = responder.API()

@api.route("/")
def hello_world(req, resp):
    resp.text = "hello, world!"

@api.route("/hello/{who}")
def hello_to_who(req, resp, *, who):
    resp.text = f"hello, {who}!"

@api.route("/hello/{who}/json")
def hello_to_who_json(req, resp, *, who):
    resp.media = {"hello": who}

@api.route("/hello/{who}/html")
def hello_html(req, resp, *, who):
    resp.content = api.template('hello.html', who=who)

if __name__ == "__main__":
    api.run()