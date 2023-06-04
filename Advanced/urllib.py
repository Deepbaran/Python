# https://realpython.com/urllib-request/#understanding-what-an-http-message-is

from urllib.request import urlopen, Request
from urllib.parse import urlencode
from urllib.error import HTTPError, URLError
import json
from pprint import pprint

"""
Basic HTTP GET Requests With urllib.request:
"""

with urlopen("https://www.example.com") as res:
    body = res.read()
    print(body[:15]) # b'<!doctype html>'

url = "https://jsonplaceholder.typicode.com/todos/1"
with urlopen(url) as res:
    body = res.read()
    todo_item = json.loads(body)
    print(todo_item) # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}

#################################################################################################

"""
The Nuts and Bolts of HTTP Messages:
"""
"""
* Understanding What an HTTP Message Is

HTTP message can be understood as text, transmitted as a stream of bytes, structured to follow the guidelines specified by RFC 7230. A decoded HTTP message can be as simple as two lines:

/////////////////
GET / HTTP/1.1
Host: www.google.com
////////////////

This specifies a GET request at the root (/) using the HTTP/1.1 protocol. The one and only header required is the host, www.google.com. The target server has enough information to make a response with this information.

A response is similar in structure to a request. HTTP messages have two main parts, the metadata and the body. In the request example above, the message is all metadata with no body. The response, on the other hand, does have two parts:

////////////////
HTTP/1.1 200 OK
Content-Type: text/html; charset=ISO-8859-1
Server: gws
(... other headers ...)

<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage"
...
////////////////

The response starts with a status line that specifies the HTTP protocol HTTP/1.1 and the status 200 OK. After the status line, you get many key-value pairs, such as Server: gws, representing all the response headers. This is the metadata of the response.


After the metadata, there's a blank line, which serves as the divider between the headers and the body. Everything that follows the blank line makes up the body. This is the part that gets read when you're using urllib.request.

Note: Blank lines are often technically referred to as newlines. A newline in an HTTP message has to be a Windows-style carriage return (\r) together with a line ending (\n). On Unix-like systems, newlines are typically just a line ending (\n).

You can assume that all HTTP messages follow these specifications, but it's possible that some may break these rules or follow an older specification. It's exceptionally rare for this to cause any issues, though. So, just keep it in the back of your mind in case you run into a strange bug!
"""

"""
* Understanding How urllib.request Represents an HTTP Message

The main representation of an HTTP message that you'll be interacting with when using urllib.request is the HTTPResponse object. The urllib.request module itself depends on the low-level http module, which you don't need to interact with directly. You do end up using some of the data structures that http provides, though, such as HTTPResponse and HTTPMessage.

When you make a request with urllib.request.urlopen(), you get an HTTPResponse object in return. The HTTPResponse object provides many different methods and properties.

But you'll only end up using a handful of these. Apart from .read(), the important ones usually involve getting information about the headers.

One way to inspect all the headers is to access the .headers attribute of the HTTPResponse object. This will return an HTTPMessage object. Conveniently, you can treat an HTTPMessage like a dictionary by calling .items() on it to get all the headers as tuples.

There are convenience methods to get the headers from an HTTPResponse object because it's quite a common operation. You can call .getheaders() directly on the HTTPResponse object, which will return exactly the same list of tuples as above. If you're only interested in one header, say the Server header, then you can use the singular .getheader("Server") on HTTPResponse or use the square bracket ([]) syntax on .headers from HTTPMessage.
"""
with urlopen("https://www.example.com") as response:
    pprint(dir(response))
    print(response.headers) # <http.client.HTTPMessage object at 0x000001E029D9F4F0>
    pprint(response.headers.items())
    print(response.getheader("Server")) # 'ECS (nyb/1D16)'
    print(response.headers["Server"]) # 'ECS (nyb/1D16)'

