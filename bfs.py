graph= {
    'Chamkarmon': {
        'listing' :[
            {'type':'room', 'price': 120},
            {'type':'room', 'price': 50},
            {'type':'apartment', 'price': 200},
        ],
        'neighbor': ['MeanChey','ChbarAmpov','BKK','ToulKork','7Makara','DaunPenh']
    },
    'DaunPenh': {
        'listing' :[
            {'type':'room', 'price': 200},
            {'type':'apartment', 'price': 350},
            {'type':'apartment', 'price': 360},
            {'type':'room', 'price': 150},
        ],
        'neighbor': ['BKK','7Makara','ToulKork','ChroyChangva']
    },
    'Dangkor': {
        'listing' :[
            {'type':'room', 'price': 200},
            {'type':'apartment', 'price': 350},
            {'type':'apartment', 'price': 100},
            {'type':'house', 'price': 500},
        ],
        'neighbor': ['MeanChey','Kamboul']
    },
    'MeanChey': {
        'listing': [
            {'type':'apartment', 'price': 170},
            {'type':'apartment', 'price': 200},
            {'type':'house', 'price': 250},
            {'type':'house', 'price': 350},
        ],
        'neighbor': ['ChbarAmpov','Chamkarmon','RusseyKeo','SenSok','Kamboul']
    },
    'PorSenChey': {
        'listing': [
            {'type':'house', 'price': 170},
            {'type':'room', 'price': 50},
        ],
        'neighbor': ['PrekPhnov','Kamboul','SenSok','MeanChey']
    },
    'RusseyKeo': {
        'listing': [
            {'type':'apartment', 'price': 150},
            {'type':'room', 'price': 90},
        ],
        'neighbor': ['ChroyChangva','SenSok','ToulKork','DaunPenh']
    },
    'SenSok': {
        'listing': [
            {'type':'apartment', 'price': 180},
            {'type':'room', 'price': 90},
            {'type':'house', 'price': 350},
            {'type':'apartment', 'price': 250},
            {'type':'apartment', 'price': 170},
            {'type':'house', 'price': 400},
        ],
        'neighbor': ['RusseyKeo','ToulKork','MeanChey','PorSenChey','PrekPhnov']
    },
    'ToulKork': {
        'listing': [
            {'type':'apartment', 'price': 200},
            {'type':'room', 'price': 170},
            {'type':'room', 'price': 200},
            {'type':'room', 'price': 180},
        ],
        'neighbor': ['SenSok','RusseyKeo','MeanChey','DaunPenh','7Makara','Chamkarmon']
    },
    '7Makara': {
        'listing': [
            {'type':'apartment', 'price': 270},
            {'type':'room', 'price': 120},
            {'type':'room', 'price': 150},
        ],
        'neighbor': ['ToulKork','Chamkarmon','BKK','DaunPenh']
    },
    'ChbarAmpov': {
        'listing': [
            {'type':'apartment', 'price': 180},
            {'type':'room', 'price': 50},
        ],
        'neighbor': ['MeanChey','BKK']
    },
    'ChroyChangva': {
        'listing': [
            {'type':'house', 'price': 270},
            {'type':'house', 'price': 350},
            {'type':'apartment', 'price': 190},
            {'type':'apartment', 'price': 210},
        ],
        'neighbor': ['RusseyKeo','DaunPenh']
    },
    'PrekPhnov': {
        'listing': [
            {'type':'house', 'price': 230},
            {'type':'apartment', 'price': 170},
            {'type':'apartment', 'price': 150},
            {'type':'room', 'price': 120},
        ],
        'neighbor': ['PorSenChey','SenSok','RusseyKeo']
    },
    'BKK': {
        'listing': [
            {'type':'house', 'price': 170},
            {'type':'apartment', 'price': 200},
            {'type':'room', 'price': 70},
            {'type':'room', 'price': 50},
        ],
        'neighbor': ['Chamkarmon','DaunPenh','7Makara','ChbarAmpov']
    },
    'Kamboul': {
        'listing': [
            {'type':'house', 'price': 150},
            {'type':'house', 'price': 200},
            {'type':'room', 'price': 60},
        ],
        'neighbor': ['PorSenChey','Dangkor']
    }
}
startNode='Chamkarmon'
def bfsSearch(graph, endNode, priceRange, typeAccomadation, output_func=print):
    visited = []  #create node to keep track on visited node
    queue = [startNode] #append Chamkarmon to queue to look for designated node
    while queue != []:  #if queue is not empty continue looping until meet condition
        currentNode = queue.pop(0)  #remove 0 index of queue after visited every loop until right condition meet
        if currentNode not in visited: # check if current node != visited append current node with visited below if not move to second condition 'Success'
          visited.append(currentNode) #current node into visited to allow checking on next new node
          output_func(f" Visiting {currentNode}...")
        output_func(f"Queue Node: {queue}")
        if currentNode == endNode:
            output_func(f"====================================================")
            output_func(f"'{endNode}' location is found successfully! \^o^/")
            found = False
            output_func(f"====================================================")
            output_func(f"We are working on filtering price and house type....")
            output_func(f"====================================================")
            for listing in graph[currentNode]['listing']:
              if listing['price'] <= priceRange and listing['type'] == typeAccomadation: #set filter for any price below input price
                output_func(f"Yay Listings found with max price {priceRange}$: {currentNode}: {listing['type']} for ${listing['price']}")
                found = True
            if not found:
              output_func(f"Whoops listings not found in '{currentNode}' with your input price and type :(")
            return

        for neighbor in graph[currentNode]['neighbor']:  #loop in neighbor, grab 'neighbor' list and check if node is visited or not if not append it to queue (if node is visited alr we will not check it again)
          if neighbor not in visited:
            queue.append(neighbor)

#=======Testing input========
# print("Enter location: ")
# endNode = input()
# print('Enter Maximum price: ')
# priceRange = int(input())
# print('Enter type of accomadation: ')
# typeAccomadation = input()
# bfsSearch(graph, input(),priceRange=int(input()),typeAccomadation=input())

