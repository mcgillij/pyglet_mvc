'''
Created on Jul 23, 2012

@author: mcgillij
'''
import cocos
from cocos.layer import Layer
from cocos.actions import *
import pyglet

class HelloWorld(Layer):
    def __init__(self):
        super(HelloWorld, self).__init__()
        label = cocos.text.Label('Hi', font_name='Times New Roman', font_size=32, anchor_x='center', anchor_y='center')
        label.position = 320, 240
        self.add(label)
        sprite = cocos.sprite.Sprite('player_walk2.png')
        sprite.position = 320, 240
        self.scale = 3
        self.add(sprite, z=1)
        scale = ScaleBy(3, duration=2)
        label.do( Repeat ( scale + Reverse ( scale )))
        sprite.do( Repeat( Reverse(scale) + scale))
        self.do( RotateBy (360, duration=10))

class KeyDisplay(Layer):
    is_event_handler = True
    def __init__(self):
        super(KeyDisplay, self).__init__()
        self.text = cocos.text.Label("", x=100, y=280)
        self.keys_pressed = set()
        self.update_text()
        self.add(self.text)

    def update_text(self):
        key_names = [pyglet.window.key.symbol_string (k) for k in self.keys_pressed]
        text = 'Keys: ' + ','.join(key_names)
        self.text.element.text = text

    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)
        self.update_text()

    def on_key_release(self, key, modifiers):
        self.keys_pressed.remove(key)
        self.update_text()

class MouseDisplay(Layer):
    is_event_handler = True
    def __init__(self):
        super(MouseDisplay, self).__init__()
        self.posx = 100
        self.posy = 240
        self.text = cocos.text.Label('No mouse events yet', font_size=18, x=self.posx, y=self.posy)
        self.add(self.text)

    def update_text(self, x, y):
        text = 'Mouse @ %d, %d' % (x, y)
        self.text.element.text = text
        self.text.element.x = self.posx
        self.text.element.y = self.posy

    def on_mouse_press(self, x, y, buttons, modifiers):
        self.posx, self.posy = cocos.director.director.get_virtual_coordinates(x, y)
        self.update_text(x, y)

    def on_mouse_motion(self, x, y, dx, dy):
        self.update_text(x, y)

if __name__ == '__main__':
    cocos.director.director.init()
    main_scene = cocos.scene.Scene(HelloWorld(), KeyDisplay(), MouseDisplay())
    cocos.director.director.run(main_scene)