from reel import *
from settings import *
import pygame

class Machine:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.reel_index = 0
        self.reel_list = {}
        self.can_toggle = True
        self.spinning = False
        self.can_animate = False

        self.spawn_reels()

        # Import sounds
        # self.spin_sound = pygame.mixer.Sound('audio/spinclip.mp3')
        # self.spin_sound.set_volume(0.15)
        # self.win_three = pygame.mixer.Sound('audio/winthree.wav')
        # self.win_three.set_volume(0.6)
        # self.win_four = pygame.mixer.Sound('audio/winfour.wav')
        # self.win_four.set_volume(0.7)
        # self.win_five = pygame.mixer.Sound('audio/winfive.wav')
        # self.win_five.set_volume(0.8)

    def cooldowns(self):
        # Only lets player spin if all reels are NOT spinning
        for reel in self.reel_list:
            if self.reel_list[reel].reel_is_spinning:
                self.can_toggle = False
                self.spinning = True

        if not self.can_toggle and [self.reel_list[reel].reel_is_spinning for reel in self.reel_list].count(False) == 5:
            self.can_toggle = True

    def input(self):
        keys = pygame.key.get_pressed()

        # Checks for space key, ability to toggle spin, and balance to cover bet size
        #  and self.can_toggle and self.currPlayer.balance >= self.currPlayer.bet_size:
        if keys[pygame.K_SPACE]:
            self.toggle_spinning()
            self.spin_time = pygame.time.get_ticks()
            # self.currPlayer.place_bet()
            # self.machine_balance += self.currPlayer.bet_size
            # self.currPlayer.last_payout = None
            
    def draw_reels(self, delta_time):
        for reel in self.reel_list:
            self.reel_list[reel].animate(delta_time)

    def spawn_reels(self):
        if not self.reel_list:
            x_topleft, y_topleft = 10, -300
        while self.reel_index < 5:
            if self.reel_index > 0:
                x_topleft, y_topleft = x_topleft + (300 + X_OFFSET), y_topleft
            
            self.reel_list[self.reel_index] = Reel((x_topleft, y_topleft)) # Need to create reel class
            self.reel_index += 1

    def toggle_spinning(self):
        if self.can_toggle:
            self.spin_time = pygame.time.get_ticks()
            self.spinning = not self.spinning
            self.can_toggle = False

            for reel in self.reel_list:
                self.reel_list[reel].start_spin(int(reel) * 200)
                # self.spin_sound.play()

    def update(self, delta_time):
        self.cooldowns()
        self.input()
        self.draw_reels(delta_time)
        for reel in self.reel_list:
            self.reel_list[reel].symbol_list.draw(self.display_surface)
            self.reel_list[reel].symbol_list.update()