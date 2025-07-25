from .terminal import Terminal

SUN_COLOR   = (255, 183,  15)
CLOUD_COLOR = (176, 217, 255)
RAIN_COLOR  = (  6, 102, 212)
SNOW_COLOR  = (105, 175, 255)
LIGHTNING   = (255, 185,  33)
FOG_COLOR   = (188, 189, 187)

def get_icon(terminal: Terminal, x: int | None = None, y: int | None = None, code: int | None = None) -> None:
    x = x if (x is not None) else terminal.cursorX
    y = y if (y is not None) else terminal.cursorY

    terminal.move_cursor(x, y)
    # Clear sky
    if (code == 0):
        terminal.print("    \\   /    ", x=x, foregr=SUN_COLOR)
        terminal.print("     .-.     ",  x=x, foregr=SUN_COLOR)
        terminal.print(" -- (   ) -- ",  x=x, foregr=SUN_COLOR)
        terminal.print("     `-`     ",  x=x, foregr=SUN_COLOR)
        terminal.print("    /   \\    ", x=x, foregr=SUN_COLOR)
    # Mainly clear / Partly clear
    elif (code == 1 or code == 2):
        terminal.print("             ", x=x, foregr=CLOUD_COLOR)
        terminal.print("    \\  /    ", x=x, foregr=SUN_COLOR)
        terminal.print(" __ /\"\"",     x=x, foregr=SUN_COLOR, end='')
        terminal.print(".-.     ",           foregr=CLOUD_COLOR)
        terminal.print("    \\_",       x=x, foregr=SUN_COLOR, end='')
        terminal.print("(   )   ",           foregr=CLOUD_COLOR)
        terminal.print("   / ",         x=x, foregr=SUN_COLOR, end='')
        terminal.print("(__(__)   ",         foregr=CLOUD_COLOR)

    # Overcast
    elif (code == 3):
        terminal.print("              ", x=x, foregr=CLOUD_COLOR)
        terminal.print("     .--.     ", x=x, foregr=CLOUD_COLOR)
        terminal.print("  .-(    ).   ", x=x, foregr=CLOUD_COLOR)
        terminal.print(" (___.__)__)  ", x=x, foregr=CLOUD_COLOR)
        terminal.print(" (_____.____) ", x=x, foregr=CLOUD_COLOR)

    # Fog and depositing rime fog
    elif (code == 45 or code == 48):
        terminal.print("     .--.    ", x=x, foregr=CLOUD_COLOR)
        terminal.print("  .-(    ).  ", x=x, foregr=CLOUD_COLOR)
        terminal.print(" (_.__.__._) ", x=x, foregr=CLOUD_COLOR)
        terminal.print("  ~~ ~~~ ~~  ", x=x, foregr=FOG_COLOR)
        terminal.print("  ~~~ ~ ~~~  ", x=x, foregr=FOG_COLOR)

    # Light drizzle
    elif (code == 51):        
        terminal.print("     .--.    ", x=x, foregr=CLOUD_COLOR)
        terminal.print("  .-(    ).  ", x=x, foregr=CLOUD_COLOR)
        terminal.print(" (___.__)__) ", x=x, foregr=CLOUD_COLOR)
        terminal.print("  .   .   ,  ", x=x, foregr=RAIN_COLOR)
        terminal.print("  ,  .  ,    ", x=x, foregr=RAIN_COLOR)

    # Moderate drizzle
    elif (code == 53):        
        terminal.print("     .--.    ", x=x, foregr=CLOUD_COLOR)
        terminal.print("  .-(    ).  ", x=x, foregr=CLOUD_COLOR)
        terminal.print(" (___.__)__) ", x=x, foregr=CLOUD_COLOR)
        terminal.print("  , .   , .  ", x=x, foregr=RAIN_COLOR)
        terminal.print(" .   .   .   ", x=x, foregr=RAIN_COLOR)
        
    # Dense drizzle
    elif (code == 55):        
        terminal.print("     .--.    ", x=x, foregr=CLOUD_COLOR)
        terminal.print("  .-(    )-. ", x=x, foregr=CLOUD_COLOR)
        terminal.print(" (_.___.),__)", x=x, foregr=CLOUD_COLOR)
        terminal.print("  , . , . ,  ", x=x, foregr=RAIN_COLOR)
        terminal.print(" . , . , .   ", x=x, foregr=RAIN_COLOR)

    # Light rain
    elif (code == 61):        
        terminal.print("     .--.    ", x=x, foregr=CLOUD_COLOR)
        terminal.print("  .-(    ).  ", x=x, foregr=CLOUD_COLOR)
        terminal.print(" (___.__)__) ", x=x, foregr=CLOUD_COLOR)
        terminal.print(" ,  .  ,  ,  ", x=x, foregr=RAIN_COLOR)
        terminal.print("  ,  ,  .    ", x=x, foregr=RAIN_COLOR)

    # Moderate rain / Moderate rain shower
    elif (code == 63 or code == 81):        
        terminal.print("     .--.    ", x=x, foregr=CLOUD_COLOR)
        terminal.print("  .-(    ).  ", x=x, foregr=CLOUD_COLOR)
        terminal.print(" (___.__)__) ", x=x, foregr=CLOUD_COLOR)
        terminal.print("  ‘ , ‘ , ‘  ", x=x, foregr=RAIN_COLOR)
        terminal.print(" ‘ , ‘ , ‘   ", x=x, foregr=RAIN_COLOR)

    # Heavy rain / Violent rain shower
    elif (code == 65 or code == 82):
        terminal.print("     .--.    ", x=x, foregr=CLOUD_COLOR)
        terminal.print("  .-(    )-. ", x=x, foregr=CLOUD_COLOR)
        terminal.print(" (___.__)___)", x=x, foregr=CLOUD_COLOR)
        terminal.print("  , / / , ‘  ", x=x, foregr=RAIN_COLOR)
        terminal.print(" / / ‘ / /   ", x=x, foregr=RAIN_COLOR)

    # Light freezing rain
    elif (code == 66):
        terminal.print("     .--.    ", x=x, foregr=CLOUD_COLOR)
        terminal.print("  .-(    )-. ", x=x, foregr=CLOUD_COLOR)
        terminal.print(" (___.__)___)", x=x, foregr=CLOUD_COLOR)
        terminal.print("  ,  *  ,  , ", x=x, foregr=RAIN_COLOR)
        terminal.print("   ,  ,  *   ", x=x, foregr=RAIN_COLOR)

    # Heavy freezing rain
    elif (code == 67):
        terminal.print("     .--.    ", x=x, foregr=CLOUD_COLOR)
        terminal.print("  .-(    )-. ", x=x, foregr=CLOUD_COLOR)
        terminal.print(" (___.__)___)", x=x, foregr=CLOUD_COLOR)
        terminal.print("  / * / , *  ", x=x, foregr=RAIN_COLOR)
        terminal.print(" * / , * /   ", x=x, foregr=RAIN_COLOR)

    # Slight snow
    elif (code == 71):
        terminal.print("     .--.    ", x=x, foregr=CLOUD_COLOR)
        terminal.print("  .-(    ).  ", x=x, foregr=CLOUD_COLOR)
        terminal.print(" (___.__)__) ", x=x, foregr=CLOUD_COLOR)
        terminal.print(" *  .  *  .  ", x=x, foregr=SNOW_COLOR)
        terminal.print("   *  .  *   ", x=x, foregr=SNOW_COLOR)

    # Moderate snow
    elif (code == 73):
        terminal.print("     .--.    ", x=x, foregr=CLOUD_COLOR)
        terminal.print("  .-(    ).  ", x=x, foregr=CLOUD_COLOR)
        terminal.print(" (___.__)__) ", x=x, foregr=CLOUD_COLOR)
        terminal.print(" . *  .  * . ", x=x, foregr=SNOW_COLOR)
        terminal.print("  * . * . *  ", x=x, foregr=SNOW_COLOR)

    # Heavy snow  / Heavy snow shower
    elif (code == 75 or code == 86):
        terminal.print("     .--.    ", x=x, foregr=CLOUD_COLOR)
        terminal.print("  .-(    ).  ", x=x, foregr=CLOUD_COLOR)
        terminal.print(" (___.__)__) ", x=x, foregr=CLOUD_COLOR)
        terminal.print("  * * * * *  ", x=x, foregr=SNOW_COLOR)
        terminal.print(" * * * * *   ", x=x, foregr=SNOW_COLOR)

    # Snow grains
    elif (code == 77):
        terminal.print("     .--.    ", x=x, foregr=CLOUD_COLOR)
        terminal.print("  .-(    ).  ", x=x, foregr=CLOUD_COLOR)
        terminal.print(" (___.__)__) ", x=x, foregr=CLOUD_COLOR)
        terminal.print("  * • * * •  ", x=x, foregr=SNOW_COLOR)
        terminal.print(" • * * • *   ", x=x, foregr=SNOW_COLOR)


    # Light rain shower
    elif (code == 80):
        terminal.print(" _`/\"\"",      x=x, foregr=SUN_COLOR, end='')
        terminal.print(".-.    ",            foregr=CLOUD_COLOR)
        terminal.print("  ,\\_",        x=x, foregr=SUN_COLOR, end='')
        terminal.print("(   ).  ",           foregr=CLOUD_COLOR)
        terminal.print("   /",          x=x, foregr=SUN_COLOR, end='')
        terminal.print("(___(__) ",          foregr=CLOUD_COLOR)
        terminal.print("    , ‘ , ‘  ", x=x, foregr=RAIN_COLOR)
        terminal.print("   , ‘ , ‘   ", x=x, foregr=RAIN_COLOR)

    # Light snow shower
    elif (code == 85):
        terminal.print(" _`/\"\"",      x=x, foregr=SUN_COLOR, end='')
        terminal.print(".-.    ",            foregr=CLOUD_COLOR)
        terminal.print("  ,\\_",        x=x, foregr=SUN_COLOR, end='')
        terminal.print("(   ).  ",           foregr=CLOUD_COLOR)
        terminal.print("   /",          x=x, foregr=SUN_COLOR, end='')
        terminal.print("(___(__) ",          foregr=CLOUD_COLOR)
        terminal.print("    * . * .  ", x=x, foregr=RAIN_COLOR)
        terminal.print("   . * . *   ", x=x, foregr=RAIN_COLOR)
 
    # Slight or moderate thunderstorm
    elif (code == 95):
        terminal.print("     .--.    ", x=x, foregr=CLOUD_COLOR)
        terminal.print("  ,-(    )-. ", x=x, foregr=CLOUD_COLOR)
        terminal.print(" (___,__)___)", x=x, foregr=CLOUD_COLOR)
        terminal.print("  ‘ ‘",         x=x, foregr=RAIN_COLOR, end='')
        terminal.print("_//",                foregr=LIGHTNING, end='')
        terminal.print(" ‘ ‘ ",              foregr=RAIN_COLOR)
        terminal.print(" ‘",            x=x, foregr=RAIN_COLOR, end='')
        terminal.print(" //",                foregr=LIGHTNING, end='')
        terminal.print(" ‘ ‘ ‘",             foregr=RAIN_COLOR)

    # Thunderstorm with slight and heavy hail
    elif (code == 96 or code == 97):
        terminal.print("     .--.    ", x=x, foregr=CLOUD_COLOR)
        terminal.print("  ,-(    )-. ", x=x, foregr=CLOUD_COLOR)
        terminal.print(" (___,__)___)", x=x, foregr=CLOUD_COLOR)
        terminal.print("  . ",          x=x, foregr=FOG_COLOR, end='')
        terminal.print("__//",               foregr=LIGHTNING, end='')
        terminal.print(" o . ",              foregr=FOG_COLOR)
        terminal.print(" o",            x=x, foregr=FOG_COLOR, end='')
        terminal.print(" //",                foregr=LIGHTNING, end='')
        terminal.print(" o . o",             foregr=FOG_COLOR)

    else:
        terminal.print("     .--.    ", x=x, foregr=CLOUD_COLOR)
        terminal.print("  .-(    ).  ", x=x, foregr=CLOUD_COLOR)
        terminal.print(" (___.__)__) ", x=x, foregr=CLOUD_COLOR)
        terminal.print("  │unknown│  ", x=x, foregr=(252, 83, 71))
        terminal.print("  │weather│  ", x=x, foregr=(252, 83, 71))