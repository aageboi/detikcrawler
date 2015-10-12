from BeautifulSoup import BeautifulSoup
import requests as req


def image_url(u):
    if u[0:7] == '/images':
        return url + u
    elif u[0:7] == 'images/':
        return url + '/' + u
    elif u[0:2] == '//':
        return 'http:' + u
    else:
        return u


def get_image_size(i):
    r = req.get(i)
    return r.headers['Content-Length']

url = "http://www.detik.com"

page = req.get(url)
soup = BeautifulSoup(page.content)

img = soup.findAll('img')

# Remove duplicate image
# tmpimg = []
# for image in img:
#     if image['src'] and image['src'] not in tmpimg:
#         tmpimg.append(image['src'])

# Total image after removed duplicate images
# print "Total Image: %d " % len(tmpimg)

print "Total Image: %d " % len(img)


total_size = 0;
for i in img:
    if i['src']:
        images = image_url(i['src'])
        try:
            size = get_image_size(images)
            total_size += int(size)
        except:
            print "Error get headers from: " + images


print "Total Images size: %d" % total_size

