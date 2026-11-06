#ifndef MRBE_UI_H
#define MRBE_UI_H

#include "fb.h"
#include "input.h"

typedef enum {
    MRBE_SCREEN_HOME = 0,
    MRBE_SCREEN_APPS,
    MRBE_SCREEN_SETTINGS
} MrbeScreen;

typedef enum {
    MRBE_FOCUS_NAV = 0,
    MRBE_FOCUS_HERO,
    MRBE_FOCUS_CONTENT
} MrbeFocus;

typedef struct {
    MrbeScreen screen;
    MrbeFocus focus;
    int nav_index;
    int hero_index;
    int content_row;
    int content_col;
    int apps_index;
    int settings_index;
    int show_notice;
    char notice[128];
} MrbeUIState;

void mrbe_ui_init(MrbeUIState *state);
void mrbe_ui_handle_key(MrbeUIState *state, int key);
void mrbe_ui_draw(MrbeFramebuffer *fb, const MrbeUIState *state);

#endif
