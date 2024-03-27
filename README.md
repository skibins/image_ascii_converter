Project Documentation: Image to ASCII Art Converter
---------------------------------------------------

### Overview:

This project provides a tool to convert images into ASCII art. It utilizes the Google Images Search API for image retrieval and the ASCII Magic library for converting the images to ASCII format.

### Installation:

1.  Install the required packages:

    `pip install google-images-search`
    
    `pip install windows-curses`
    
    `pip install ascii_magic`

### Running the Program:

1.  Acquire Google Developer API Key and Custom Search Engine (CSE) ID, then use them in the code:

    -   To obtain a Google Developer API Key:
        -   Go to the [Google Developers Console](https://console.developers.google.com/).
        -   Create a new project.
        -   Enable the Custom Search API for your project.
        -   Generate an API Key.
    -   To create a Custom Search Engine:
        -   Go to the [Google Custom Search Engine](https://cse.google.com/cse/).
        -   Click on "Add" to create a new search engine.
        -   Follow the setup process and obtain the CSE ID.
        -   Remember to enable "Image search" option and for "Sites to search" option select "Search the entire web but emphasize included sites".
2.  Open a terminal or command prompt.

3.  Navigate to the directory where the script is located.

4.  Run the script:

    `python image_to_ascii.py`

5.  Follow the prompts:

    -   If you have a specific image URL you want to convert, enter 'Y' and provide the URL.
    -   If not, enter 'N' and specify the image you want to search for.
    -   For customizing the image search, enter values corresponding to the options listed (e.g., 'clipart' for image type).
    -   Once the image is selected, the program will convert it to ASCII art and save it as an HTML file.

### Usage:

1.  Start the program and follow the prompts to select an image or specify search parameters.

2.  If providing a specific image URL, ensure it is accessible and valid.

3.  If performing a search, input the desired image query and customize the search using the provided options.

4.  After conversion, locate the generated HTML file ('new_img.html') to view the ASCII art representation of the image.

### Customization Options:

-   For customizing the image search, responses to the prompts should be either left blank (press Enter) or contain values listed in the corresponding question (e.g., 'clipart' for image type).

### Troubleshooting:

-   If encountering any issues during installation or execution, ensure that the required packages are correctly installed.
-   Verify that the Google Developer API Key and Custom Search Engine ID are valid and correctly configured.

By following these instructions, users can easily install, run, and utilize the Image to ASCII Art Converter tool to convert images into ASCII art.

### Packages documentation:
- [google-images-search](https://pypi.org/project/Google-Images-Search/)
- [ascii_magic](https://pypi.org/project/ascii-magic/)
- [windows-curses](https://pypi.org/project/windows-curses/)
