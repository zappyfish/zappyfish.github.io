from yattag import Doc
import os
import yaml

HEADER_STRING = """---
layout: page
title:  Projects
subtitle: Things I have made and helped make
---

"""

def add_project(doc, tag, text, yaml_file):
  with open(yaml_file, "r") as f:
    project_info = yaml.safe_load(f)
  with tag('a', href=project_info['page_link']):
    with tag('div', id="project"):
      project_banner = os.path.join('/assets/img/banner_images/', project_info['banner_image'])
      project_examine = os.path.join('/assets/img/focus_images/', project_info['focus_image'])
      description = project_info['description']
      doc.stag('img', src=project_banner, klass="project_image")
      with tag('div', klass="examine_project"):
        doc.stag('img', src=project_examine)
        text(project_info['description'])
      text("test test test test test test teeeeeest")
  

def save_file(html_string):
  with open("projects.html", "w") as f:
    f.write(HEADER_STRING + html_string)


def main():
  doc, tag, text = Doc().tagtext()
  with tag('html'):
    with tag('head'):
      doc.stag('link', rel="stylesheet", type="text/css", href="/_projects/project_styles.css")
    with tag('body'):
      for project in os.listdir('_projects/configs/'):
        config_path = os.path.join('_projects/configs/', project)
        add_project(doc, tag, text, config_path)
  save_file(doc.getvalue())
  

if __name__ == '__main__':
  main()

