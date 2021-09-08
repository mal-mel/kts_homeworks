import asyncio
import functools
import logging


def watchdog(afunc, stop: bool = False):
    @functools.wraps(afunc)
    async def _watchdog(*args, **kwargs):
        try:
            await afunc(*args, **kwargs)
        except asyncio.CancelledError:
            logging.info(f"task {afunc.__name__} cancelled")
            return
        except Exception as e:
            logging.exception(e)
            if stop:
                asyncio.get_event_loop().stop()
    return _watchdog
