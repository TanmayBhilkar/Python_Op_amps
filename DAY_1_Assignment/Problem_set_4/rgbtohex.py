  def hex_to_rgb(value):
        value = value.lstrip('#')
   t = len(value)
    return tuple(int(value[i:i+lv/3], 16) for i in range(0, t, t/3))
  hex_to_rgb("FFFFFF")

  def rgb_to_hex(rgb):
   return '%02x%02x%02x' % rgb
   rgb_to_hex((255, 255, 255))
   'ffffff'