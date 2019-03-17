import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
from button import Button
import game_functions as gf #well, i have no gf ...


def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	# screen = pygame.display.set_mode((1200, 800))
	pygame.display.set_caption("alien invasion")

	#创建用于存储游戏统计信息的实例
	stats = GameStats(ai_settings)
	#创建每一艘飞船
	ship = Ship(ai_settings, screen)
	#创建一艘飞船，一个子弹、一个外星人的编组
	bullets = Group()
	aliens = Group()

	#创建外星人群
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	#创建play按钮
	play_button  = Button(ai_settings, screen, "play")

	#开始游戏主循环
	while  True:
		gf.check_events(ai_settings, screen,stats,play_button, ship, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			# bullets.update()
			gf.update_aliens(ai_settings, stats, screen,ship , aliens, bullets)

			#每次循环时重绘屏幕
		gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets,
			play_button)
	

run_game()