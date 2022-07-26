from os import getenv

from aiohttp.web import Application, HTTPFound, run_app

app = Application()
app.router.add_static("/files/", ".", show_index=True)


async def root_handler(request):
    return HTTPFound("https://google.com")


app.router.add_route("*", "/", root_handler)

run_app(app, port=int(getenv("PORT", "80")))
