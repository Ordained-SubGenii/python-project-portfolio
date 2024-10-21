import python_avatars as pa
my_avatar = pa.Avatar(
    style=pa.AvatarStyle.CIRCLE,
    background_color=pa.BackgroundColor.WHITE,
    top=pa.HairType.SHAGGY,
    eyebrows=pa.EyebrowType.DEFAULT_NATURAL,
    eyes=pa.EyeType.SIDE,
    nose=pa.NoseType.DEFAULT,
    mouth=pa.MouthType.SMILE,
    facial_hair=pa.FacialHairType.BEARD_MEDIUM,
    # You can use hex colors on any color attribute...
    skin_color="#F19EC2",
    # Or you can use the colors provided by the library
    hair_color=pa.HairColor.BROWN,
    accessory=pa.AccessoryType.SUNGLASSES,
    clothing=pa.ClothingType.JEDI_ROBE,
    clothing_color=pa.ClothingColor.HEATHER
)
# Save to a file
my_avatar.render("my_avatar.svg")


