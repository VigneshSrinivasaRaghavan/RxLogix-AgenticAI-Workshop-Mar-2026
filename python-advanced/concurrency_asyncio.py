import time
import asyncio

# Part 1 - Synchronous (slow - runs one by one)

def sync_check_login():
    time.sleep(2)
    return "Login API: OK"

def sync_check_dashboard():
    time.sleep(2)
    return "Dashboard API: OK"

def sync_check_report():
    time.sleep(2)
    return "Report API: OK"

def run_sync():
    print("=== SYNC (Sequential) ===")
    start = time.time()

    print(sync_check_login())
    print(sync_check_dashboard())
    print(sync_check_report())

    print(f"Total time: {time.time() - start:.2f} seconds\n")


# Part 2 - Asynchronous (fast - runs in parallel)

async def async_check_login():
    await asyncio.sleep(2)
    return "Login API: OK"

async def run_async_single():
    print("=== ASYNC (Single function) ===")
    start = time.time()

    result = await async_check_login()
    print(result)

    print(f"Total time: {time.time() - start:.2f} seconds\n")



#  PART 3: asyncio.gather (all at once - fast)

async def async_check_dashboard():
    await asyncio.sleep(2)
    return "Dashboard API: OK"

async def async_check_report():
    await asyncio.sleep(2)
    return "Report API: OK"

async def run_async_parallel():
    print("=== ASYNC (Parallel with gather) ===")
    start = time.time()

    results = await asyncio.gather(
        async_check_login(),
        async_check_dashboard(),
        async_check_report(),
    )

    for result in results:
        print(result)

    print(f"Total time: {time.time() - start:.2f} seconds\n")


async def main():
    run_sync()
    await run_async_parallel()
    await run_async_single()

asyncio.run(main())