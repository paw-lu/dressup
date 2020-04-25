Reference
=========

.. _CLI reference:

Command-line usage
------------------

Dress up's command-line usage looks like:

.. code-block:: console

   ❯ dressup [OPTIONS] [CHARACTERS]

.. option:: -s, --strict-case

   Do not fallback to different cases.

.. option:: -r, --reverse

   Reverse the output.

.. option:: -t, --type TEXT

   The Unicode type to convert to.

.. option:: --version

   Display the version and exit.

.. option:: --help

   Display a short usage message and exit.

.. option:: --install-completion [bash|zsh|fish|powershell|pwsh]

   Install completion for the specified shell.

.. option:: ----show-completion [bash|zsh|fish|powershell|pwsh]

   Show completion for the specified shell, to copy it or customize the installation.


.. _Library reference:

dressup.converter
-----------------

.. automodule:: dressup.converter
    :members: convert, show_all
