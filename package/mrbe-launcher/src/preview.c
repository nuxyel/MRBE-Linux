/* Offline headless screenshot of the exact MRBE framebuffer renderer.
 * Host-only tool: not part of the ARM64 target package. */
#include "fb.h"
#include "ui.h"
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, char **argv) {
    const int w=1280,h=720;
    const size_t size=(size_t)w*(size_t)h*4u;
    MrbeFramebuffer fb;
    MrbeUIState ui;
    FILE *out;
    int x,y;
    if (argc<2 || argc>3) { fprintf(stderr, "Usage: mrbe-preview output.ppm [apps|settings]\n"); return 2; }
    memset(&fb,0,sizeof(fb));
    fb.memory=calloc(size,1);
    if (!fb.memory) return 2;
    fb.memory_size=size;
    fb.bytes_per_pixel=4;
    fb.fixed.line_length=w*4;
    fb.variable.xres=w;
    fb.variable.yres=h;
    fb.variable.bits_per_pixel=32;
    fb.variable.red.offset=16; fb.variable.red.length=8;
    fb.variable.green.offset=8; fb.variable.green.length=8;
    fb.variable.blue.offset=0; fb.variable.blue.length=8;
    mrbe_ui_init(&ui);
    if (argc == 3 && strcmp(argv[2], "apps") == 0) {
        ui.screen = MRBE_SCREEN_APPS;
    } else if (argc == 3 && strcmp(argv[2], "settings") == 0) {
        ui.screen = MRBE_SCREEN_SETTINGS;
    }
    mrbe_ui_draw(&fb,&ui);
    out=fopen(argv[1],"wb");
    if (!out) { perror("fopen"); free(fb.memory); return 2; }
    fprintf(out,"P6\n%d %d\n255\n",w,h);
    for (y=0;y<h;y++) for(x=0;x<w;x++) {
        size_t i=((size_t)y*w+x)*4;
        uint8_t pixel[3]={fb.memory[i+2],fb.memory[i+1],fb.memory[i]};
        if(fwrite(pixel,1,3,out)!=3) { perror("write"); fclose(out); free(fb.memory); return 2; }
    }
    fclose(out); free(fb.memory);
    return 0;
}
