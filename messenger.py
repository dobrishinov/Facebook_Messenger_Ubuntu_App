#!/usr/bin/python 
# -*- coding: utf-8 -*- 
 
from gi.repository import Gtk, WebKit 

builder = Gtk.Builder() 
builder.add_from_file("ui.glade") 
 
window = builder.get_object("window") 

browserholder = WebKit.WebView() 
 
browserholder.set_editable(False) 
 
browserholder.load_uri("http://messenger.com/t")

scrolled_window = builder.get_object("scrolledwindow") 
 
scrolled_window.add(browserholder) 

browserholder.show() 
 
window.connect("delete-event", Gtk.main_quit) 
window.show_all() 
Gtk.main()
