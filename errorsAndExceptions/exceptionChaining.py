# Chaining RuntimeError to IOError
try:
    raise IOError
except IOError as exc:
    raise RuntimeError('Failed to open something... IDK') from exc
