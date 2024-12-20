import tv_show

def main():
   # object creation
   tv1 = tv_show.TV()

   # object usage
   print(tv1.show_status())
   tv1.turn_on()
   print(tv1.show_status())
   tv1.show_channels()
   tv1.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Discovery'])
   tv1.show_channels()
   print(tv1.show_volume())
   tv1.increase_volume()
   print(tv1.show_volume())
   tv1.set_volume(9)
   print(tv1.show_volume())
   tv1.set_channel(4)
   print(tv1.show_status())

   tv1.turn_off()
   print(tv1.show_status())

if __name__ == "__main__":
   main() 

# In the TV class, add support for volume adjustment in the range 0 to 10. The initial value of the volume level is 0. Add two methods to increase and decrease the TV volume 
# level by one. Note that you cannot increase or decrease the volume beyond the specified range.
#  Display the current volume level in the show_status() method. Then check the operation of the TV by adjusting and displaying its volume level.