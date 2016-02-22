import crawl, compute_ranks, hash_stuff

index, graph = crawl.crawl_web('https://www.udacity.com/cs101x/urank/index.html')
ranks = compute_ranks.compute_ranks(graph)
print ranks
print index
