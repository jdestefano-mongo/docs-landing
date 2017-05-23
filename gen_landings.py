#!/usr/bin/env python3
import os.path

from sys import argv

# Build directory name will be the name of Makefile recipe
BUILD_DIR = argv[1]

# Paths of source files
MANUAL_INPUT_PATH = './manual.html'
CLOUD_INPUT_PATH = './cloud.html'
DRIVERS_INPUT_PATH = './drivers.html'
TOOLS_INPUT_PATH = './tools.html'

# Path of the output files
LANDING_OUTPUT_PATH = os.path.join(BUILD_DIR, 'landing', 'index.html')
CLOUD_OUTPUT_PATH = os.path.join(BUILD_DIR, 'cloud', 'index.html')
TOOLS_OUTPUT_PATH = os.path.join(BUILD_DIR, 'tools', 'index.html')

# Order of which all cards will show on the main landing page
RENDER_ORDER = (MANUAL_INPUT_PATH, CLOUD_INPUT_PATH,
                DRIVERS_INPUT_PATH, TOOLS_INPUT_PATH)


def build_all(template):
    """Build the main landing page for docs.mongodb.com"""
    html = ''

    # Read each file and concatenate the HTML
    fragments = []
    for f in RENDER_ORDER:
        with open(f) as in_file:
            fragments.append(in_file.read())
    html = '\n'.join(fragments)

    # Substitute the template placeholder w/ HTML
    file_contents = template.replace('{0}', html)

    # Write the output file
    with open(LANDING_OUTPUT_PATH, 'w') as out_file:
        out_file.write(file_contents)


def build_individual(template, input_path, output_path):
    """Build a landing page from a single source file
       pyfe.g., Cloud landing page, Tools..."""
    html = ''

    # Read the source file
    with open(input_path, 'r') as in_file:
        html = in_file.read()

    # Substitute the template placeholder w/ HTML
    file_contents = template.replace('{0}', html)

    # Write the output file
    with open(output_path, 'w') as out_file:
        out_file.write(file_contents)


def main():
    # Read the template
    with open('./index.html', 'r') as in_file:
        template = in_file.read()

    # Build each landing page using the template
    build_all(template)
    build_individual(template, CLOUD_INPUT_PATH, CLOUD_OUTPUT_PATH)
    build_individual(template, TOOLS_INPUT_PATH, TOOLS_OUTPUT_PATH)

if __name__ == '__main__':
    main()
