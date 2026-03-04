import time
from prefect import flow, task


@task
def add_integers(a, b):
    return a + b


@flow(log_prints=True)
def buy():
    result = add_integers(1, 2)
    print(f"Buying securities {result}")
    time.sleep(30)


if __name__ == "__main__":
    buy.from_source(
        "https://github.com/drowzie/dummy.git", entrypoint="flows/hello_worl.py:buy"
    ).deploy(
        name="my-code-baked-into-an-image-deployment",
        work_pool_name="generic-bob",
        build=False,
        job_variables={"nodeSelector": {"hardware": "gene"}},
    )
