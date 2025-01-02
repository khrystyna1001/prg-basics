class TV:
   def __init__(self):
      self.is_on = False
      self.channel_no = 1
      self.channels = []
      self.volume = 0
   def turn_off(self):
      self.is_on = False
   def turn_on(self):
      self.is_on = True
   def set_volume(self, volume):
      if volume >= 0 and volume <= 10:
          self.volume = volume
   def increase_volume(self):
      if self.volume + 1 >= 0 and self.volume + 1 <= 10:
          self.volume += 1
   def decrease_volume(self):
      if self.volume - 1 >= 0 and self.volume - 1 <= 10:
          self.volume -= 1
   def show_volume(self):
      return f'Volume: {self.volume}'
   def set_channel(self, channel):
      self.channel_no = channel
   def set_channels(self, channels_list):
      self.channels = channels_list
   def show_channels(self):
      for i, item in enumerate(self.channels):
         print(f'{i+1}. {item}')
   def show_status(self):
      if self.is_on:
         if self.channels:
            return f'TV is on, channel {self.channel_no}: {self.channels[self.channel_no - 1]} volume: {self.volume}'
         else:
            return f'TV is on but no channels available'
      else:
         return 'TV is off'