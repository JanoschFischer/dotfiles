from libqtile.config import Key
from libqtile.lazy import lazy
import os

mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser("~")

TERMINAL = "urxvt"
TERMINAL2 = "alacritty"
EDITOR = "code"
PROGRAMS = "rofi -show run"


def init_keys():
    return [
        # Bindings [mod]:
        Key([mod], "t", lazy.spawn(TERMINAL)),
        Key([mod], "Return", lazy.spawn(TERMINAL2)),
        Key([mod], "p", lazy.spawn("rofi -show run")),
        Key([mod], "b", lazy.spawn("brave")),
        Key([mod], "x", lazy.spawn("arcolinux-logout")),
        Key([mod], "Escape", lazy.spawn("xkill")),
        Key([mod], "i", lazy.spawn("light-locker-command -l")),
        Key([mod], "f", lazy.window.toggle_fullscreen()),
        Key([mod], "q", lazy.window.kill()),
        Key([mod], "r", lazy.restart()),
        
        Key([mod2], "Print", lazy.spawn("xfce4-screenshooter")),
        Key([mod2, "shift"], "Print", lazy.spawn("gnome-screenshot -i")),
        # INCREASE/DECREASE BRIGHTNESS
        Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
        Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),
        # INCREASE/DECREASE/MUTE VOLUME
        Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
        Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
        Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),
        # QTILE LAYOUT KEYS
        Key([mod], "n", lazy.layout.normalize()),
        Key([mod], "space", lazy.next_layout()),
        # CHANGE FOCUS
        Key([mod], "Up", lazy.layout.up()),
        Key([mod], "Down", lazy.layout.down()),
        Key([mod], "Left", lazy.layout.left()),
        Key([mod], "Right", lazy.layout.right()),
        Key([mod], "k", lazy.layout.up()),
        Key([mod], "j", lazy.layout.down()),
        Key([mod], "h", lazy.layout.left()),
        Key([mod], "l", lazy.layout.right()),
        # RESIZE UP, DOWN, LEFT, RIGHT
        Key(
            [mod, "control"],
            "l",
            lazy.layout.grow_right(),
            lazy.layout.grow(),
            lazy.layout.increase_ratio(),
            lazy.layout.delete(),
        ),
        Key(
            [mod, "control"],
            "Right",
            lazy.layout.grow_right(),
            lazy.layout.grow(),
            lazy.layout.increase_ratio(),
            lazy.layout.delete(),
        ),
        Key(
            [mod, "control"],
            "h",
            lazy.layout.grow_left(),
            lazy.layout.shrink(),
            lazy.layout.decrease_ratio(),
            lazy.layout.add(),
        ),
        Key(
            [mod, "control"],
            "Left",
            lazy.layout.grow_left(),
            lazy.layout.shrink(),
            lazy.layout.decrease_ratio(),
            lazy.layout.add(),
        ),
        Key(
            [mod, "control"],
            "k",
            lazy.layout.grow_up(),
            lazy.layout.grow(),
            lazy.layout.decrease_nmaster(),
        ),
        Key(
            [mod, "control"],
            "Up",
            lazy.layout.grow_up(),
            lazy.layout.grow(),
            lazy.layout.decrease_nmaster(),
        ),
        Key(
            [mod, "control"],
            "j",
            lazy.layout.grow_down(),
            lazy.layout.shrink(),
            lazy.layout.increase_nmaster(),
        ),
        Key(
            [mod, "control"],
            "Down",
            lazy.layout.grow_down(),
            lazy.layout.shrink(),
            lazy.layout.increase_nmaster(),
        ),
        # FLIP LAYOUT FOR MONADTALL/MONADWIDE
        Key([mod, "shift"], "f", lazy.layout.flip()),
        # FLIP LAYOUT FOR BSP
        Key([mod, "mod1"], "k", lazy.layout.flip_up()),
        Key([mod, "mod1"], "j", lazy.layout.flip_down()),
        Key([mod, "mod1"], "l", lazy.layout.flip_right()),
        Key([mod, "mod1"], "h", lazy.layout.flip_left()),
        # MOVE WINDOWS UP OR DOWN BSP LAYOUT
        Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
        Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
        Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
        Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
        # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
        Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
        Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
        Key([mod, "shift"], "Left", lazy.layout.swap_left()),
        Key([mod, "shift"], "Right", lazy.layout.swap_right()),
        # TOGGLE FLOATING LAYOUT
        Key([mod, "shift"], "space", lazy.window.toggle_floating()),
    ]
