#
# see https://shenli.dev/2020/06/20/asgi-from-scratch.html
#
# {
#     "type": "http",
#     "http_version": "1.1",
#     "server": ("127.0.0.1", 8000),
#     "client": ("127.0.0.1", 60457),
#     "scheme": "http",
#     "method": "GET",
#     "root_path": "",
#     "path": "/hello/a",
#     "raw_path": b"/hello/a",
#     "query_string": b"",
#     "headers": [
#         (b"host", b"localhost:8000"),
#         (b"connection", b"keep-alive"),
#         (
#             b"user-agent",
#             b"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 ...",
#         ),
#         (
#             b"accept",
#             b"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#         ),
#         (b"accept-encoding", b"gzip, deflate, br"),
#         (b"accept-language", b"en-US,en;q=0.9"),
#         (
#             b"cookie",
#             b'csrftoken=dDA2IAPrvgPc7hkyBSyctxDk78KmhHAzUqR0LUpjXI3Xgki0QrGEWazE3RGZuLGl',
#         ),
#     ],
# }

async def application(scope, receive, send):
    name = scope["path"].split("/", 1)[-1] or "world"
    await send(
        {
            "type": "http.response.start",
            "status": 200,
            "headers": [[b"content-type", b"text/plain"],],
        }
    )
    await send(
        {
            "type": "http.response.body",
            "body": f"Hello, {name}!".encode(),
            "more_body": False,
        }
    )

