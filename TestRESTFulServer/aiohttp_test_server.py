from aiohttp import web

routes = web.RouteTableDef()


@routes.post('/')
async def echo(request):
    print('headers=%r' % request.headers)
    print('message=%r' % request.message)
    data = await request.post()
    print('data=%r' % data.keys())

    data = {"data": [
       "app",
       "calico-system",
       "cicd",
       "contoso",
       "default",
       "devops",
       "ingress-basic",
       "kube-node-lease",
       "kube-public",
       "kube-system",
       "kubeapps",
       "monitoring",
       "tigera-operator",
       "wordpress"],
       "message": "OK"}
    return web.json_response(data)

app = web.Application()
app.add_routes(routes)
web.run_app(app)
