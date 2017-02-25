import urwid
def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

pallet = [
    ('banner', 'black', 'light gray'),
    ('streak', 'dark red', 'dark red'),
    ('bg', 'black', 'dark blue'),]

txt = urwid.Text(('banner', u"Hi"), align='center')
map1= urwid.AttrMap(txt, 'streak')
fill = urwid.Filler(map1)
map2 = urwid.AttrMap(fill, 'bg')
loop = urwid.MainLoop(map2, pallet, unhandled_input=exit_on_q)
loop.run()
