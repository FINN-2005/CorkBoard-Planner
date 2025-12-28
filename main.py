from pygame_template import *


# buttons
BUTTONS = {
    'pan'  :  pygame.K_SPACE,
    'zoom' :  pygame.K_LCTRL        # not actually used
}
HELD = { butt : False for butt in BUTTONS.values() }


# cursors
GRABBY = pygame.Cursor(pygame.SYSTEM_CURSOR_HAND)
ARROW  = pygame.Cursor(pygame.SYSTEM_CURSOR_ARROW)


# paper
PAPER_COLS = (
    (230, 210, 124, 255),       # yellow
    (224, 224, 224, 255),       # white
    (237, 168, 111, 255),       # orange
    (126, 173, 230, 255),       # blue
    (176, 136, 207, 255),       # purple
    (138, 219, 134, 255),       # green
    (227, 148, 148, 255),       # red
)
PAPER_DEFAULT_SIZE = V2(300, 300)
PAPER_ANGLE_RANGE = ( -7.5, 7.5 )


# global defaults
OFFSET = V2()
ZOOM = 1.0



'''
More To Add:
    - paper-text class
    - paper-image class
    - paper-canvas class

    - bottomdrawer class
    - topdrawer class
    - floatingmenu class
    
    - right click menu (for options like copy, paste, cut, undo, redo, copy template, z ordering(layers), etc)
    - pins, strings
'''

'''
DONE:
    - camera zoom
'''



class Paper(Sprite):
    def __init__(self, 
                pos = V2(APP.HW, APP.HH),
                Ptype = 'text',

                *groups):
        super().__init__(*groups)
        '''
            Things like:
                - papers of random colours from a selection
                - slightly randomised tilting of the whole paper when pasted on the board
                - can drag out a page from the bottom overlay to put on the board
                - when creating a new page or when clicking an existing one to edit it:
                    - it should open a side panel which has all the properties to be messed with like colour, font stuff, text format, etc
                
                - three type of paper:
                    - text
                    - image
                    - drawing canvas
        '''

        self.type = Ptype
        
        self.pos = pos
        self.size = V2(PAPER_DEFAULT_SIZE)
        self.angle = random.uniform(*PAPER_ANGLE_RANGE)

        self.base = pygame.Surface(self.size, pygame.SRCALPHA)
        self.col = random.choice(PAPER_COLS)

        self.content = ...
        
        self.base.fill(self.col)
        pygame.draw.rect(self.base, Color.purple, (50,50,100,100), 10)      # fill in for the content

        self.rotated = pygame.transform.rotate(self.base, self.angle)

        self.zoom_level = None
        self.zoomed = None

    def draw(self, screen):
        if self.zoom_level != ZOOM:
            self.zoom_level = ZOOM
            self.zoomed = pygame.transform.scale_by(self.rotated, ZOOM)

        screen_pos = (self.pos - OFFSET) * ZOOM
        rect = self.zoomed.get_frect(center=screen_pos)

        screen.blit(self.zoomed, rect)




class Bottom_Drawer(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        '''
            when i drag my mouse to the bottom, it should show the paper / string / other element tray which i can drag and drop stuff from
        '''


class Top_Drawer(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        '''
            when i drag mouse to top of window, it shows the FILE, SETTINGS, HELP, thing
        '''


class Floating_Menu(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        '''
            has all the properties to be messed with like colour, font stuff, text format, etc
        '''
    

class Board(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        
        self.tile = pygame.image.load(join('cork.png')).convert_alpha()
        self.tile_size = V2(self.tile.size)

        self.image = pygame.Surface((APP.W, APP.H))
        self.rect = self.image.get_frect()

    def draw(self, screen):
        global OFFSET, ZOOM

        tw, th = self.tile_size
        sw, sh = screen.get_size()

        scaled_tw = int(round(tw * ZOOM))
        scaled_th = int(round(th * ZOOM))
        if scaled_tw <= 0 or scaled_th <= 0: return

        tile_img = pygame.transform.scale(self.tile, (scaled_tw, scaled_th))

        ox = -int((OFFSET.x * ZOOM) % scaled_tw)
        oy = -int((OFFSET.y * ZOOM) % scaled_th)

        x = ox
        while x < sw + scaled_tw:
            y = oy
            while y < sh + scaled_th:
                screen.blit(tile_img, (x, y))
                y += scaled_th
            x += scaled_tw




class run(APP):
    def init(self):
        # self.WIDTH, self.HEIGHT = 1920, 1080      # Uncomment to make 1080p fullscree
        # self.FULLSCREEN = True                    # comment to make 720p window
        ...

    def setup(self):
        self.board_group = Group(Board())       # cork board
        self.paper_group = Group(Paper())       # papers

    def draw(self):
        self.board_group.draw()
        self.paper_group.draw()

    def update(self):
        global OFFSET, ZOOM

        if HELD[BUTTONS['pan']]:
            dx, dy = pygame.mouse.get_rel()
            OFFSET -= V2(dx, dy) / ZOOM

        self.board_group.update()
        self.paper_group.update()

    def event(self, e):
        global ZOOM, OFFSET
        # pan
        if e.type == pygame.KEYDOWN:
            if e.key in HELD:
                HELD[e.key] = True
                if e.key == BUTTONS['pan']:
                    pygame.mouse.get_rel()      # flush accumulated values
                    pygame.mouse.set_cursor(GRABBY)
        elif e.type == pygame.KEYUP:
            if e.key in HELD:
                HELD[e.key] = False
                if e.key == BUTTONS['pan']:
                    pygame.mouse.set_cursor(ARROW)

        # zoom
        if e.type == pygame.MOUSEWHEEL:
            mpos = V2(pygame.mouse.get_pos())
            before = self.StW(mpos)

            s = 1.01
            ZOOM *= s if e.y > 0 else 1/s
            ZOOM = max(0.2, min(4.0, ZOOM))

            after = self.StW(mpos)
            OFFSET += before - after

        # spawn new paper
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            self.paper_group.add(Paper(self.StW(V2(e.pos))))



    def WtS(self, p): return (p - OFFSET) * ZOOM
    def StW(self, p): return V2(p) / ZOOM + OFFSET




run()