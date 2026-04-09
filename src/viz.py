"""
Shared visualization helpers for Polutka Lab.

Dark theme constants, Instagram composition, and radar chart utilities.
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# ═══════════════════════════════════════════════════════════════════════════════
# DARK THEME COLOR PALETTE
# ═══════════════════════════════════════════════════════════════════════════════
BG_COLOR    = '#0a0a0a'
GOLD        = '#d4af37'
ACCENT      = '#f6c453'
BLUE        = '#3498db'
GREEN       = '#27ae60'
RED         = '#e05c5c'
TEXT_WHITE  = '#FFFFFF'
TEXT_GREY   = '#A0A0A0'
GRID_COLOR  = '#1f2a3a'
PANEL_COLOR = '#0f1722'
LINE_COLOR  = '#1f2a3a'
HIGHLIGHT   = '#17324a'

# ═══════════════════════════════════════════════════════════════════════════════
# INSTAGRAM POST COMPOSITION
# ═══════════════════════════════════════════════════════════════════════════════
INSTAGRAM_SIZE = (1080, 1350)


def compose_instagram_post(
    chart_path: Path,
    output_path: Path,
    assets_dir: Path,
    chart_width: int = 1000,
    y_shift: int = 30,
) -> Image.Image:
    """
    Overlay a transparent chart onto the Instagram background template.

    Parameters
    ----------
    chart_path : Path to the chart PNG (transparent background).
    output_path : Path to save the final 1080×1350 post.
    assets_dir : Directory containing background.png (and optionally pfp.png).
    chart_width : Target width for the chart (height scales proportionally).
    y_shift : Vertical offset from center (positive = down).

    Returns the composed RGBA image.
    """
    bg_path = assets_dir / 'background.png'
    if bg_path.exists():
        background = Image.open(bg_path).convert('RGBA')
        if background.size != INSTAGRAM_SIZE:
            background = background.resize(INSTAGRAM_SIZE, Image.Resampling.LANCZOS)
    else:
        background = Image.new('RGBA', INSTAGRAM_SIZE, BG_COLOR)

    chart = Image.open(chart_path).convert('RGBA')
    chart_h = int(chart.height * (chart_width / chart.width))
    chart = chart.resize((chart_width, chart_h), Image.Resampling.LANCZOS)

    x_offset = (INSTAGRAM_SIZE[0] - chart_width) // 2
    y_offset = (INSTAGRAM_SIZE[1] - chart_h) // 2 + y_shift

    background.alpha_composite(chart, (x_offset, y_offset))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    background.convert('RGB').save(output_path, quality=95)
    return background


# ═══════════════════════════════════════════════════════════════════════════════
# RADAR CHART
# ═══════════════════════════════════════════════════════════════════════════════

def draw_radar(
    labels: list[str],
    values_main: list[float],
    values_compare: list[float],
    name_main: str,
    name_compare: str,
    color_main: str = ACCENT,
    color_compare: str = RED,
    save_path: Path | None = None,
) -> plt.Figure:
    """
    Draw a percentile radar chart comparing two players.

    Parameters
    ----------
    labels : Radar axis labels (supports \\n for multi-line).
    values_main : Percentile values (0–100) for the main player.
    values_compare : Percentile values (0–100) for the comparison player.
    name_main / name_compare : Legend labels.
    color_main / color_compare : Line/fill colours.
    save_path : If provided, saves the figure as a transparent PNG.

    Returns the matplotlib Figure.
    """
    N = len(labels)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]

    main_vals = list(values_main) + [values_main[0]]
    comp_vals = list(values_compare) + [values_compare[0]]

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True), dpi=100)
    fig.patch.set_alpha(0.0)
    ax.set_facecolor('none')
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    # Concentric ring fills
    ring_values = [20, 40, 60, 80, 100]
    ring_alphas = [0.06, 0.09, 0.12, 0.15, 0.18]
    for rv, ra in zip(ring_values, ring_alphas):
        ax.fill(np.linspace(0, 2 * np.pi, 200), [rv] * 200,
                color='#1a283d', alpha=ra, zorder=0)

    # Main player (on top)
    ax.plot(angles, main_vals, 'o-', linewidth=2.8, color=color_main,
            markersize=6, zorder=6, label=name_main)
    ax.fill(angles, main_vals, alpha=0.15, color=color_main, zorder=5)

    # Comparison player (behind)
    ax.plot(angles, comp_vals, 'o-', linewidth=2.8, color=color_compare,
            markersize=6, zorder=4, label=name_compare)
    ax.fill(angles, comp_vals, alpha=0.15, color=color_compare, zorder=3)

    # Labels & grid
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=13, color='#e8e8e8', fontweight='bold')
    ax.set_ylim(0, 100)
    ax.set_yticks(ring_values)
    ax.set_yticklabels([str(v) for v in ring_values], fontsize=8, color='#555555')
    ax.yaxis.grid(True, color='#2a2a2a', linewidth=0.5, linestyle='--')
    ax.xaxis.grid(True, color='#2a2a2a', linewidth=0.5)
    ax.spines['polar'].set_color('#2a2a2a')

    legend = ax.legend(
        loc='upper right', bbox_to_anchor=(1.05, 1.12),
        fontsize=13, fancybox=False, edgecolor='#333333',
        facecolor=BG_COLOR, labelcolor='#e8e8e8', framealpha=0.85,
        handlelength=1.8, handletextpad=0.8, labelspacing=0.6,
    )
    legend.get_frame().set_linewidth(1.0)

    plt.tight_layout()

    if save_path:
        save_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(save_path, dpi=100, transparent=True,
                    bbox_inches='tight', pad_inches=0.02)

    return fig
