from yattag import Doc
import os
import yaml

HEADER_STRING = """---
layout: page
title:  Projects
subtitle: Some things I have made and helped make
---

"""

def add_project(doc, tag, text, yaml_file):
  with open(yaml_file, "r") as f:
    project_info = yaml.safe_load(f)
  with tag('tr'):
    with tag('h2', klass="title"):
      text(project_info['title'])
  with tag('tr', id="project"):
    with tag('a', href=project_info['page_link']):
      project_banner = os.path.join('/assets/img/banner_images/', project_info['banner_image'])
      project_examine = os.path.join('/assets/img/focus_images/', project_info['focus_image'])
      description = project_info['description']
      doc.stag('img', src=project_banner, klass="project_image")
      with tag('div', klass="examine_project"):
        doc.stag('img', src=project_examine, style="width:50%;")
        with tag('p', style="width:50%;"):
         text(project_info['description'])
  

def save_file(html_string):
  with open("projects.html", "w") as f:
    f.write(HEADER_STRING + html_string)


def main():
  doc, tag, text = Doc().tagtext()
  with tag('html'):
    with tag('head'):
      doc.stag('link', rel="stylesheet", type="text/css", href="/assets/css/project_styles.css")
    with tag('body'):
      with open('_projects/configs.txt', 'r') as f:
        configs = f.readlines()
      with tag('table', id="projects"):
        for project in configs:
          config_path = os.path.join('_projects/configs/', project.strip())
          add_project(doc, tag, text, config_path)
  save_file(doc.getvalue())
  

if __name__ == '__main__':
  main()

