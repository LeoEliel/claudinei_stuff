'''def generateNode(data):
    return {
            'prev': None,
            'value': data,
            'next': None
            }

def addNode(head, data):
    
    new_node = generateNode(data)

    if not head:
        return new_node
    
    else:
        head['prev'] = new_node
        new_node['next'] = head

        return new_node

def display(head):
    
    current = head

    while current:
        print(current['value'])
        current = current['next']

def displayReverse(head):

    current = head

    while current and current['next']:
        current = current['next']

    while current:
        print(current['value'])
        current = current['prev']

def main():
    head = None

    head = addNode(head, 1)
    head = addNode(head, 2)
    head = addNode(head, 3)

    print(f'\n{display(head)}')
    print(f'\n{displayReverse(head)}')

if __name__ == '__main__':
    main()'''

def generateNode(data):

    return {
            'prev': None,
            'value': data,
            'next': None
        }

def addNode(head, data):
    
    new_node = generateNode(data)

    if not head:
        return new_node
    
    else:
        head['prev'] = new_node
        new_node['next'] = head

        return new_node

def insertBetween(head, data, after_value):
    new_node = generateNode(data)
    current = head

    while current and current['value'] != after_value:
        current = current['next']
    
    if not current:
        print(f'valor {after_value} não encontrado na lista')
        return head
    
    next_node = current['next']

    if next_node:
            next_node['prev'] = new_node

    new_node['next'] = next_node

    new_node['prev'] = current

    current['next'] = new_node

    return head

def display(head):
    
    current = head

    while current:
        print(current['value'])
        current = current['next']

    current = head

    while current and current['next']:
        current = current['next']

    while current:
        print(current['value'])
        current = current['prev']

def main():
    head = None

    head = addNode(head, 'D')
    head = addNode(head, 'B')
    head = addNode(head, 'A')

    print(f'\nMostra do início: \n{display(head)}')

    head = insertBetween(head, 'C', 'B')

    print(f'\nMostra do início com a inserção de "C" no meio: \n{display(head)}')

if __name__ == '__main__':
    main()