# Standard argument
def standard_arg(arg):
    print(arg)


standard_arg(2)
standard_arg(arg=2)


# Keyword only argument
def kwd_only_arg(*, arg):
    print(arg)


kwd_only_arg(arg=3)


# Combined arguments
# Noted that current use of Python (version 3.6.9) haven't support positional argument yet
def combined_example(standard, *, kwd_only):
    print(standard, kwd_only)


combined_example(2, kwd_only=3)
combined_example(standard=2, kwd_only=3)
