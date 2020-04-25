Dress up
========

.. toctree::
   :caption: Contents
   :maxdepth: 2

   reference
   CONTRIBUTING
   Code of Conduct <CODE_OF_CONDUCT>
   license
   Changelog <https://github.com/pscosta5/dressup/releases>

Installation
------------

To install Dress up,
run this command in your terminal:

.. code-block:: console

   ❯ pip install dressup

If you're using it primarily as a command-line tool,
it's recommended you install it via `pipx <https://github.com/pipxproject/pipx>`_.

.. code-block:: console

   ❯ pipx install dressup

Command-line usage
------------------

Display all possible transformations by running:

.. code-block:: console

   ❯ dressup Hello
   Circle

   Ⓗⓔⓛⓛⓞ

   Negative circle

   🅗🅔🅛🅛🅞

   Monospace

   Ｈｅｌｌｏ

   Math bold

   𝐇𝐞𝐥𝐥𝐨

   ...

Return only a specific transformation by using the ``--type`` flag.

.. code-block:: console

   ❯ dressup Goodbye --type inverted
   ƃoopqʎǝ

See more options in the :ref:`CLI reference`, or by running

.. code-block:: console

   ❯ dressup --help

Autocompletion
--------------

Dress up supports argument completions along with live previews.
To enable autocompletion run.

.. code-block:: console

   ❯ dressup --install-completion zsh
   zsh completion installed in /Users/username/.zshrc.
   Completion will take effect once you restart the terminal.

``zsh`` may be replaced with ``bash``, ``fish``, ``powershell``, or ``pwsh``.
Along with typical autocompletion, when typing in a value for ``--type``
if ``[TAB]`` is pressed the matching parameter values will be displayed below along with a preview of the conversion.

.. code-block:: console

   ❯ dressup Words --type math [TAB]
   math-bold              -- 𝐖𝐨𝐫𝐝𝐬
   math-bold-fraktur      -- 𝖂𝖔𝖗𝖉𝖘
   math-bold-italic       -- 𝑾𝒐𝒓𝒅𝒔
   math-bold-script       -- 𝓦𝓸𝓻𝓭𝓼
   math-double-struck     -- 𝕎𝕠𝕣𝕕𝕤
   math-fraktur           -- 𝔚𝔬𝔯𝔡𝔰
   math-monospace         -- 𝚆𝚘𝚛𝚍𝚜
   math-sans              -- 𝖶𝗈𝗋𝖽𝗌
   math-sans-bold         -- 𝗪𝗼𝗿𝗱𝘀
   math-sans-bold-italic  -- 𝙒𝙤𝙧𝙙𝙨
   math-sans-italic       -- 𝘞𝘰𝘳𝘥𝘴

Library usage
-------------

Dress up can also be used as a Python library.

To convert characters, use ``convert``.

.. code-block:: python

   import dressup


   dressup.convert("Hello", unicode_type="negative circle")

.. code-block:: console

   '🅗🅔🅛🅛🅞'

To return all possible conversions, use ``show_all``.

.. code-block:: python

   import dressup


   dressup.show_all("Hello")

.. code-block:: console

   {'Circle': 'Ⓗⓔⓛⓛⓞ', 'Negative circle': '🅗🅔🅛🅛🅞',
   'Monospace': 'Ｈｅｌｌｏ', 'Math bold': '𝐇𝐞𝐥𝐥𝐨',
   'Math bold fraktur': '𝕳𝖊𝖑𝖑𝖔', 'Math bold italic': '𝑯𝒆𝒍𝒍𝒐',
   'Math bold script': '𝓗𝓮𝓵𝓵𝓸', 'Math double struck': 'ℍ𝕖𝕝𝕝𝕠',
   'Math monospace': '𝙷𝚎𝚕𝚕𝚘', 'Math sans': '𝖧𝖾𝗅𝗅𝗈', 'Math sans bold':
   '𝗛𝗲𝗹𝗹𝗼', 'Math sans bold italic': '𝙃𝙚𝙡𝙡𝙤', 'Math sans italic':
   '𝘏𝘦𝘭𝘭𝘰', 'Parenthesized': '⒣⒠⒧⒧⒪', 'Square': '🄷🄴🄻🄻🄾',
   'Negative square': '🅷🅴🅻🅻🅾', 'Cute': 'Héĺĺő', 'Math fraktur':
   'ℌ𝔢𝔩𝔩𝔬', 'Rock dots': 'Ḧëḷḷö', 'Small caps': 'ʜᴇʟʟᴏ', 'Stroked':
   'Ħɇłłø', 'Subscript': 'ₕₑₗₗₒ', 'Superscript': 'ᴴᵉˡˡᵒ',
   'Inverted': 'ɥǝןןo', 'Reversed': 'Hɘ⅃⅃o'}

See :ref:`Library reference` for more arguments and examples.

Prior art
---------

Pseudomappings were inspired by `Unicode Text Converter <https://qaz.wtf/u/convert.cgi>`_.

Index
~~~~~
:ref:`genindex`
