# Markdown Syntax Guide
Markdown is a lightweight syntax for styling forms. It is used on GitHub instead of html pages.

Specifically it is used for the README files in GitHub. The file uses the .md extension. VS Code provides editing support for these files. Note that there is an icon at the top of the edit window that opens a preview window. 

## Headers

\# are used to form headers. Examples
> \# for an \<h1> tag <br />
> \## for an \<h2> tag <br />

The number of \#'s indicates the level of the heading. A space is used after the last \# to separate the Markdown "command" from the text of the header.

## Normal Text
Just type the text. 

To get a new paragraph just add a blank line between the new paragraph and the previous one.

## Code - Syntax highlighting

Use "\```Python" on the first line to start a section of Python code. After that just type the code. Follow the last line of code with a line with \```. An illustrations is shown below

> \```Python <br />
> def hello(): <br />
> &nbsp;&nbsp;&nbsp;&nbsp;print("Hello World") <br /><br />
> hello()<br />
> \```

results in:

```Python
def hello():
    print("Hello World")

hello()    
```

## Blockquotes

Use the '\>' character to designate the text in the quote. For example:

> \> quote \<br /> <br />
> \> quote

results in:

> quote <br />
> quote

The \<br /> is used to break the line, otherwise the text will wrap.

## Some Links

https://www.markdownguide.org/basic-syntax

https://guides.github.com/features/mastering-markdown/

https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
