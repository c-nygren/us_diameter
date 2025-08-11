"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Project code. 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
# -----------------
# To Do
# -----------------
# - Implement directivity function
# - Add detailed description for directivity function
# - 



def directivity(
        height      : float,
        weight      : float,
        n_elements  : int,
        freq        : float,
        theta_s     : float,
        c           : float,
        x_true      : bool,
        y_true      : bool,
        range       : int, # must set equal to 1000, check formatting
        kerf        : float,
):
    """
    Calculate the directivity of a rectangular aperture.

    Parameters
    ----------
    height : float
        Height of aperture in m
    width : float
        Width of aperture in m
    n_elements : int
        Number of elements in the aperture
    freq : float
        Frequency of the ultrasound in Hz
    theta_s : float, optional
        Steering angle in radians
    c : float
        Speed of sound in m/s
    x_true : bool, optional
        If True, calculate x component of directivity
    y_true : bool, optional
        If True, calculate y component of directivity
    range : int, optional
        Number of points in the range of theta and phi. Default is 1000.

    Returns
    -------
    directivity : np.ndarray
        Directivity pattern of the aperture.
    """
