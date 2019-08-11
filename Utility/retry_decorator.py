import time
from functools import wraps


def retry(exception_to_check, tries=4, delay=3, back_off=2):
    """Retry calling the decorated function using an exponential backoff.
    :param exception_to_check: the exception to check. may be a tuple of
        exceptions to check
    :type exception_to_check: Exception or tuple
    :param tries: number of times to try (not retry) before giving up
    :type tries: int
    :param delay: initial delay between retries in seconds
    :type delay: int
    :param back_off: back_off multiplier e.g. value of 2 will double the delay
        each retry
    :type back_off: int
    """

    def deco_retry(f):

        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except exception_to_check as e:
                    msg = "%s, Retrying in %d seconds..." % (str(e), mdelay)
                    print(msg)
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= back_off
            return f(*args, **kwargs)

        return f_retry

    return deco_retry
