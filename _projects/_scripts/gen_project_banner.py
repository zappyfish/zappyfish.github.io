from yattag import Doc


HEADER_STRING = """---
layout: page
title: :hammer: Projects :hammer:
subtitle: Things I have made and helped make
---

"""


def add_project(doc, tag, text):
  with tag('div', klass="tab-content"):
    with tag('div', id="background"):
      text('testing')


def save_file(html_string):
  with open("projects.html", "w") as f:
    f.write(HEADER_STRING + html_string)

def main():
  doc, tag, text = Doc().tagtext()
  with tag('html'):
    with tag('head'):
      doc.stag('link', rel="stylesheet", href="_projects/project_styles.css")
    with tag('body'):
      add_project(doc, tag, text)
  save_file(doc.getvalue())
  

if __name__ == '__main__':
  main()
