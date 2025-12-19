import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# -----------------------------
# Configuration
# -----------------------------
LABELS = [
    "Facebook.com", "Suno.ai", "Genmo.ai", "app.pixverse.ai",
    "chatgpt.com", "tunee.ai", "fables.gg", "ideogram.ai",
    "github.com", "rocking.gr", "blabbermouth.net", "soundcloud.com"
]

FIG_SIZE = (40, 40)
RADIUS_OUTER = 1.0
RADIUS_TEXT = 0.85
RADIUS_HOUR_HAND = 0.5
RADIUS_MIN_HAND = 0.75


# -----------------------------
# Utility
# -----------------------------
def polar_to_cartesian(radius, angle_deg):
    angle_rad = np.deg2rad(angle_deg)
    return radius * np.cos(angle_rad), radius * np.sin(angle_rad)


# -----------------------------
# Main drawing function
# -----------------------------
def draw_os_clock():
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    ax.set_aspect("equal")
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.axis("off")

    # Outer circle
    ax.add_artist(
        plt.Circle((0, 0), RADIUS_OUTER, fill=False, linewidth=2, alpha=0.8)
    )

    # Hour markers
    for i in range(12):
        angle = 90 - i * 30
        x1, y1 = polar_to_cartesian(0.95, angle)
        x2, y2 = polar_to_cartesian(1.0, angle)
        ax.plot([x1, x2], [y1, y2], linewidth=1, alpha=0.6)

    # Labels
    for i, label in enumerate(LABELS):
        angle = 90 - i * 30
        x, y = polar_to_cartesian(RADIUS_TEXT, angle)
        ax.text(
            x, y, label,
            ha="center", va="center",
            fontsize=9,
            fontweight="semibold"
        )

    # Current time
    now = datetime.now()
    hour = (now.hour % 12) + now.minute / 60
    minute = now.minute

    # Hour hand
    hx, hy = polar_to_cartesian(RADIUS_HOUR_HAND, 90 - hour * 30)
    ax.plot([0, hx], [0, hy], linewidth=3, color="#d62828", label="Hour")

    # Minute hand
    mx, my = polar_to_cartesian(RADIUS_MIN_HAND, 90 - minute * 6)
    ax.plot([0, mx], [0, my], linewidth=2, color="#003049", label="Minute")

    # Center cap
    ax.scatter(0, 0, s=40, color="black", zorder=5)

    # Title & legend
    ax.set_title("Games Clock", fontsize=15, fontweight="bold", pad=15)
    ax.legend(loc="lower right", frameon=False)

    plt.show()


draw_os_clock()

