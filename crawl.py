
def get_next_target(page):
	start_link = page.find('<a href=')
	if start_link == -1:
		return None, 0
	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quote + 1)
	url = page[start_quote + 1 : end_quote]
	return url, end_quote

def rest_of_string(page):
	return s[1:]

def print_all_links(page):
	while True:
		url, endpos = get_next_target(page)
		if url:
			print url
			page = page[endpos:]
		else:
			break

def get_all_links(page):
	links = []
	while True:
		url, endpos = get_next_target(page)
		if url:
			links.append(url)
			page = page[endpos:]
		else:
			break
	return links

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''

def union(list_1, list_2):
    for item in list_2:
        if item not in list_1:
            list_1.append(item)


def crawl_web(seed):
	to_crawl = [seed]
	crawled = []
	index = {}
	graph = {}

	while to_crawl:
		page = to_crawl.pop()
		if page not in crawled:
			content = get_page(page)
			add_page_to_index(index, page, content)
			outlinks = get_all_links(content)
			union(to_crawl, outlinks)

			graph[page] = outlinks

			crawled.append(page)
			
	return index, graph


#uses depth first search so not really a good way to build a corpus of the web, 
#but meh, was just practice


def add_to_index(index, keyword, url):
	if keyword in index:
		index[keyword].append(url)
	else:
		index[keyword] = [url]

def lookup(index, keyword):
	if keyword in index:
		return index[keyword]
	else:
		return None

def add_page_to_index(index,url,content):
        words = content.split()
        for word in words:
        	add_to_index(index, word, url)

