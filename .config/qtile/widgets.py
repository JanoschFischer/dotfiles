import requests

from colors import init_colors
from dataclasses import dataclass
from libqtile import widget

colors = init_colors()



@dataclass
class Font:
    regular: str = "Inconsolata"
    bold: str = "Inconsolata Bold"
    size_small: int = 10
    size_large: int = 14


SEPERATOR = widget.Sep(
    linewidth=2, padding=10, size_percent=50, foreground=colors[2], background=colors[0]
)

SEPERATORHOR = widget.Sep(
    linewidth=10,
    padding=20,
    size_percent=5,
    foreground=colors[2],
    background=colors[0],
)

SEPERATORBLANK = widget.Sep(
    linewidth=0,
    padding=20,
    size_percent=5,
    foreground=colors[0],
    background=colors[5],
)

LAYOUTICON = widget.CurrentLayoutIcon(
    font=Font.regular,
    fontsize=Font.size_large,
    scale=0.65,
    foreground=colors[5],
    background=colors[0],
)


GROUPBOX = widget.GroupBox(
    font="FontAwesome Bold",
    fontsize=Font.size_large,
    margin_y=2,
    padding_x=5,
    disable_drag=True,
    active=colors[7],
    inactive=colors[6],
    highlight_method="block",
    this_current_screen_border=colors[5],
    foreground=colors[2],
    background=colors[0],
)

WINDOWNAME = widget.WindowName(
    font=Font.bold,
    fontsize=Font.size_large,
    foreground=colors[0],
    background=colors[5],
)

CLOCK = widget.Clock(
    font=Font.bold,
    fontsize=Font.size_large,
    foreground=colors[0],
    background=colors[5],
    format="%H:%M",
)

BATTERY = widget.Battery(
    font=Font.bold,
    fontsize=Font.size_large,
    update_interval=10,
    format="{percent:2.0%} \uf241",
    foreground=colors[5],
    background=colors[0],
)


def init_widgets_list():
    widgets_list = [
        LAYOUTICON,
        SEPERATOR,
        GROUPBOX,
        SEPERATORHOR,
        SEPERATORBLANK,
        WINDOWNAME,
        CLOCK,
        SEPERATORBLANK,
        SEPERATORHOR,
        BATTERY,
        SEPERATOR,
        widget.TextBox(
            text="",
            # font="FontAwesome",
            font=Font.regular,
            fontsize=Font.size_large,
        ),
        widget.NetGraph(
            background=colors[0],
            fill_color=colors[5],
            border_color=colors[7][0],
            graph_color=colors[9][0],
            bandwidth_type="down",
            frequency=1,
            border_width=1,
            interface="auto",
        ),
        SEPERATOR,
        widget.TextBox(
            text=requests.get("http://ip.42.pl/raw").text,
            # font="FontAwesome",
            font=Font.regular,
            fontsize=Font.size_small,
        ),
        widget.Systray(background=colors[1], icon_size=20, padding=4),
    ]
    return widgets_list
