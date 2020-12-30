# ================================
#!/bin/bash
# Personalización de QTile 
# Fernando Castillo
# ferncastillov@outlook.com
# ================================

# IMPORTS
import os
import re
import socket
import subprocess

from typing import List  # noqa: F401
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen, Match
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
# terminal = guess_terminal()
terminal = 'konsole'

# @hook.subscibe.startup_once
# def autostart():
#    home = os.path.expanduser('/home/nyakode/.config/qtile/autostart.sh')
#    subprocess.call([home])
#
# ================================
# Definimos las "keys" de acceso directo
# ================================ 
keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "h", lazy.layout.left()),

    # Change window sizes (MonadTall)
    Key([mod, "shift"], "l", lazy.layout.grow()),
    Key([mod, "shift"], "h", lazy.layout.shrink()),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn(terminal)),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),

    # APPS CONFIG
    # menu
    Key([mod], "m", lazy.spawn("rofi -show run")),
    
    # visual 
    Key([mod], "v", lazy.spawn("code")),

    #Sublime
    Key([mod], "s", lazy.spawn("subl")),

    # Firefox
    Key([mod], "f", lazy.spawn("firefox")),

    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -D pulse sset Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -D pulse sset Master 5%+")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -D pulse sset Master toggle")),

    #Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 10%+")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]

# ================================
# Definimos los espacios de trabajo
# ================================ 
def init_group_names():
    return [("", {'layout': 'max'}),
            ("", {'layout': 'max'}),
            ("", {'layout': 'max'}),
            ("", {'layout': 'max'}),
            ("", {'layout': 'max'})]

def init_groups():
    return [Group(name, **kwargs) for name, kwargs in group_names]

if __name__ in ["config", "__main__"]:
    group_names = init_group_names()
    groups = init_groups()

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))

# ================================
# Definimos los layouts en que se puede dividir la pantalla
# ================================

layouts = [
    layout.Max(),
    layout.Stack(margin = 2, num_stacks=2, border_focus = "#08b8df"),
    # Try more layouts by unleashing below layouts.
    layout.Bsp(margin=2, border_focus = "#08b8df"),
    # layout.Columns(),
    # layout.Matrix(),
    layout.MonadTall(margin = 2, border_focus = "#08b8df"),
    layout.MonadWide(margin = 2, border_focus = "#08b8df"),
    # layout.RatioTile(),
    # layout.Tile(), nt
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
	float_rules=[
	    # Run the utility of `xprop` to see the wm class and name of an X client.
	    {'wmclass': 'confirm'},
	    {'wmclass': 'dialog'},
	    {'wmclass': 'download'},
	    {'wmclass': 'error'},
	    {'wmclass': 'file_progress'},
	    {'wmclass': 'notification'},
	    {'wmclass': 'splash'},
	    {'wmclass': 'toolbar'},
	    {'wmclass': 'confirmreset'},  # gitk
	    {'wmclass': 'makebranch'},  # gitk
	    {'wmclass': 'maketag'},  # gitk
	    {'wname': 'branchdialog'},  # gitk
	    {'wname': 'pinentry'},  # GPG key password entry
	    {'wmclass': 'ssh-askpass'},  # ssh-askpass
	],
	    # border_focus = "colors"
)
auto_fullscreen = True
focus_on_window_activation = "smart"


# ================================
# Definimos los los widgets de la barra
# ================================
widget_defaults = dict(
    font='sans',
    fontsize=13,
    padding=3,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        # outis -> change button for topASA
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_method = "line",
                    birderwdth = -2,
                    highlight_color = "#000000",
                    rounded = False,
                    active = "#1234EF",
                    inactive  = "#707880",
                    center_aligned = True,
                    fontsize = 15
                ),
                widget.Prompt(
                    prompt = "Run:",
                ),
                widget.TextBox(
                    text = '',
                    foreground="#bf6a6a",
                    fontsize = 15
                ),

                widget.Spacer(bar.STRETCH),
                
                widget.Systray(),
                
                widget.TextBox(
                    text='',
                    foreground="bf6a6a",
                ),
                widget.Net(
                    foreground="bf6a6a",
                    #interface="wlp3s0",
                    format="↓{down}",
                ),
                widget.TextBox(
                    text='',
                    foreground="8fbcbb",
                ),
                widget.KeyboardLayout(
                    foreground="8fbcbb",
                    configured_keyboards="LATAM"
                ),
                
                widget.TextBox(
                    text='',
                    foreground="5e81ac",
                ),
                
                widget.Battery(
                    format = '{percent:2.0%}',
                    foreground = '5e81ac',
                ),
                
                widget.TextBox(
                    text='墳',
                    foreground="ebcb8b",
                ),
                
                widget.Volume(
                    foreground="ebcb8b",
                ),
                widget.TextBox(
                    text='',
                    foreground="88c0d0",
                ),

                widget.Backlight(
                    foreground="88c0d0",
                    backlight_name="intel_backlight",
                ),
                widget.TextBox(
                    text='',
                    foreground="a3be8c",
                ),
                widget.Clock(
                    format='%a %d  %H:%M:%S',
                    foreground = "a3be8c",
                ),
            ], 
            26, 
            background="2e3440"
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False


