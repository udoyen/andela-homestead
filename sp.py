def split(seq, n):
    """Partitions `seq` into `n` successive slices of roughly equal size.

    The sizes of each yielded slice shall differ by at most one.
    """
    q, r = divmod(len(seq), n)
    start = 0

    for i in range(n):
        size = q + (i >= (n - r))
        yield seq[start: start + size]
        start += size


print(list(split('123456789', 4)))
