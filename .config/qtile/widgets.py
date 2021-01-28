from libqtile import widget
import os
import socket
import requests
from colors import init_colors

colors = init_colors()


def init_widgets_list():
    FONT_LARGE = 16
    FONT_SMALL = 10
    FONT_NOTO = "Noto Sans Bold"
    FONT_AWESOME = "Inconsolata Bold"
    # FONT_AWESOME = "FontAwesome Bold"
    SEPERATOR = widget.Sep(
        linewidth=1,
        padding=10,
        size_percent=50,
        foreground=colors[2],
        background=colors[1],
    )

    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
        widget.CurrentLayoutIcon(
            font=FONT_NOTO,
            scale=0.5,
            fontsize=FONT_SMALL,
            margin_y=-1,
            foreground=colors[8],
            background=colors[1],
        ),
        SEPERATOR,
        widget.GroupBox(
            font=FONT_AWESOME,
            #fontsize=FONT_LARGE,
            fontsize=14,
            margin_y=2,
            margin_x=0,
            padding_y=0,
            padding_x=8,
            borderwidth=0,
            disable_drag=True,
            active=colors[7],
            inactive=colors[6],
            # rounded = False,
            highlight_method="block",
            this_current_screen_border=colors[5],
            foreground=colors[2],
            background=colors[1],
        ),
        widget.Sep(
            linewidth=10,
            padding=20,
            size_percent=5,
            foreground=colors[2],
            background=colors[1],
        ),
        widget.Sep(
            linewidth=0,
            padding=20,
            size_percent=5,
            foreground=colors[0],
            background=colors[5],
        ),
        widget.WindowName(
            font=FONT_AWESOME,
            fontsize=FONT_LARGE,
            foreground=colors[0],
            background=colors[5],
        ),
        widget.Clock(
            font=FONT_AWESOME,
            fontsize=FONT_LARGE,
            foreground=colors[0],
            background=colors[5],
            format="%H:%M",
        ),
        widget.Sep(
            linewidth=0,
            padding=20,
            size_percent=5,
            foreground=colors[0],
            background=colors[5],
        ),
        widget.Sep(
            linewidth=10,
            padding=30,
            size_percent=5,
            foreground=colors[2],
            background=colors[1],
        ),
        
        # widget.Clock(
        #     font=FONT_AWESOME,
        #     fontsize=FONT_LARGE,
        #     foreground=colors[5],
        #     background=colors[1],
        #     format="%d.%m.%Y",
        # ),
        # SEPERATOR,
        widget.Battery(
            font=FONT_AWESOME,
            fontsize=FONT_LARGE,
            update_interval=10,
            format="{percent:2.0%} \uf241",
            foreground=colors[5],
            background=colors[1],
        ),
        SEPERATOR,
        widget.TextBox(
            text="",
            font="FontAwesome",
            fontsize=FONT_LARGE
        ),
        widget.NetGraph(
            background=colors[1],
            fill_color=colors[5],
            border_color=colors[7][0],
            graph_color=colors[9][0],
            bandwidth_type='down',
            frequency=1,
            border_width=1,
            interface='auto'
            ),
        SEPERATOR,
        # widget.TextBox(
        #     text="",
        #     font="FontAwesome",
        #     fontsize=FONT_LARGE
        # ),
        # widget.NetGraph(
        #     background=colors[1],
        #     fill_color=colors[5],
        #     border_color=colors[7][0],
        #     graph_color=colors[9][0],
        #     bandwidth_type='up',
        #     frequency=1,
        #     border_width=1,
        #     interface='auto'
        #     ),
        # widget.CheckUpdates(
            # background=colors[1],
            # display_format='Packages: {updates}',
            # no_update_string='Packages: 0',
            # distro='Arch',
            # execute='paru',
            # font=FONT_AWESOME,
            # fontsize=FONT_LARGE# 
        # ),
        # SEPERATOR,
        widget.TextBox(
            text=requests.get('http://ip.42.pl/raw').text,
            font="FontAwesome",
            fontsize=FONT_SMALL
        ),
        widget.Systray(background=colors[1], icon_size=20, padding=4),
    ]
    return widgets_list