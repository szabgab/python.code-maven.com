import time
import sys
import asyncio

async def do_task(task_id: int, sec: int):
    print(f"Start {task_id}")
    await asyncio.sleep(sec)
    print(f"End {task_id}")

async def main():
    print("Main started")
    if len(sys.argv) != 2:
        exit(f"Usage {sys.argv[0]} NUMBER")

    co_routines = []
    for i in range(int(sys.argv[1])):
        co_routines.append(do_task(i, 1))

    print("Tasks created")

    for t in co_routines:
        await t

    print("Main ended")

start = time.monotonic()
asyncio.run(main())
end = time.monotonic()
print(f"Elapsed {end-start}")
