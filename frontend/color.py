# store a color with red, green, blue value
rgb = tuple[int, int, int]


# --- COLOR LIST --- #
WHITE : rgb = (255, 255, 255)
BLACK : rgb = (0, 0, 0)
GRAY : rgb = (128, 128, 128)
LIGHT_GRAY : rgb = (180, 180, 180)
DARK_GRAY : rgb = (60, 60, 60)
TERMINAL_BLACK : rgb = (30, 30, 30)

CYAN  : rgb = (94, 255, 252)
LIGHT_BLUE : rgb = (94, 185, 255)
DARK_BLUE : rgb = (0, 81, 143)
RAW_BLUE : rgb = (0, 0, 255)
LIGHT_PURPLE : rgb = (196, 162, 245)

RED : rgb = (217, 51, 46)
PINK: rgb = (250, 90, 122)
ORANGE : rgb = (247, 130, 94)
YELLOW : rgb = (255, 215, 0)

NEON : rgb = (187, 255, 0)
LIGHT_GREEN : rgb = (114, 199, 34)
GREEN : rgb = (33, 117, 0)
EMERALD: rgb = (75, 191, 117)



def lerp_color(c1, c2, t) -> rgb:
    return tuple(round(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

# Get color reperesentation of a temperature
def get_temperature_color(temp_C: float) -> rgb:
    gradient = [
        (-20, (0, 64, 255)),      # Blue
        (0,   (135, 206, 250)),   # Light blue
        (15,  (100, 200, 100)),   # Soft green
        (25,  (255, 240, 120)),   # Warm yellow
        (30,  (255, 180, 80)),    # Orange
        (40,  (255, 70, 70))      # Red
    ]

    if temp_C <= gradient[0][0]:
        return gradient[0][1]
    if temp_C >= gradient[-1][0]:
        return gradient[-1][1]

    for i in range(len(gradient) - 1):
        t1, c1 = gradient[i]
        t2, c2 = gradient[i + 1]
        if t1 <= temp_C <= t2:
            ratio = (temp_C - t1) / (t2 - t1)
            r = int(c1[0] + (c2[0] - c1[0]) * ratio)
            g = int(c1[1] + (c2[1] - c1[1]) * ratio)
            b = int(c1[2] + (c2[2] - c1[2]) * ratio)
            return (r, g, b)
        
    return LIGHT_BLUE

# Color representation of a precipitation value
def get_precip_color(mm: float) -> rgb:
    points = [
        (0.0,  (160, 200, 255)),  # Very light blue
        (1.5, (100, 160, 255)),   # Blue
        (3.0, (0, 200, 200)),     # Cyan
        (7.0, (0, 220, 0)),       # Green
        (10.0, (255, 255, 0)),    # Yellow
        (20.0, (255, 0, 100)),    # Red-pink
        (30.0, (200, 0, 255)),    # Magenta-purple
    ]

    if mm <= points[0][0]:
        return points[0][1]
    if mm >= points[-1][0]:
        return points[-1][1]

    for i in range(1, len(points)):
        if mm <= points[i][0]:
            low_mm, low_color = points[i - 1]
            high_mm, high_color = points[i]
            t = (mm - low_mm) / (high_mm - low_mm)
            return lerp_color(low_color, high_color, t)

    return points[-1][1]  # Fallback

