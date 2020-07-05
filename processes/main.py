import codetiming
import concurrent.futures


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


computations = [35, 35, 35, 35]

with codetiming.Timer():
    # Single process execution
    # for computation in computations:
    #     print(fib(computation))

    # Multi process execution
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        future_to_computation = {executor.submit(fib, value): value for value in computations}
        for future in concurrent.futures.as_completed(future_to_computation):
            value = future_to_computation[future]
            try:
                data = future.result()
            except Exception as e:
                print(f'generated exception in url: {value}, error: {e}')
            else:
                print(f'for fib {value} the result is {data}')