"""
* Closing an HTTPResponse

The HTTPResponse object has a lot in common with the file object. The HTTPResponse class inherits from the IOBase class, as do file objects, which means that you have to be mindful of opening and closing.

In simple programs, you’re not likely to notice any issues if you forget to close HTTPResponse objects. For more complex projects, though, this can significantly slow execution and cause bugs that are difficult to pinpoint.

Problems arise because input/output (I/O) streams are limited. Each HTTPResponse requires a stream to be kept clear while it’s being read. If you never close your streams, this will eventually prevent any other stream from being opened, and it might interfere with other programs or even your operating system.

So, make sure you close your HTTPResponse objects! For your convenience, you can use a context manager.

You can also achieve the same result by explicitly calling .close() on the response object.
"""
response = urlopen("https://www.example.com")
body = response.read()
response.close()

# The above example still has an issue, though, because an exception may be raised before the call to .close(), preventing the proper teardown. To make this call unconditional, as it should be, you can use a try … except block with both an else and a finally clause:

response = None
try:
    response = urlopen("https://www.example.com")
except Exception as e:
    print(e)
else:
    body = response.read()
finally:
    if response is not None:
        response.close()


# To read first and second 50 bytes of the response separately: 

with urlopen("https://www.example.com") as response:
    res.read(50) # b'<!doctype html>\n<html>\n<head>\n    <title>Example D'
    res.read(50) # b'omain</title>\n\n    <meta charset="utf-8" />\n    <m'

# The HTTPResponse object will close once you exit the with block scope, meaning that the .read() method will only return empty bytes objects:
with urlopen("https://www.example.com") as response:
    response.read(50) # b'<!doctype html>\n<html>\n<head>\n    <title>Example D'
response.read(50) # b''

#Another point to note is that you can’t reread a response once you’ve read all the way to the end. You’d have to make the request again.
with urlopen("https://www.example.com") as response:
    first_read = response.read()
    second_read = response.read()
print(len(first_read)) # 1256
print(len(second_read)) # 0

# In this regard, the response is different from a file object, because with a file object, you can read it multiple times by using the .seek() method, which HTTPResponse doesn’t support. Even after closing a response, you can still access the headers and other metadata, though.

"""
* Exploring Text, Octets, and Bits

In most of the examples so far, you read the response body from HTTPResponse, displayed the resulting data immediately, and noted that it was displayed as a bytes object. This is because text information in computers isn’t stored or transmitted as letters, but as bytes!

A raw HTTP message sent over the wire is broken up into a sequence of bytes, sometimes referred to as octets. Bytes are 8-bit chunks. For example, 01010101 is a byte.

So how do you represent letters with bytes? A byte has 256 potential combinations, and you can assign a letter to each combination. You can assign 00000001 to A, 00000010 to B, and so on. ASCII character encoding, which is quite common, uses this type of system to encode 128 characters, which is enough for a language like English. This is particularly convenient because just one byte can represent all the characters, with space to spare.

All the standard English characters, including capitals, punctuation, and numerals, fit within ASCII. On the other hand, Japanese is thought to have around fifty thousand logographic characters, so 128 characters won’t cut it! Even the 256 characters that are theoretically available within one byte wouldn’t be nearly enough for Japanese. So, to accomodate all the world’s languages there are many different systems to encode characters.

Even though there are many systems, one thing you can rely on is the fact that they’ll always be broken up into bytes. Most servers, if they can’t resolve the MIME type and character encoding, default to application/octet-stream, which literally means a stream of bytes. Then whoever receives the message can work out the character encoding.
"""

"""
* Dealing With Character Encodings

Problems often arise because, as you may have guessed, there are many, many different potential character encodings. The dominant character encoding today is UTF-8, which is an implementation of Unicode. Luckily, ninety-eight percent of web pages today are encoded in UTF-8!

UTF-8 is dominant because it can efficiently handle a mind-boggling number of characters. It handles all the 1,112,064 potential characters defined by Unicode, encompassing Chinese, Japanese, Arabic (with right-to-left scripts), Russian, and many more character sets, including emojis!

UTF-8 remains efficient because it uses a variable number of bytes to encode characters, which means that for many characters, it only requires one byte, while for others it can require up to four bytes.

While UTF-8 is dominant, and you usually won’t go wrong with assuming UTF-8 encodings, you’ll still run into different encodings all the time. The good news is that you don’t need to be an expert on encodings to handle them when using urllib.request.
"""

