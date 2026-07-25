Logging
=======


The ``demoutrei.discord`` package utilizes its own custom logging handler, :class:`~discord.Logger`.

To activate logging, execute your program with the following command:

.. code:: bash

  discord <your_main_file>.py [-d|--debug]


The :class:`~discord.Logger` singleton can be imported and used at your will, if enabled. There are two ways that logs can be made:


1. Immediate log call

The log is immediately printed.

.. code:: python

  from discord import Logger


  Logger.info("Info log")
  Logger.debug("Debug log")
  Logger.warn("Warn log")

  # Output:
  #  INFO | Info log
  # DEBUG | Debug log
  #  WARN | Warn log


2. Context manager

The log prints after it exits the context manager. If an exception is caught otherwise, then the log is neglected and the exception is raised.

.. code:: python

  from discord import Logger


  with Logger.info("Did stuff"):
    print("Hello, World!")

  # Output:
  # "Hello, World!"
  #  INFO | Did stuff


  with Logger.warn("Crazy math"):
    print(1 / 0)

  # Output:
  # ERROR | ZeroDivisionError: ...


Logging Reference
-----------------

.. autoclass:: discord.Logger()