"""
Created on Mon Feb 11 13:28:27 2018
@author: Sinh Bui <buiducsinh34@gmail.com>
"""


def create_double_curve(canvas_root, x1, y1, x2, y2):
    """Draw a curved line from A(x1, y1) to B(x2, y2)

    :param canvas_root: the tkinter canvas on which you would like to draw a double-curve
    :param x1: A's horizontal coordinate
    :param y1: A's vertical coordinate
    :param x2: B's horizontal coordinate
    :param y2: B's vertical coordinate
    """
    if y1 == y2:
        canvas_root.tag_lower(canvas_root.create_line(x1, y1, x2, y2))
        return
    if x1 < x2:
        mid_x = (x1+x2)/2; mid_y = (y1+y2)/2
        if y1 > mid_y:
            if x1 > mid_x:
                bbox_x1 = mid_x; bbox_y1 = 2*mid_y - y1; bbox_x2 = 2*x1 - mid_x; bbox_y2 = y1; start_ang = 180
            else:
                bbox_x1 = 2*x1 - mid_x; bbox_y1 = 2*mid_y - y1; bbox_x2 = mid_x; bbox_y2 = y1; start_ang = 270
        else:
            if x1 > mid_x:
                bbox_x1 = mid_x; bbox_y1 = y1; bbox_x2 = 2*x1 - mid_x; bbox_y2 = 2*mid_y - y1; start_ang = 90
            else:
                bbox_x1 = 2*x1 - mid_x; bbox_y1 = y1; bbox_x2 = mid_x; bbox_y2 = 2*mid_y - y1; start_ang = 0
        canvas_root.tag_lower(canvas_root.create_arc(bbox_x1, bbox_y1, bbox_x2, bbox_y2, start=start_ang, extent=90,
                                                     style=tk.ARC))
        if y2 > mid_y:
            if x2 > mid_x:
                bbox_x1 = mid_x; bbox_y1 = 2*mid_y - y2; bbox_x2 = 2*x2 - mid_x; bbox_y2 = y2; start_ang = 180
            else:
                bbox_x1 = x2 - (mid_x-x1); bbox_y1 = 2*mid_y - y2; bbox_x2 = mid_x; bbox_y2 = y2; start_ang = 270
        else:
            if x2 > mid_x:
                bbox_x1 = mid_x; bbox_y1 = y2; bbox_x2 = 2*x2 - mid_x; bbox_y2 = 2*mid_y - y2; start_ang = 90
            else:
                bbox_x1 = 2*x2 - mid_x; bbox_y1 = y2; bbox_x2 = mid_x; bbox_y2 = 2*mid_y - y2; start_ang = 0
        canvas_root.tag_lower(canvas_root.create_arc(bbox_x1, bbox_y1, bbox_x2, bbox_y2, start=start_ang, extent=90,
                                                     style=tk.ARC))
        return
    else:
        create_double_curve(canvas_root, x2, y2, x1, y1)