"""
* Going From Bytes to Strings

When you use urllib.request.urlopen(), the body of the response is a bytes object. The first thing you may want to do is to convert the bytes object to a string. To do this, you need to decode the bytes. To decode the bytes with Python, all you need to find out is the character encoding used. Encoding, especially when referring to character encoding, is often referred to as a character set.

As mentioned, ninety-eight percent of the time, you’ll probably be safe defaulting to UTF-8:
"""
with urlopen("https://www.example.com") as response:
    body = response.read()
decoded_body = body.decode("utf-8")
print(decoded_body[:30])
# <!doctype html>
# <html>
# <head>

# Headers are a great place to get character set information:
with urlopen("https://www.example.com") as response:
    body = response.read()
character_set = response.headers.get_content_charset()
print(character_set) # 'utf-8'
decoded_body = body.decode(character_set)
print(decoded_body[:30])
# <!doctype html>
# <html>
# <head>

"""
* Going From Bytes to File

If you want to write the body of a response into a file, you have two options:
1. Write the bytes directly to the file
2. Decode the bytes into a Python string, and then encode the string back into a file

The first method is the most straightforward, but the second method allows you to change the encoding if you want to.
"""
# To write the bytes directly to a file without having to decode, you’ll need the built-in open() function, and you’ll need to ensure that you use write binary mode:
with urlopen("https://www.example.com") as response:
    body = response.read()
with open("example.html", mode="wb") as html_file:
    html_file.write(body) # 1256
# Using open() in wb mode bypasses the need to decode or encode and dumps the bytes of the HTTP message body into the example.html file. The number that’s output after the writing operation indicates the number of bytes that have been written.

# Now say you have a URL that doesn’t use UTF-8, but you want to write the contents to a file with UTF-8. For this, you’d first decode the bytes into a string and then encode the string into a file, specifying the character encoding.
with urlopen("https://www.google.com") as response:
    body = response.read()
character_set = response.headers.get_content_charset()
print(character_set) # 'ISO-8859-1'
content = body.decode(character_set)
with open("google.html", encoding="utf-8", mode="w") as file:
    file.write(content) # 14066

# If there are encoding errors and you’re using Python to read a file, then you’ll likely get an error:
# with open("encoding-error.html", mode="r", encoding="utf-8") as file:
#     lines = file.readlines()
# # UnicodeDecodeError:
# #     'utf-8' codec can't decode byte
# # Python explicitly stops the process and raises an exception, but in a program that displays text, such as the browser where you’re viewing this page, you may find the infamous replacement characters
# # The black rhombus with a white question mark (�), the square (□), and the rectangle (▯) are often used as replacements for characters which couldn’t be decoded.

"""
* Going From Bytes to Dictionary
"""
# For application/json responses, you’ll often find that they don’t include any encoding information:
with urlopen("https://httpbin.org/json") as response:
    body = response.read()
character_set = response.headers.get_content_charset()
print(character_set) # None

# The default encoding of UTF-8 is an absolute requirement of the application/json specification. That’s not to say that every single server plays by the rules, but generally, you can assume that if JSON is being transmitted, it’ll almost always be encoded using UTF-8.

# Fortunately, json.loads() decodes byte objects under the hood and even has some leeway in terms of different encodings that it can deal with. So, json.loads() should be able to cope with most bytes objects that you throw at it, as long as they’re valid JSON:
print(json.loads(body))
# {'slideshow': {'author': 'Yours Truly', 'date': 'date of publication', 'slides'
# : [{'title': 'Wake up to WonderWidgets!', 'type': 'all'}, {'items': ['Why <em>W
# onderWidgets</em> are great', 'Who <em>buys</em> WonderWidgets'], 'title': 'Ove
# rview', 'type': 'all'}], 'title': 'Sample Slide Show'}}

# As you can see, the json module handles the decoding automatically and produces a Python dictionary. Almost all APIs return key-value information as JSON, although you might run into some older APIs that work with XML.

#################################################################################################

