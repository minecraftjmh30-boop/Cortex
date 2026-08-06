_c_error_handler = None
_jack_error_handler = None
_jack_info_handler = None

def linux_fix():
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