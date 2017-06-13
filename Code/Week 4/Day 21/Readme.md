# Day 21

Today I was answering questions on treehouse's forum. This is the one that I spent real time on. The question was

>**Switching Keys and values Python**

>Hi

>How could I go about switching keys and value of a dictionary in Python, I think it would pretty achievable using a for loop, however I am struggling to figure it out with the following requirements

>Keys are arrays
>Keys and value could appear twice
>Example:
> ```python
>interfaces = {
>        ["172.17.110.1", "255.255.255.0"] : "ACCESS",
>        ["172.18.165.1", "255.255.255.0"] : "WAN",
>        ["172.19.132.1", "255.255.255.0"] : "ACCESS",
>        ["172.19.34.1", "255.255.255.0"] : "WAN",
>        ["172.12.134.1", "255.255.255.0"] : "APP"
>        }
> ```
>Thanks in advance, really struggled to figure this out.

I first researched the __hash__ method and how to test for it in is_mutable.py, then began testing list, sets, dictionarys until I got a really good understanding of the topic. Itwas a good couple of hours of research and experiments. My answer was voted best by the OP, here is the response I gave:

>Jon Mirow 
>3 hours ago
>As Alex said, keys must be immutable, and in the case of tuples as keys, all of their contents must be immutable. Tuple's can be a >powerful way of using a dictionary, allowing you to look up multiple combinations of values, but of course, most dictionaries probably >don't need tuples for keys, so it's worth pointing out that this could be a warning sign to double-check your approach.

>Here, the warning sign isn't using tuples - IP addresses and subnet masks (I assume) in tuples would be very good keys. However that >"keys and values may not be unique"... Basically that would be a red flag not to do this. If you can't guarantee that each IP and subnet >mask pair were unique you couldn't do it. Basically to switch keys with values you have to be sure that the values in the dictionary >will always be unique, and then handle any mutable objects.

>Moreover you don't control the data creation. If it's an external API, it's perfectly reasonable to assume that a future update to the >API may add items to the list, add nested lists, or dictionarys, or custom objects that don't have a .hash method. All of these things >could be appended to the list in the dictionary (or JSON) without affecting the "normal" use of the api - dictionary[key][value index]

>Anyway to answer the question, Assuming you only had a dictionary of keys and values in the form of a 1D list, you could switch them >over like this:
> ```python
>#Assume the Api data looks a bit like this:
>api_data =  {
>        "ACCESS": ["172.17.110.1", "255.255.255.0"],
>        "WAN": ["172.18.165.1", "255.255.255.0"],
>        "APP": ["172.19.132.1", "255.255.255.0"],
>        "LAN": ["172.19.34.1", "255.255.255.0"],
>        "DNS": ["172.12.134.1", "255.255.255.0"]
>        }
>
>api_data_formatted = { tuple(value): key for key, value in api_data.items()}
> ```
>Would do the job.
>
>But like I say, you really want to be quite sure about what's in the dictionary first of all. Hope it helps!