"""
Common urllib.request Troubles:
"""
"""
* Implementing Error Handling

Before you turn your attention to specific errors, boosting your code’s ability to gracefully deal with assorted errors will pay off. Web development is plagued with errors, and you can invest a lot of time in handling errors sensibly. Here, you’ll learn to handle HTTP, URL, and timeout errors when using urllib.request.

HTTP status codes accompany every response in the status line. If you can read a status code in the response, then the request reached its target. While this is good, you can only consider the request a complete success if the response code starts with a 2. For example, 200 and 201 represent successful requests. If the status code is 404 or 500, for example, something went wrong, and urllib.request will raise an HTTPError.

Sometimes mistakes happen, and the URL provided isn’t correct, or a connection can’t be made for another reason. In these cases, urllib.request will raise a URLError.

Finally, sometimes servers just don’t respond. Maybe your network connection is slow, the server is down, or the server is programmed to ignore specific requests. To deal with this, you can pass a timeout argument to urlopen() to raise a TimeoutError after a certain amount of time.

The first step in handling these exceptions is to catch them. You can catch errors produced within urlopen() with a try … except block, making use of the HTTPError, URLError, and TimeoutError classes:

The function make_request() takes a URL string as an argument, tries to get a response from that URL with urllib.request, and catches the HTTPError object that’s raised if an error occurs. If the URL is bad, it’ll catch a URLError. If it goes through without any errors, it’ll just print the status and return a tuple containing the body and the response. The response will close after return.

The function also calls urlopen() with a timeout argument, which will cause a TimeoutError to be raised after the seconds specified. Ten seconds is generally a good amount of time to wait for a response, though as always, much depends on the server that you need to make the request to.
"""
def make_request(url, headers=None, data=None): 
    # You can’t pass None, as this will cause an error.
    request = Request(url, headers=headers or {}, data=data)
    try:
        with urlopen(url, timeout=10) as response:
            print(response.status)
            return response.read(), response
    except HTTPError as error:
        print(error.status, error.reason)
    except URLError as error:
        print(error.reason)
    except TimeoutError:
        print("Request timed out")

# Command to run a .py file in interactive: python -i file.py

"""
* Dealing With 403 Errors

You can use the make_request() function to make some requests to httpstat.us, which is a mock server used for testing. This mock server will return responses that have the status code you request. If you make a request to https://httpstat.us/200, for example, you should expect a 200 response.

The 403 status means that the server understood the request but won’t fulfill it. This is a common error that you can run into, especially while web scraping. In many cases, you can solve it by passing a User-Agent header.

Note: There are two closely related 4xx codes that sometimes cause confusion:
    1. 401 Unauthorized
    2. 403 Forbidden
Servers should return 401 if the user isn’t identified or logged in and must do something to gain access, like log in or register.

The 403 status should be returned if the user is sufficiently identified but doesn’t have access to the resource. For example, if you’re logged in to a social media account and try to look at a person’s private profile page, then you’ll likely get a 403 status.
"""
make_request("https://httpstat.us/403") # 403 Forbidden

# One of the primary ways that servers identify who or what is making the request is by examining the User-Agent header. The raw default request sent by urllib.request is the following:
"""
///////////
GET https://httpstat.us/403 HTTP/1.1
Accept-Encoding: identity
Host: httpstat.us
User-Agent: Python-urllib/3.10
Connection: close
///////////
"""
# Notice that User-Agent is listed as Python-urllib/3.10. You may find that some sites will try to block web scrapers, and this User-Agent is a dead giveaway. With that said, you can set your own User-Agent with urllib.request.
# To customize the headers that you send out with your request, you first have to instantiate a Request object with the URL. Additionally, you can pass in a keyword argument of headers, which accepts a standard dictionary representing any headers you wish to include. So, instead of passing the URL string directly into urlopen(), you pass this Request object which has been instantiated with the URL and headers.

# In the example above, when Request is instantiated, you need to pass it the headers if they’ve been defined. Otherwise, pass a blank object, like {}. You can’t pass None, as this will cause an error.
# call make_request() with a dictionary representing the headers as an argument:
body, response = make_request("https://www.httpbin.org/user-agent", {"User-Agent": "Real Python"})
print(body) # b'{\n  "user-agent": "Real Python"\n}\n'
# In this example, you make a request to httpbin. Here you use the user-agent endpoint to return the request’s User-Agent value. Because you made the request with a custom user agent of Real Python, this is what gets returned.

