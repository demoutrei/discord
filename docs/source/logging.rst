Logging
=======

The library supports and implements its own logging module.

To enable, you must execute your code using the ``discord`` command-line command.

.. code:: bash

    $ discord path/to/file.py

.. admonition:: Debug Logs
    :class: tip

    Debug-level logs are disabled by default. To enable, append the ``-d`` or ``--debug`` flag.

    .. code:: bash

        $ discord path/to/file.py --debug


Usage
+++++

If logging is enabled, the :class:`~discord.logging.Logger` singleton class can be imported from anywhere in your codebase.

.. code:: python

    from discord import Logger

    Logger.info("Info log")

Post-Execution Logging
^^^^^^^^^^^^^^^^^^^^^^

The library's logging system supports the implementation of explicitly logging after a certain execution, or automatically raise the exception if any, through the ``with`` keyword.

.. code:: python

    from discord import Logger
    import time

    with Logger.info("Task completed"):
      time.sleep(3)
      print("Hello, World!")

    # Output:
    # "Hello, World!"
    # xxxx-xx-xx xx:xx | [ INFO] "Task Completed"

    with Logger.info("Task completed"):
      print(f"{0 / 0 = } ")

    # Output:
    # xxxx-xx-xx xx:xx | [ERROR] ZeroDivisionError...