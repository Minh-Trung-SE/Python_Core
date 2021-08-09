def is_pangram(msg, alphabet):
    return not set(alphabet) - set(msg.lower())