"""
* Fixing the SSL CERTIFICATE_VERIFY_FAILED Error
"""

#################################################################################################

"""
Authenticated Requests:

One of the most common authentication tools is the bearer token, specified by RFC 6750. It’s often used as part of OAuth, but can also be used in isolation. It’s also most common to see as a header, which you can use with your current make_request() function.

In this example, you make a request to the httpbin /bearer endpoint, which simulates bearer authentication. It’ll accept any string as a token. It only requires the proper format specified by RFC 6750. The name has to be Authorization, or sometimes the lowercase authorization, and the value has to be Bearer, with a single space between that and the token.

Note: If you’re using any form of tokens or secret information, be sure to protect these tokens appropriately. For example, don’t commit them to a GitHub repository but instead store them as temporary environment variables.

Another form of authentication is called Basic Access Authentication, which is a very simple method of authentication, only slightly better than sending a username and password in a header. It’s very insecure!

One of the most common protocols in use today is OAuth (Open Authorization). If you’ve ever used Google, GitHub, or Facebook to sign into another website, then you’ve used OAuth. The OAuth flow generally involves a few requests between the service that you want to interact with and an identity server, resulting in a short-lived bearer token. This bearer token can then be used for a period of time with bearer authentication.

Much of authentication comes down to understanding the specific protocol that the target server uses and reading the documentation closely to get it working.
"""
token = "abcdefghijklmnopqrstuvwxyz"
headers = {"Authorization": f"Bearer {token}"}
make_request("https://httpbin.org/bearer", headers) 
# 200 (b'{\n  "authenticated": true, \n  "token": "abcdefghijklmnopqrstuvwxyz"\n}\n', <http.client.HTTPResponse object at 0x0000023D612642E0>)

#################################################################################################

"""
POST Requests With urllib.request:

To make POST requests with urllib.request, you don’t have to explicitly change the method. You can just pass a data object to a new Request object or directly to urlopen(). The data object must be in a special format, though. You’ll adapt your make_request() function slightly to support POST requests by adding the data parameter.

You can use one of two different formats to execute a POST request:
    1. Form Data: application/x-www-form-urlencoded
    2. JSON: application/json
The first format is the oldest format for POST requests and involves encoding the data with percent encoding, also known as URL encoding. You may have noticed key-value pairs URL encoded as a query string. Keys are separated from values with an equal sign (=), key-value pairs are separated with an ampersand (&), and spaces are generally suppressed but can be replaced with a plus sign (+).

If you’re starting off with a Python dictionary, to use the form data format with your make_request() function, you’ll need to encode twice:
    1. Once to URL encode the dictionary
    2. Then again to encode the resulting string into bytes
For the first stage of URL encoding, you’ll use another urllib module, urllib.parse. Remember to start your script in interactive mode so that you can use the make_request() function and play with it on the REPL.
"""
post_dict = {"Title": "Hello World", "Name": "Real Python"}
url_encoded_data = urlencode(post_dict)
print(url_encoded_data) # 'Title=Hello+World&Name=Real+Python'
post_data = url_encoded_data.encode("utf-8")
body, response = make_request("https://httpbin.org/anything", data=post_data) # 200
print(body.decode("utf-8"))
# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {
#     "Name": "Real Python",
#     "Title": "Hello World"
#   },
#   "headers": {
#     "Accept-Encoding": "identity",
#     "Content-Length": "34",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Host": "httpbin.org",
#     "User-Agent": "Python-urllib/3.10",
#     "X-Amzn-Trace-Id": "Root=1-61f25a81-03d2d4377f0abae95ff34096"
#   },
#   "json": null,
#   "method": "POST",
#   "origin": "86.159.145.119",
#   "url": "https://httpbin.org/anything"
# }

