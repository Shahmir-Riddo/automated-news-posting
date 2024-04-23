from io import BytesIO
import requests
from PIL import Image

def create_post(title, image_url, date):
    response =  requsts.get(image_url)
    image = Image.open(BytesIO(response.content))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("Kollektif.ttf", 20)

#     def select_news(self):
#         pass

#     def create_post(self, title, image_image):
#         response = requests.get(image_url)
#         image = Image.open(BytesIO(response.content))
#         draw = ImageDraw.Draw(image)
#         font = ImageFont.truetype("Kollektif.ttf", 20)
#         # Calculate the size of the headline text
#         text_width, text_height = draw.textsize(headline, font=font)

#         # Calculate the position to place the headline at the bottom center
#         image_width, image_height = image.size
#         text_position = ((image_width - text_width) // 2, image_height - text_height - 20)  # Adjust the padding as needed

#         # Specify the color of the headline text (RGB format)
#         text_color = (255, 255, 255)  # White color

#         # Add the headline text to the image
#         draw.text(text_position, headline, fill=text_color, font=font)

#         # Save the modified image
#         image.save("image_with_headline.jpg")

#         # Show the modified image
#         image.show()


#     def publish(self, post):
#         pass


# quillings = Quillings()
# quillings.parse_feed()
