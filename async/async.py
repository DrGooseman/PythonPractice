import asyncio

async def process1():
  print('started process1')
  await asyncio.sleep(1)
  print('finished process1')

async def process2():
  print('started process2')
  await asyncio.sleep(5)
  print('finished process2')

async def process3():
  print('started process3')
  await asyncio.sleep(5)
  print('finished process3')



async def main():
    print("starting processes") 
    await asyncio.wait([process1(), process2(), process3()])
    print("all processes complete")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()


