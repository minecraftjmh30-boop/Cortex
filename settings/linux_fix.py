_c_error_handler = None
_jack_error_handler = None
_jack_info_handler = None

def linux_fix():
    import os
    import time
    # Ensure TZ is set for Linux environments where timezone detection might fail (e.g. Raspberry Pi)
    # python-kasa uses zoneinfo which requires IANA names (e.g. 'Etc/UTC') rather than POSIX strings.
    if 'TZ' not in os.environ:
        os.environ['TZ'] = 'Etc/UTC'
        if hasattr(time, 'tzset'):
            time.tzset()
    else:
        # Check if TZ is a POSIX string (often contains digits like 'EST5EDT')
        import re
        if re.search(r'\d', os.environ['TZ']):
             os.environ['TZ'] = 'Etc/UTC'
             if hasattr(time, 'tzset'):
                 time.tzset()

    # this should suppress ALSA lib errors
    import ctypes

    global _c_error_handler
    ERROR_HANDLER_FUNC = ctypes.CFUNCTYPE(None, ctypes.c_char_p, ctypes.c_int,
                                          ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p)

    def py_error_handler(filename, line, function, err, fmt):
        pass

    _c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

    try:
        asound = ctypes.cdll.LoadLibrary('libasound.so.2')
        asound.snd_lib_error_set_handler(_c_error_handler)
    except OSError:
        pass

    # Suppress JACK errors
    global _jack_error_handler, _jack_info_handler
    JACK_HANDLER_FUNC = ctypes.CFUNCTYPE(None, ctypes.c_char_p)

    def py_jack_handler(msg):
        pass

    _jack_error_handler = JACK_HANDLER_FUNC(py_jack_handler)
    _jack_info_handler = JACK_HANDLER_FUNC(py_jack_handler)

    for libname in ['libjack.so.0', 'libjack.so.1']:
        try:
            jack = ctypes.cdll.LoadLibrary(libname)
            jack.jack_set_error_function(_jack_error_handler)
            jack.jack_set_info_function(_jack_info_handler)
            break
        except (OSError, AttributeError):
            continue