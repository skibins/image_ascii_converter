from google_images_search import GoogleImagesSearch
from ascii_magic import AsciiArt


def validate_value(value):
    """
    Validates if a value is provided. If not, it exits the program.

    Parameters:
        value (str): The value to be validated.

    Returns:
        None
    """
    if not value:
        print('No value provided. Exiting.')
        exit()


class ImageConverter:
    """
    Class to convert images to ASCII art using Google Images and ASCII Magic libraries.
    """

    def __init__(self, api_key, cx):
        """
        Initializes ImageConverter object.

        Parameters:
            api_key (str): Your Google developer API key.
            cx (str): Your Google Custom Search Engine (CSE) ID.
        """
        self.image_url = None
        self.gis = GoogleImagesSearch(api_key, cx)
        # Parameters for Google Images search
        self._search_params = {
            'num': 1,
            'fileType': 'jpg|png',
            'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived',
        }
        # Questions to customize the image search
        self.questions = {
            'Image security(active|high|medium|off|safeUndefined): ': 'imgSafe',
            'Image type(clipart|face|lineart|stock|photo|animated|imgTypeUndefined): ': 'imgType',
            'Image size(huge|icon|large|medium|small|xlarge|xxlarge|imgSizeUndefined): ': 'imgSize',
            'Image dominant color(black|blue|brown|gray|green|orange|pink|purple|red|teal|white|yellow|imgDominantColorUndefined): ': 'imgDomColor',
            'Image color type(color|gray|mono|trans|imgColorTypeUndefined): ': 'imgColorType'
        }

    def get_img_params(self):
        """
        Prompts the user to input parameters for image search.
        """
        have_own_url = input('Do you have your specific image URL that you want to convert to ascii?(Y/n) ')

        if have_own_url.lower() == 'y':
            self.image_url = input('Provide URL address: ')
            validate_value(self.image_url)
        else:
            query = input('What image do you want to search for? ')
            validate_value(query)

            self._search_params['q'] = query

            print('==========')
            print("""If you want these options to be set by default, just press 'enter'.""")
            print('==========')

            # Prompt user for custom search parameters
            for question, key in self.questions.items():
                answer = input(question)
                if answer:
                    self._search_params[key] = answer

            print('LOOKING FOR ' + query.upper())

            # Perform Google Images search
            self.gis.search(search_params=self._search_params)
            for image in self.gis.results():
                print('Your image url: ' + image.url)
                self.image_url = image.url

    def convert_image(self):
        """
        Converts image to ASCII art and saves it as an HTML file.
        """
        print('CONVERTING IMAGE TO ASCII')

        try:
            img_to_ascii = AsciiArt.from_url(self.image_url)
        except OSError as e:
            print(f'Could not load the image, server said: {e.code} {e.msg}')
            exit()

        # Convert image to ASCII and save as HTML file
        img_to_ascii.to_html_file("new_img.html", columns=220, width_ratio=2)
        print("Your image can be found at 'new_img.html' file.")


# Your Google developer API key and Custom Search Engine ID
api_key = 'your_dev_api_key'
cx = 'your_project_cx'

# Create ImageConverter object and perform image conversion
converter = ImageConverter(api_key, cx)
converter.get_img_params()
converter.convert_image()
