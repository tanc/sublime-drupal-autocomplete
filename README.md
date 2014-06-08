Sublime Text Drupal autocomplete plugin
=======================

This is a package manager hosted plugin for Sublime Text (2 and 3) which provides autocomplete for all Drupal functions on a per project basis. This means that you can have this plugin autocomplete your Drupal 7 project's functions and provide argument hinting as well as your Drupal 6 project with no clashes. It manages this by scanning your project's files and creating a file in your project's root directory called Drupal.sublime-projectcompletions containing Sublime Text's autocomplete data. The plugin then injects this into ST's autocomplete popup using the API and the result should be autocomplete suggestions for all functions in your project.

This functionality might also be acheived using the ctags or SublimeCodeIntel packages, but this package is a Drupal centric package and works out of the box.

## Requirements

For this plugin to provide autocompletions for your Drupal project you must have a Sublime Text project file saved in the root of the Drupal project.

To do this open your Drupal files (drag and drop the whole directory onto Sublime Text) and then save a new project by using the Project menu item. Make sure you save it in the Drupal root (where the index.php and CHANGELOG.txt files are) and call it whatever you want.

## How to install

The easiest way to install is through the [Sublime Package Control](http://wbond.net/sublime_packages/package_control) repository (currently awaiting approval).

If you've come to the github page and are looking to install this manually you'll want to fetch the master branch and rename the resulting directory DPCompletions. Move this directory into your ST packages directory (on OS X its located in ~/Library/Application Support/Sublime Text 2/Packages/) and it should automatically get picked up as a new plugin. You may need to restart Sublime Text.

## How it works

The plugin scans upwards from the currently saved file, looking for the ST project file. It uses this to determine the root directory of the project and from here is loads all files (.module, .inc etc) and looks for functions within them. It builds a projectcompletions file (basically a big json array) containing the function name and any expected parameters. Note that it does this on every file save.

It then uses the ST API to inject these possible completions as you start typing a function name. The tab stop should allow you to easy to the different arguments expected by the function.

## Notes

If you are using a VCS you will want to exclude this plugin's autocompletions file. If you are using git you can add something like the following line to your gitignore file:

*.sublime-projectcompletions

Theoretically it would be possible to save the ST project files anywhere within the Drupal project which could allow for subprojects if that is how you use ST with Drupal. For instance, you might have a single Drupal root with many multisites under sites/ and have a different ST project for each one. This plugin will still work but will not provide autocomplete for any functions above the ST project in the filesystem.

This is a first attempt at providing this functionality as a plugin and my first attempt at writing code in Python. Any bugs or suggestions for improvement (ideally with a coded solution) please add comments in the issue queue.
