class Cell:
    """
    Cell for sorted linked list.
    """
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

def bucketsort(values, num_buckets):
    """
    Bucket sorting.
    """

    # Create bucks in which put empty linked lists.
    buckets = []
    for i in range(num_buckets):
        buckets.append(Cell())

    # Сalculate maximum value in array.
    i = 0
    max_value = values[i]
    while i < len(values):
        if values[i] > max_value:
            max_value = values[i]
        i += 1

    # Calculate numbers of values in bucket.
    items_per_bucket = (max_value + 1) / num_buckets

    # Distribute values in the bucket.
    for value in values:
        # Calculate number of bucket.
        backet_num = int(value / items_per_bucket)

        # Insert value into bucket with sorting.
        after_me = buckets[backet_num]
        while (after_me.next_node is not None) and (after_me.next_node.value < value):
            after_me = after_me.next_node
        cell = Cell(value, after_me.next_node)
        after_me.next_node = cell

    # Send values back to the array.
    index = 0
    for i in range(num_buckets):
        # Copy values from bucket to array.
        cell = buckets[i].next_node
        while cell is not None:
            values[index] = cell.value
            index += 1
            cell = cell.next_node

data = [3, 7, 8, 1, 2, 4, 9, 6, 5, 0]
bucketsort(data, 4)
print(data)
