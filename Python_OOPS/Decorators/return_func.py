def is_called():
    """Here, is_returned() is a nested function which is defined and returned each time we call is_called().
    """
    def is_returned():
        print("Hello")
    return is_returned


new = is_called()

# Outputs "Hello"
new()
