Sublime Text 2 Drupal autocomplete plugin
=======================

This is a package manager hosted plugin for Sublime Text 2 which provides autocomplete for all Drupal functions on a per project basis. This means that you can have this plugin autocomplete your Drupal 7 project's functions and provide argument hinting as well as your Drupal 6 project with no clashes. It manages this by scanning your project's files and creating a file in your project's root directory called Drupal.sublime-projectcompletions containing Sublime Text 2's autocomplete data. The plugin then injects this into ST2's autocomplete using the API and the result should be autocomplete suggestions for all functions in your project.

This is a first attempt at providing this functionality as a plugin and my first attempt at writing code in Python. Any bugs or suggestions for improvement (ideally with a coded solution) please add comments in the issue queue.