"""
In this example, you:

Import urlencode() from the urllib.parse module
Initialize your POST data, starting with a dictionary
Use the urlencode() function to encode the dictionary
Encode the resulting string into bytes using UTF-8 encoding
Make a request to the anything endpoint of httpbin.org
Print the UTF-8 decoded response body
UTF-8 encoding is part of the specification for the application/x-www-form-urlencoded type. UTF-8 is used preemptively to decode the body because you already know that httpbin.org reliably uses UTF-8.

The anything endpoint from httpbin acts as a sort of echo, returning all the information it received so that you can inspect the details of the request you made. In this case, you can confirm that method is indeed POST, and you can see that the data you sent is listed under form.
"""
# To make the same request with JSON, you’ll turn a Python dictionary into a JSON string with json.dumps(), encode it with UTF-8, pass it as the data argument, and finally add a special header to indicate that the data type is JSON:
json_string = json.dumps(post_dict)
print(json_string) # '{"Title": "Hello World", "Name": "Real Python"}'
post_data = json_string.encode("utf-8")
body, response = make_request("https://httpbin.org/anything", data=post_data, headers={"Content-Type": "application/json"}) # 200
print(body.decode("utf-8"))
# {
#   "args": {},
#   "data": "{\"Title\": \"Hello World\", \"Name\": \"Real Python\"}",
#   "files": {},
#   "form": {},
#   "headers": {
#     "Accept-Encoding": "identity",
#     "Content-Length": "47",
#     "Content-Type": "application/json",
#     "Host": "httpbin.org",
#     "User-Agent": "Python-urllib/3.10",
#     "X-Amzn-Trace-Id": "Root=1-61f25a81-3e35d1c219c6b5944e2d8a52"
#   },
#   "json": {
#     "Name": "Real Python",
#     "Title": "Hello World"
#   },
#   "method": "POST",
#   "origin": "86.159.145.119",
#   "url": "https://httpbin.org/anything"
# }

"""
To serialize the dictionary this time around, you use json.dumps() instead of urlencode(). You also explicitly add the Content-Type header with a value of application/json. With this information, the httpbin server can deserialize the JSON on the receiving end. In its response, you can see the data listed under the json key.
Note: Sometimes it’s necessary to send JSON data as plain text, in which case the steps are as above, except you set Content-Type as text/plain; charset=UTF-8. A lot of these necessities depend on the server or API that you’re sending data to, so be sure to read the documentation and experiment!
"""

#################################################################################################

"""
The Request Package Ecosystem:
"""
"""
* What Are urllib2 and urllib3?

To answer this question, you need to go back to early Python, all the way back to version 1.2, when the original urllib was introduced. Around version 1.6, a revamped urllib2 was added, which lived alongside the original urllib. When Python 3 came along, the original urllib was deprecated, and urllib2 dropped the 2, taking on the original urllib name. It also split into parts:
    urllib.error
    urllib.parse
    urllib.request
    urllib.response
    urllib.robotparser
So what about urllib3? That’s a third-party library developed while urllib2 was still around. It’s not related to the standard library because it’s an independently maintained library. Interestingly, the requests library actually uses urllib3 under the hood, and so does pip!
"""

"""
* When Should I Use requests Over urllib.request?

The main answer is ease of use and security. urllib.request is considered a low-level library, which exposes a lot of the detail about the workings of HTTP requests. The Python documentation for urllib.request makes no bones about recommending requests as a higher-level HTTP client interface.

If you interact with many different REST APIs, day in and day out, then requests is highly recommended. The requests library bills itself as “built for human beings” and has successfully created an intuitive, secure, and straightforward API around HTTP. It’s usually considered the go-to library!

An example of how requests makes things easier is when it comes to character encoding. You’ll remember that with urllib.request, you have to be aware of encodings and take a few steps to ensure an error-free experience. The requests package abstracts that away and will resolve the encoding by using chardet, a universal character encoding detector, just in case there’s any funny business.

If your goal is to learn more about standard Python and the details of how it deals with HTTP requests, then urllib.request is a great way to get into that. You could even go further and use the very low-level http modules. On the other hand, you may just want to keep dependencies to a minimum, which urllib.request is more than capable of.
"""

"""
* Why Is requests Not Part of the Standard Library?
"""