# Chris Aung
# Midterm - Create Webpage
# October 19, 2023

import os

def read_template(filename):
    with open(filename, 'r') as f:
        return ''.join(f.readlines())

def main():
    # User Input
    file_name = input("Enter the filename: ")
    out_file = file_name + ".html"
    
    body_h1 = input("Enter the character name: ")
    body_h1 = f"<h1>{body_h1}</h1>\n"
    
    body_h2 = input("Enter the actor's name: ")
    body_h2 = f"<h2>Played by {body_h2}</h2>\n"
    
    body_description = input("Enter a description: ")
    body_description = f"<p>{body_description}</p>\n"
    
    body_img = input("Enter the image location: ")
    body_img = f'<img src="{body_img}" alt="{file_name}">\n'
    
    # Extra Credit: Quote and YouTube Link
    body_quote = input("Enter a character quote: ")
    body_quote = f'<blockquote>{body_quote}</blockquote>\n'
    
    body_youtube = input("Enter the YouTube embed link: ")
    body_youtube = f'<iframe width="560" height="315" src="{body_youtube}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n'

    
    # Combined_body with extra credit additions
    combined_body = body_h1 + body_h2 + body_description + body_img + body_quote + body_youtube
    
    # Templates
    page_head = read_template("assets/page-head.txt")
    page_footer = read_template("assets/page-footer.txt")
    
    # Combined Page
    combined_page = page_head + combined_body + page_footer
    
    # HTML File
    with open(out_file, "w") as f:
        f.write(combined_page)
    
    print(f"Created {out_file}")

if __name__ == "__main__":
    main()
