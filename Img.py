import base64


def convert_image():
    # Picture ==> base64 encode
    with open('imgs/30000001.jpg', 'rb') as fin:
        image_data = fin.read()
        base64_data = base64.b64encode(image_data)
        print base64_data

        fout = open('data/base64_content.txt', 'w')
        fout.write(base64_data.decode())
        fout.close()

        # base64 encode ==> Picture
    with open('data/base64_content.txt', 'r') as fin:
        base64_data = fin.read()
        ori_image_data = base64.b64decode(base64_data)

        fout = open('imgs/30000001_2.jpg', 'wb')
        fout.write(ori_image_data)
        fout.close()


if __name__ == '__main__':
    convert_image()
