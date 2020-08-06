Python ASGI Test
================

Python ASGI-interface & load test.

Install
-------

    python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt


Run
---

    uvicorn main:application


Load Test
---------

First, install wrk from https://github.com/wg/wrk

Tested on a laptop with Intel i7-8750H and 16GB RAM. Note that load is generated on the same computer so not really ideal test.

Window 1:

    uvicorn main:application --workers 12 --no-access-log

Window 2:

    $ wrk -t12 -c400 -d30s http://localhost:8000/hi
    Running 30s test @ http://localhost:8000/hi
      12 threads and 400 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency     3.28ms    3.05ms  61.62ms   92.02%
        Req/Sec    11.37k     3.27k   36.99k    76.20%
      4070408 requests in 30.09s, 570.63MB read
    Requests/sec: 135262.84
    Transfer/sec:     18.96MB
