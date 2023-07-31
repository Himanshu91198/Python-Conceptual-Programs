import bitlyshortener

tokens = ["e3645b13c0c210fd9f60cb45461c5d715976381c"]

shortener = bitlyshortener.Shortener(tokens=tokens, max_cache_size=256)

my_urls = []
url = input("Enter your url: ")
my_urls.append(url)


x = shortener.shorten_urls(my_urls)
print(f"Your shortened url is {x}")
