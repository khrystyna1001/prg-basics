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
   tv1.decrease_volume()
   print(tv1.show_status())

   tv1.turn_off()
   print(tv1.show_status())

if __name__ == "__main__":
   main() 
