#ifndef MRBE_INPUT_H
#define MRBE_INPUT_H

#define MRBE_KEY_NONE 0
#define MRBE_KEY_LEFT 1
#define MRBE_KEY_RIGHT 2
#define MRBE_KEY_UP 3
#define MRBE_KEY_DOWN 4
#define MRBE_KEY_ENTER 5
#define MRBE_KEY_BACK 6
#define MRBE_KEY_HOME 7
#define MRBE_KEY_APPS 8
#define MRBE_KEY_SETTINGS 9

typedef struct {
    int fds[32];
    int count;
} MrbeInput;

int mrbe_input_open(MrbeInput *input);
void mrbe_input_close(MrbeInput *input);
int mrbe_input_next(MrbeInput *input, int timeout_ms);

#endif
