from PIL import Image, ImageFilter


def main():
    image = Image.open(r'e:\images\wulo.jpg')
    image.filter(ImageFilter.CONTOUR).show()


if __name__ == '__main__':
    main()
