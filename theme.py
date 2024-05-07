import dearpygui.dearpygui as dpg

TRACKED_RESOURCES = {
    'Ale': {
        'color': [] # add color here
    },
    'Approval': {
        'color': [] # add color here
    },
    'Berries': {
        'color': [] # add color here
    },
    'Clay': {
        'color': [] # add color here
    },
    'Eggs': {
        'color': [] # add color here
    },
    'Firewood': {
        'color': [] # add color here
    },
    'Hides': {
        'color': [] # add color here
    },
    'Iron Ore': {
        'color': [] # add color here
    },
    'Leather': {
        'color': [] # add color here
    },
    'Meat': {
        'color': [] # add color here
    },
    'Planks': {
        'color': [] # add color here
    },
    'Regional Wealth': {
        'color': [] # add color here
    },
    'Roof Tiles': {
        'color': [] # add color here
    },
    'Stone': {
        'color': [] # add color here
    },
    'Timber': {
        'color': [] # add color here
    },
    'Vegetables': {
        'color': [] # add color here
    },
}

def setupGlobalAllRules():
    baseColor = [48, 55, 78]
    tileColor = [18, 23, 42]
    gridColor = [92, 92, 92]
    textColor = [195, 195, 195]

    # Frame + bgs
    dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 10, category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvPlotCol_FrameBg, tileColor, category=dpg.mvThemeCat_Plots)
    dpg.add_theme_color(dpg.mvPlotCol_PlotBg, tileColor, category=dpg.mvThemeCat_Plots)
    dpg.add_theme_color(dpg.mvThemeCol_FrameBg, tileColor, category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_WindowBg, baseColor, category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_ChildBg, tileColor, category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 10, category=dpg.mvThemeCat_Core)

    # Axis styling
    dpg.add_theme_color(dpg.mvPlotCol_PlotBorder, baseColor, category=dpg.mvThemeCat_Plots)

    # Font
    dpg.set_global_font_scale(1.2)
    dpg.add_theme_color(dpg.mvThemeCol_Text, textColor, category=dpg.mvThemeCat_Core)

    # Grid
    dpg.add_theme_style(dpg.mvPlotStyleVar_MinorGridSize, 3, category=dpg.mvThemeCat_Plots)
    dpg.add_theme_color(dpg.mvPlotCol_XAxisGrid, gridColor, category=dpg.mvThemeCat_Plots)
    dpg.add_theme_color(dpg.mvPlotCol_YAxisGrid, gridColor, category=dpg.mvThemeCat_Plots)

    # Line + Marker
    dpg.add_theme_color(dpg.mvPlotCol_Line, (150, 255, 0), category=dpg.mvThemeCat_Plots)
    # dpg.add_theme_style(dpg.mvPlotStyleVar_Marker, dpg.mvPlotMarker_Circle, category=dpg.mvThemeCat_Plots)
    # dpg.add_theme_color(dpg.mvPlotCol_MarkerOutline, tileColor, dpg.mvPlotMarker_Circle, category=dpg.mvThemeCat_Plots)
    # dpg.add_theme_style(dpg.mvPlotStyleVar_MarkerSize, 4, dpg.mvPlotMarker_Circle, category=dpg.mvThemeCat_Plots)
    dpg.add_theme_style(dpg.mvPlotStyleVar_LineWeight, 4, dpg.mvPlotMarker_Circle, category=dpg.mvThemeCat_Plots)

def setupButtonStyling():
    dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 0, 0, 0))
    dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (0, 0, 0, 0))
    dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (0, 0, 0, 0))

def setupTextures():
    print("lol")
    # dpg.add_static_texture(100, 100, default_value=[80, 87, 105], tag="active-btn", label="Static Texture 1")

    # wallpaperWidth, wallpaperHeight, channels, wallpaperData = dpg.load_image("./assets/chart-bg.png")
    # dpg.add_static_texture(width=wallpaperWidth, height=wallpaperHeight, default_value=wallpaperData, tag="wallpaper_img")

    # Setup icons for all resources

    # for resource in TRACKED_RESOURCES:
    #     iconPath = f"./assets/{resource}.png"
    #     width, height, channels, imgData = dpg.load_image(iconPath)

    #     dpg.add_static_texture(width=width, height=height, default_value=imgData, tag=f"{resource}_icon")

def setupResourceTheme(label: str):
    with dpg.theme(tag=label):
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvPlotCol_Line, TRACKED_RESOURCES[label]['color'], category=dpg.mvThemeCat_Plots)