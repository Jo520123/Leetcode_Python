import math
import string
import random

Original_short = {}
Short_original = {}
l = string.ascii_letters + string.digits

class Codec:

    def encode(self, longUrl):
        """
        Encodes a URL to a shortened URL.
        :param longUrl: str
        :return: str
        """
        def short_url():
            a = ' '
            t = ' '
            for i in range(6):
                t = l[random.randint(0, 10000) % 62]
                a += t
            return a

        if longUrl in Original_short:
            return "http://tinyurl.com/" + Original_short[longUrl]

        else:
            s = short_url()
            Original_short[longUrl] = s
            Short_original[s] = longUrl
            return "http://tinyurl.com/" + s


    def decode(self, shortUrl):
        """
        Decodes a shortened URL to its original URL.
        :param shortUrl: str
        :return: str
        """
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

        shortUrl = shortUrl.split('/')[-1]
        if shortUrl in Short_original:
            return Short_original[shortUrl]
        else:
            return None
