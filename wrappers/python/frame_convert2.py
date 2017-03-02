import numpy as np

def get_gradient_color(value, max_value=1024.0):
    #we use 4 colours in our gradient so we normalize value in [0, 4]
    normalized_value = float(value)*4/max_value
    gradient_color = (0, 0, 0)

    #yellow -> red
    if normalized_value > 3:
        normalized_value -= 3
        gradient_color = (255, 255*(1-normalized_value), 0)
    #green -> yellow
    elif normalized_value > 2:
        normalized_value -= 2
        gradient_color = (255*normalized_value, 255, 0)
    #cyan -> green
    elif normalized_value > 1:
        normalized_value -= 2
        gradient_color = (0, 255, 255*(1-normalized_value))
    #blue -> cyan
    else:
        gradient_color = (0, 255*(1-normalized_value), 255)

    return gradient_color


def pretty_depth(depth):
    """Converts depth into a 'nicer' format for display

    This is abstracted to allow for experimentation with normalization

    Args:
        depth: A numpy array with 2 bytes per pixel

    Returns:
        A numpy array that has been processed with unspecified datatype
    """

    np.clip(depth, 0, 1024, depth)
    #depth = depth.astype(np.uint8) 

    #return vector_gradient_color(depth)
    """color = np.zeros((len(depth), len(depth[0]), 3))
    for x in range(len(depth)):
        for y in range(len(depth[0])):
            color[x][y] = get_gradient_color(depth[x][y])"""

    gradient_image = []
    for l in depth:
        gradient_image.append(map(get_gradient_color, l))

    #gradient_image = map(get_gradient_color, depth)

    return gradient_image

def pretty_depth_cv(depth):
    """Converts depth into a 'nicer' format for display

    This is abstracted to allow for experimentation with normalization

    Args:
        depth: A numpy array with 2 bytes per pixel

    Returns:
        A numpy array with unspecified datatype
    """
    return pretty_depth(depth)


def video_cv(video):
    """Converts video into a BGR format for display

    This is abstracted out to allow for experimentation

    Args:
        video: A numpy array with 1 byte per pixel, 3 channels RGB

    Returns:
        A numpy array with with 1 byte per pixel, 3 channels BGR
    """
    return video[:, :, ::-1]  # RGB -> BGR
