import asyncio
from aiohttp import web, ClientSession
import json
import argparse


async def get_weather(city: str) -> str:
    async with ClientSession() as session:
        url = f'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

        async with session.get(url=url, params=params) as response:
            weather_json = await response.json()
            try:
                return weather_json['weather'][0]['main']
            except KeyError:
                return 'No Data Available'


async def weather_entrypoint(request):
    # return web.Response(text="Welcome home!")
    city = request.rel_url.query['city']
    weather = await get_weather(city)
    result = {'city': city, 'weather': weather}
    return web.Response(text=json.dumps(result, ensure_ascii=False))


async def index(request):
    return web.Response(text="Welcome home!")
    # return handle(request)


# async def main():
#     app.router.add_get('/', index)
#     app.add_routes([web.get('/weather_entrypoint', weather_entrypoint)])
#     runner = web.AppRunner(app)
#     await runner.setup()
#     site = web.TCPSite(runner, "127.0.0.1", 82)
#     await site.start()
#
#     while True:
#         await asyncio.sleep(300)


parser = argparse.ArgumentParser()


def get_opts():
    parser.add_argument('--path')
    parser.add_argument('--port')
    args = parser.parse_args()
    return args


async def deploy_application(args):
    app = web.Application()
    app.add_routes([
        web.get('/', index),
        web.get('/weather_entrypoint', weather_entrypoint)]
    )
    runner = web.AppRunner(app)

    web.run_app(app, path=args.path, port=args.port)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 1234)
    await site.start()


if __name__ == '__main__':
    args = get_opts()
    app = deploy_application(args)

    # asyncio.run(main())
# else:
#     app = web.Application()
#     asyncio.run(main())


# async def weather_entrypoint():
#     app = web.Application()
#     app.add_routes([web.get('/', index)])
#     app.add_routes([web.get('/weather_entrypoint', handle)])
#     return app
#
# app = web.Application()
# asyncio.run(main())
