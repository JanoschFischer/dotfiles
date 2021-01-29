
import os
import subprocess
from libqtile.config import Drag, Key, Screen, Group, Drag
from libqtile.lazy import lazy
from libqtile import layout, bar, hook


from colors import init_colors
from widgets import init_widgets_list
from keys import init_keys


keys = init_keys()
widgets_list = init_widgets_list()
colors = init_colors()

# mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser("~")

TERMINAL = "urxvt"
EDITOR = "code"
PROGRAMS = "rofi -show run"

focus_on_window_activation = 'smart'

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


groups = []

NUM_OF_GROUPS = 5

group_names = [str(i) for i in range(1, NUM_OF_GROUPS + 1)]
group_labels = ["", "", "", "", ""]

# group_labels = [str(i) for i in range(1, NUM_OF_GROUPS + 1)]
group_layouts = ["monadtall" for i in range(NUM_OF_GROUPS)]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        )
    )

for i in groups:
    keys.extend(
        [
            # CHANGE WORKSPACES
            Key([mod], i.name, lazy.group[i.name].toscreen()),
            Key([mod], "Tab", lazy.screen.next_group()),
            Key(["mod1"], "Tab", lazy.screen.next_group()),
            Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),
            # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
            # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
        ]
    )


layouts = [
    layout.MonadTall(
        margin=10, 
        border_width=2, 
        border_focus=colors[8][0], 
        border_normal=colors[4][0],
        ratio=0.6
    ),
]



def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


# def init_widgets_screen2():
#     widgets_screen2 = init_widgets_list()
#     return widgets_screen2


widgets_screen1 = init_widgets_screen1()
# widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [
        Screen(top=bar.Bar(margin=[5,10,0,10],widgets=init_widgets_screen1(), size=20, opacity=0.9)),
        # Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26)),
    ]


screens = init_screens()


# MOUSE CONFIGURATION
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []


main = None


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/scripts/autostart.sh"])


@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(["xsetroot", "-cursor_name", "left_ptr"])


@hook.subscribe.client_new
def set_floating(window):
    if (
        window.window.get_wm_transient_for()
        or window.window.get_wm_type() in floating_types
    ):
        window.floating = True


floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        {"wmclass": "Arcolinux-welcome-app.py"},
        {"wmclass": "Arcolinux-tweak-tool.py"},
        {"wmclass": "confirm"},
        {"wmclass": "dialog"},
        {"wmclass": "download"},
        {"wmclass": "error"},
        {"wmclass": "file_progress"},
        {"wmclass": "notification"},
        {"wmclass": "splash"},
        {"wmclass": "toolbar"},
        {"wmclass": "confirmreset"},
        {"wmclass": "makebranch"},
        {"wmclass": "maketag"},
        {"wmclass": "Arandr"},
        {"wmclass": "feh"},
        {"wmclass": "Galculator"},
        {"wmclass": "arcolinux-logout"},
        {"wmclass": "xfce4-terminal"},
        {"wname": "branchdialog"},
        {"wname": "Open File"},
        {"wname": "pinentry"},
        {"wmclass": "ssh-askpass"},
    ],
    fullscreen_border_width=0,
    border_width=2,
    border_focus=colors[8][0], 
    border_normal=colors[4][0],
)
auto_fullscreen = True

focus_on_window_activation = "focus"  # or smart

wmname = "LG3D"
