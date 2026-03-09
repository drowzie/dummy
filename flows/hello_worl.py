import time
from prefect import flow, task


@task
def test_dev_mem():
    try:
        with open("/dev/mem", "rb") as f:
            data = f.read(64)  # Try to read 64 bytes
            print(
                f"Successfully read from /dev/mem: {data[:10]}..."
            )  # Print first 10 bytes
    except PermissionError:
        print("Permission denied: /dev/mem access requires privileged mode.")
    except FileNotFoundError:
        print("/dev/mem not available (may be disabled by kernel).")
    except Exception as e:
        print(f"Unexpected error: {e}")


@task
def add_integers(a, b):
    return a + b


@task
def subtract_integers(a, b):
    return a - b


@flow(log_prints=True)
def buy():
    result = add_integers(1, 2)
    print(f"Buying securities {result}")
    test_dev_mem()
    time.sleep(30)
    result = subtract_integers(1, 2)


if __name__ == "__main__":
    buy()
