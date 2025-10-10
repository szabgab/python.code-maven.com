import time
import sys

def do_task(task_id: int, sec: int):
    print(f"Start task {task_id}")
    time.sleep(sec)
    print(f"End task {task_id}")

def main():
    if len(sys.argv) != 2:
        exit(f"Usage {sys.argv[0]} NUMBER")

    for i in range(int(sys.argv[1])):
        do_task(i, 1)


start = time.monotonic()
main()
end = time.monotonic()
print(f"Elapsed time: {end-start}")
