def num_cuts(height, width):
    if height == width:
        return 0;
    if height > width:
        return 1 + num_cuts(height - width, width)
    else:
        return 1 + num_cuts(height, width - height)



height = int(input())
width = int(input())
print(num_cuts(height,width))