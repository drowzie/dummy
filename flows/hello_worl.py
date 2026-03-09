import time
from prefect import flow, task


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
    time.sleep(30)
    result = subtract_integers(1, 2)


if __name__ == "__main__":
    buy()
