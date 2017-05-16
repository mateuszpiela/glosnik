#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial
import dbus
from time import sleep
connected = False

try:
	conn = serial.Serial('/dev/ttyACM0', 9600);
	sleep(5)
	connected = True
	print("Połączono z Arduino ")
	print("Autor: Mateusz Pieła ")
	print("Wersja: 0.0.3 B+")
except:
	print("Nie połączono ;-;")
	
while connected:
	inputValue = (conn.readline()[:-2])
	bus = dbus.SessionBus()
	vlc_dbus = dbus.SessionBus().get_object('org.mpris.MediaPlayer2.vlc', '/org/mpris/MediaPlayer2')
	mpris='org.mpris.MediaPlayer2'
	player = dbus.Interface(vlc_dbus, mpris + '.Player')
	tracklist_pl = dbus.Interface(vlc_dbus, mpris + '.TrackList')
	muzyka_katalog = '/home/mateusz/Muzyka/'
	error_notimplemented = "Jeszcze tej funkcji nie zaimplementowano"
	if inputValue == '9':
		print(error_notimplemented)
		pass
	elif inputValue == '8':
		print(error_notimplemented)
		pass
	elif inputValue == '7':
		print(error_notimplemented)
		pass
	elif inputValue == '6':
		print(error_notimplemented)
		pass
	elif inputValue == '5':
		print(error_notimplemented)
		pass
	elif inputValue == '4':
		print(error_notimplemented)
		pass
	elif inputValue == '3':
		print(error_notimplemented)
		pass
	elif inputValue == '2':
		print("Otwieram Katalog SoundTrack")
		tracklist_pl.AddTrack('directory://' + muzyka_katalog + 'soundtrack','/',True)
		pass
	elif inputValue == '1':
		print("Otwieram Katalog Pop")
		tracklist_pl.AddTrack('directory://' + muzyka_katalog + 'pop','/',True)
		pass
	elif inputValue == '0':
		print("Odpalam VISTA")
		tracklist_pl.AddTrack('file://' + '/usr/share/sounds/ubuntu/stereo/system-ready.ogg','/',True)
		pass
	elif inputValue == '100+':
		print("Otwieram Katalog Demonstracyjny")
		tracklist_pl.AddTrack('directory://' + '/home/mateusz/Muzyka/demo','/',True)
		pass
	elif inputValue == '200+':
		print("Otwieram Katalog Anime")
		tracklist_pl.AddTrack('directory://' + muzyka_katalog + 'anime','/',True)
		pass
	elif inputValue == 'vol-':
		property_interface = dbus.Interface(player, dbus_interface='org.freedesktop.DBus.Properties')
		volume = property_interface.Get('org.mpris.MediaPlayer2.Player', 'Volume')
		property_interface.Set('org.mpris.MediaPlayer2.Player', 'Volume', volume-0.1)
		pass
	elif inputValue == 'vol+':
		property_interface = dbus.Interface(player, dbus_interface='org.freedesktop.DBus.Properties')
		volume = property_interface.Get('org.mpris.MediaPlayer2.Player', 'Volume')
		property_interface.Set('org.mpris.MediaPlayer2.Player', 'Volume', volume+0.1)
		pass
	elif inputValue == 'eq':
		property_interface = dbus.Interface(player, dbus_interface='org.freedesktop.DBus.Properties')
		volume = property_interface.Get('org.mpris.MediaPlayer2.Player', 'Volume')
		property_interface.Set('org.mpris.MediaPlayer2.Player', 'Volume', volume-1.0)
		pass
	elif inputValue == 'prev':
		player.Previous()
		pass
	elif inputValue == 'next':
		player.Next()
		pass
	elif inputValue == 'playandpause':	
		player.PlayPause()
		pass
	elif inputValue == 'ch-':
		print("Uruchramiam RMF FM ")
		tracklist_pl.AddTrack('http://' + '31.192.216.5/RMFFM48','/',True)
		pass
	elif inputValue == 'ch':
		print("Uruchramiam Vanessa FM")
		tracklist_pl.AddTrack('http://' + 'vanessa.fm/RV_online.m3u','/',True)
		pass
	elif inputValue == 'ch+':
		print("Uruchramiam Tuba FM")
		tracklist_pl.AddTrack('http://' + 'poznan5-6.radio.pionier.net.pl:8000/tuba9-1.mp3','/',True)
		pass
