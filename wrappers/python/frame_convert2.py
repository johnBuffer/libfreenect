import numpy as np

def get_gradient_color(value, max_value=1024.0):
    #we use 4 colours in our gradient so we normalize value in [0, 4]
    normalized_value = float(float(value)*3/max_value)
    normalized_value = min(normalized_value, 4)
    (r, g, b) = (0, 0, 0)

    #print(normalized_value)

    #yellow -> red
    if normalized_value > 3:
        normalized_value -= 3
        (r, g, b) = (255, 255*(1-normalized_value), 0)
    #green -> yellow
    elif normalized_value > 2:
        normalized_value -= 2
        (r, g, b) = (255*normalized_value, 255, 0)
    #cyan -> green
    elif normalized_value > 1:
        normalized_value -= 1
        (r, g, b) = (0, 255, 255*(1-normalized_value))
    #blue -> cyan
    else:
        (r, g, b) = (0, 255*(1-normalized_value), 255)

    #return (r, g, b)
    return (255, 0, 0)

def apply_gradient(matrix):
    map(get_gradient_color, matrix)


def pretty_depth(depth):
    """Converts depth into a 'nicer' format for display

    This is abstracted to allow for experimentation with normalization

    Args:
        depth: A numpy array with 2 bytes per pixel

    Returns:
        A numpy array that has been processed with unspecified datatype
    """

    np.clip(depth, 0, 1024, depth)
    """
    depth >>= 2
    depth = depth.astype(np.uint8)
    """

    gradient_image = [[]]*len(depth)
    for l in range(len(depth)):
        gradient_image[l] = map(get_gradient_color, depth[l])

    #gradient_image = map(apply_gradient, depth)

    depth = np.array(gradient_image)
    depth = depth.astype(np.uint8)

    return depth

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
