import pygame


class ImageLoader:
    # Static dictionary to store loaded images by their file path
    images = {}

    @staticmethod
    def get_image(file_path):
        # Check if the image is already loaded
        if file_path in ImageLoader.images:
            return ImageLoader.images[file_path]
        else:
            # Load the image, add it to the dictionary, and return it
            image = pygame.image.load(file_path).convert_alpha()
            ImageLoader.images[file_path] = image
            return image
