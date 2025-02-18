import redis
import time
import sys
import os
import datetime

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_DB = int(os.getenv("REDIS_DB", "0"))
DESIRED_EXPIRE = int(os.getenv("DESIRED_EXPIRE", "60"))
DESIRED_INTERVAL = int(os.getenv("DESIRED_INTERVAL", "30"))

# see https://github.com/darkweak/storages/issues/23
KEY_PATTERN = "IDX_*"


def log(message):
    ts = datetime.datetime.now().isoformat()
    print(f"{ts} {message}", file=sys.stderr)


def main():
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
    while True:
        count = 0
        for key in r.scan_iter(KEY_PATTERN):
            if r.ttl(key) < 0:
                r.expire(key, DESIRED_EXPIRE)
                count += 1
        if count > 0:
            log(f"set expiration for {count} mapping keys to {DESIRED_EXPIRE}")
        time.sleep(DESIRED_INTERVAL)


if __name__ == "__main__":
    log(f"REDIS_HOST={REDIS_HOST}")
    log(f"REDIS_PORT={REDIS_PORT}")
    log(f"REDIS_DB={REDIS_DB}")
    log(f"DESIRED_EXPIRE={DESIRED_EXPIRE}")
    log(f"DESIRED_INTERVAL={DESIRED_INTERVAL}")
    main()
