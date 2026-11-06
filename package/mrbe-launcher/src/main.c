#include "fb.h"
#include "input.h"
#include "ui.h"

#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char **argv)
{
    MrbeFramebuffer fb;
    MrbeInput input;
    MrbeUIState ui;
    int key;

    if (argc > 1 && strcmp(argv[1], "--version") == 0) {
        puts("MRBE Linux TV Launcher 0.4.0");
        return 0;
    }
    if (argc > 1 && strcmp(argv[1], "--help") == 0) {
        puts("Usage: mrbe-launcher [--version|--help]");
        puts("Arrows/Enter/Esc: navigate; H: home, A: apps, S: settings.");
        return 0;
    }
    if (mrbe_fb_open(&fb, "/dev/fb0") != 0) {
        fprintf(stderr, "MRBE: /dev/fb0 indisponivel. Verifique virtio-gpu e fbdev.\n");
        return 1;
    }
    memset(&input, 0, sizeof(input));
    mrbe_ui_init(&ui);
    mrbe_input_open(&input);
    mrbe_ui_draw(&fb, &ui);
    for (;;) {
        if (input.count == 0) {
            sleep(1);
            mrbe_input_open(&input);
        }
        key = mrbe_input_next(&input, 150);
        if (key == MRBE_KEY_NONE) continue;
        mrbe_ui_handle_key(&ui, key);
        mrbe_ui_draw(&fb, &ui);
    }
    /* Normally the launcher is stopped by init SIGTERM. */
    mrbe_input_close(&input);
    mrbe_fb_close(&fb);
    return 0;
}
