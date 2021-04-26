import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

from typing import List
from plotwise.problem.demand import Coordinate


def plot_route(route: List[Coordinate]):
    vertices = [(event.coordinate.x, event.coordinate.y) for event in route]

    verts = [vertices[0]] + vertices
    codes = [Path.MOVETO] + [Path.LINETO] * len(vertices)

    path = Path(verts, codes)

    patch = patches.PathPatch(path, facecolor="none", lw=2)

    fig, ax = plt.subplots()

    ax.add_patch(patch)

    xs, ys = zip(*verts)
    ax.plot(xs, ys, "x--", lw=2, color="black", ms=10)

    return fig, ax