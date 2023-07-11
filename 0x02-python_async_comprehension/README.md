# Python - Async Comprehension

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uplo…663c75e55926cd52172339585600321003bc9e0921ec405ee)
```
josephgreen@JosephGreen-Mugabi:~/0x02-python_async_comprehension$ cat 1-main.py 
#!/usr/bin/env python3

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def main():
    print(await async_comprehension())

asyncio.run(main())
josephgreen@JosephGreen-Mugabi:~/0x02-python_async_comprehension$ 
```

```
josephgreen@JosephGreen-Mugabi:~/0x02-python_async_comprehension$ ./1-main.py 
[9.80381563108615, 8.157515323946411, 1.8905593490845518, 3.9145991706678354, 9.968052822848284, 8.990383526294597, 4.162267499095601, 0.6522048320365248, 2.9616308201653507, 6.131669423852776]
josephgreen@JosephGreen-Mugabi:~/0x02-python_async_comprehension$
