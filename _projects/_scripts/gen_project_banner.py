from yattag import Doc
import yaml

HEADER_STRING = """---
layout: page
title:  Projects
subtitle: Things I have made and helped make
---

"""

def add_yaml_to_project(doc, tag, text, yaml_file):
  with open(yaml_file, "r") as f:
    project_info = yaml.safe_load(f)
  doc.stag('img', src=project_info['banner_image'], klass="project_image")
  with tag('div', klass="examine_project"):
    doc.stag('img', src=project_info['focus_image'])
    txt(project_info['description'])

def add_project(doc, tag, text):
  with tag('div', klass="tab-content"):
    with tag('div', id="project"):
      add_yaml_to_project(doc, tag, text, "_projects/_project.yaml")


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

