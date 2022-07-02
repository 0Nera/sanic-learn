from sanic import Sanic
from sanic.response import text
from sanic.response import json


app = Sanic("MyHelloWorldApp")


@app.get("/")
async def hello_world(request):
    return text("Hello, world.")
 

@app.route('/api')
async def test(request):
    return json({'hello': 'world'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)