# Create-Webpage Project by Chris Aung

## Description

This is a Python program that generates a webpage based on user input. You can provide details such as the character name, actor's name, description, image location, a quote, and a YouTube embed link.

---

## Table of Contents

- [Create-Webpage Project by Chris Aung](#create-webpage-project-by-chris-aung)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Files](#files)
  - [How to Use](#how-to-use)
  - [User Inputs](#user-inputs)
  - [Technical Details](#technical-details)
  - [HTML Templates](#html-templates)
  - [CSS](#css)
  - [Extra Credit Features](#extra-credit-features)
  - [Requirements](#requirements)
  - [Execution](#execution)
  - [Contact](#contact)

---

## Required Files

- `create-webpage.py`: Main Python script where the program logic resides.
- `assets/page-head.txt`: Text file containing the top half of the HTML template (up to opening `<body>` tag).
- `assets/page-footer.txt`: Text file containing the bottom half of the HTML template (closing `</body>` and `</html>` tags).
- `assets/styles.css`: CSS file containing styling rules.

---

## How to Use

1. Run `create-webpage.py`.
2. Input file name for the HTML page to be generated.
3. Input details as prompted.
4. A new HTML file will be generated in the current directory.

---

### User Inputs/ Expectations

- **Filename**: Base name for the output HTML file.
- **Character Name**: Displayed as `<h1>` on the webpage.
- **Actor's Name**: Displayed as `<h2>` on the webpage.
- **Description**: Displayed as a paragraph `<p>` on the webpage.
- **Image Location**: Used in `<img>` tag for image.
- **Character Quote**: Displayed as `<blockquote>` on the webpage.
- **YouTube Embed Link**: Embedded as an `<iframe>`.

---

### HTML Templates

There are two text files, `assets/page-head.txt` and `assets/page-footer.txt`, which are the top and bottom half of the HTML templates. The Python script reads these text files and combines them with the user input to generate the complete webpage.

### CSS

CSS styling is located in `assets/styles.css`. It contains rules for body text, headers, images, and is responsive to screen size changes.

---

## Extra Credit Features

- Included a quote section, displayed as `<blockquote>`.
- Included a YouTube video, embedded as an `<iframe>`.

---

## Software Requirements

- Python 3.x
- Text editor

---

## Execution

To execute the program, navigate to the directory where `create-webpage.py` is located and run `python create-webpage.py`.

---

## Contact

For any further questions or issues, please contact Chris Aung.