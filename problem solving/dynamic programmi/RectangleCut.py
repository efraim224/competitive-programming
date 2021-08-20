def num_cuts(height, width):
    if height == width:
        return 0;
    if height > width:
        return 1 + num_cuts(height - width, width)
    else:
        return 1 + num_cuts(height, width - height)



height, width = map(int, input().split())
print(num_cuts(height,width))